import os.path as osp
from plotpy.plot import ImageDialog
from plotpy.builder import make


def test():
    """Test"""
    # -- Create QApplication
    import guidata
    _app = guidata.qapplication()
    # --
    filename = osp.join(osp.dirname(__file__), "brain.png")
    image = make.image(filename=filename, title="Original", colormap='gray')
    win = ImageDialog(edit=False, toolbar=True, wintitle="Contrast test", options=dict(show_contrast=True))
    plot = win.get_plot()
    plot.add_item(image)
    win.resize(600, 600)
    win.show()
    try:
        plot.save_widget('contrast.png')
    except IOError:
        # Skipping this part of the test
        # because user has no write permission on current directory
        pass
    win.exec_()


if __name__ == "__main__":
    test()
    