from guidata.qt.QtCore import QRectF
from guidata.qt.QtGui import QImage
import os
import numpy as np
from plotpy.image import assemble_imageitems
from plotpy.plot import ImageDialog
from plotpy.builder import make
from plotpy import io


DEFAULT_CHARS = "".join([chr(c) for c in range(32, 256)])


def get_font_array(sz, chars=DEFAULT_CHARS):
    from guidata.qt.QtGui import QFont, QPainter, QColor
    font = QFont()
    font.setFixedPitch(True)
    font.setPixelSize(sz)
    font.setStyleStrategy(QFont.NoAntialias)
    dummy = QImage(10, 10, QImage.Format_ARGB32)
    pnt = QPainter(dummy)
    pnt.setFont(font)
    metric = pnt.fontMetrics()
    rct = metric.boundingRect(chars)
    pnt.end()
    h = rct.height()
    w = rct.width()
    img = QImage(w, h, QImage.Format_ARGB32)
    paint = QPainter()
    paint.begin(img)
    paint.setFont(font)
    paint.setBrush( QColor(255, 255, 255) )
    paint.setPen( QColor(255, 255, 255) )
    paint.drawRect(0, 0, w+1, h+1)
    paint.setPen( QColor(0, 0, 0))
    paint.setBrush( QColor(0, 0, 0) )
    paint.drawText(0, paint.fontMetrics().ascent(), chars)
    paint.end()
    try:
        try:
            data = img.bits().asstring(img.numBytes())
        except AttributeError:
            # PyQt5
            data = img.bits().asstring(img.byteCount())
    except SystemError:
        # Python 3
        return
    npy = np.frombuffer(data, np.uint8)
    npy.shape = img.height(), img.bytesPerLine()/4, 4
    return npy[:,:, 0]


def txtwrite(data, x, y, sz, txt, range=None):
    arr = get_font_array(sz, txt)
    if arr is None:
        return
    if range is None:
        m, M = data.min(), data.max()
    else:
        m, M = range
    z = (float(M)-float(m))*np.array(arr, float)/255.+m
    arr = np.array(z, data.dtype)
    dy, dx = arr.shape
    data[y:y+dy, x:x+dx] = arr


def imshow(items, title=""):
    gridparam = make.gridparam(background="black", minor_enabled=(False, False), major_style=(".", "gray", 1))
    win = ImageDialog(edit=False, toolbar=True, wintitle=title, options=dict(gridparam=gridparam))
    nc = int(np.sqrt(len(items))+1.0)
    maxy = 0
    y = 0
    x = 0
    w = None
    plot = win.get_plot()
    print("-"*80)
    for i, item in enumerate(items):
        h = item.boundingRect().height()
        if i%nc==0:
            x = 0
            y += maxy
            maxy = h
        else:
            x += w
            maxy = max(maxy, h)
        w = item.boundingRect().width()
        item.set_transform(x, y, 0.0)
        print("Adding item #%d..." % i, end=' ')
        plot.add_item(item)
        print("Done")
    win.show()
    win.exec_()


def compute_image(NX, NY):
    BX, BY = 40, 40
    img = np.random.normal(0, 100, size=(BX, BY))
    timg = np.fft.fftshift(np.fft.fft2(img))
    print(timg.shape)
    cx = NX/2
    cy = NY/2
    bx2 = BX/2
    by2 = BY/2
    z=np.zeros( (NX, NY), np.complex64)
    z[cx-bx2:cx-bx2+BX, cy-by2:cy-by2+BY] = timg
    z = np.fft.ifftshift(z)
    rev = np.fft.ifft2(z)
    return np.abs(rev)


def get_bbox(items):
    r = QRectF()
    for it in items:
        r = r.united(it.boundingRect())
    return r


def save_image(name, data):
    for fname in (name+".u16.tif", name+".u8.png"):
        if os.path.exists(fname):
            os.remove(fname)
    print("Saving image: %d x %d (%d KB):" % (data.shape[0], data.shape[1], data.nbytes/1024.))
    print(" --> uint16")
    io.imwrite(name+".u16.tif", data, dtype=np.uint16, max_range=True)
    print(" --> uint8")
    io.imwrite(name+".u8.png", data, dtype=np.uint8, max_range=True)


def build_image(items):
    r = get_bbox(items)
    x, y, w, h = r.getRect()
    print("-"*80)
    print("Assemble test1:", w, "x", h)
    dest = assemble_imageitems(items, r, w, h)
    save_image("test1", dest)
    print("-"*80)
    print("Assemble test2:", w/4, "x", h/4)
    dest = assemble_imageitems(items, r, w/4, h/4)
    save_image("test2", dest)
    print("-"*80)


def test():
    """Test"""
    N = 500
    data = compute_image(N, N)
    m = data.min()
    M = data.max()
    items = [make.trimage(data, alpha_mask=True, colormap="jet")]
    for type in (np.uint8, np.uint16, np.int8, np.int16):
        info = np.iinfo(type().dtype)
        s = float((info.max-info.min))
        a1 = s*(data-m)/(M-m)
        img = np.array(a1+info.min, type)
        txtwrite(img, 0, 0, N/15., str(type))
        items.append(make.trimage(img, colormap="jet"))
    imshow(items, title="Transform test (%dx%d images)" % (N, N))
    return items


if __name__ == "__main__":
    # -- Create QApplication
    import guidata
    _app = guidata.qapplication()
    # --
    items = test()
    build_image(items)
