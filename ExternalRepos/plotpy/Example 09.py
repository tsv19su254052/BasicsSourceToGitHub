from numpy import random, array, dot, concatenate
from plotpy.plot import ImageDialog
from plotpy.builder import make
from plotpy.config import _


def hist2d(X, Y):
    win = ImageDialog(edit=True, toolbar=True, wintitle="2-D Histogram X0=(0,1), X1=(-1,-1)")
    hist2d = make.histogram2D(X, Y, 200, 200)
    curve = make.curve(X[::50], Y[::50], linestyle='', marker='+', title=_("Markers"))
    plot = win.get_plot()
    plot.set_aspect_ratio(lock=False)
    plot.set_antialiasing(False)
    plot.add_item(hist2d)
    plot.add_item(curve)
    plot.set_item_visible(curve, False)
    win.show()
    win.exec_()


if __name__ == "__main__":
    import guidata
    _app = guidata.qapplication()
    N = 150000
    m = array([[ 1., .2], [-.2, 3.]])
    X1 = random.normal(0, .3, size=(N, 2))
    X2 = random.normal(0, .3, size=(N, 2))
    X = concatenate((X1+[0, 1.], dot(X2, m)+[-1, -1.]))
    hist2d(X[:, 0], X[:, 1])
    