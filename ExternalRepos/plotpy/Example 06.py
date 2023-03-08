import os.path as osp, numpy as np
from plotpy.plot import ImageDialog
from plotpy.builder import make


def create_window():
    win = ImageDialog(edit=False, toolbar=True, wintitle="Cross sections test", options=dict(show_xsection=True, show_ysection=True, show_itemlist=True))
    win.resize(800, 600)
    return win

def test():
    """Test"""
    # -- Create QApplication
    import guidata
    _app = guidata.qapplication()
    # --
    filename = osp.join(osp.dirname(__file__), "brain.png")
    win = create_window()
    image = make.image(filename=filename, colormap="bone")
    data2 = np.array(image.data.T[200:], copy=True)
    image2 = make.image(data2, title="Modified", alpha_mask=True)
    plot = win.get_plot()
    plot.add_item(image)
    plot.add_item(image2, z=1)
    win.exec_()


if __name__ == "__main__":
    test()
