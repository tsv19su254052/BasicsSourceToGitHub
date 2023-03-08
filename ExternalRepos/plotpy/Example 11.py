import os.path as osp

from plotpy.plot import ImageDialog
from plotpy.tools import (RectangleTool, EllipseTool, HRangeTool, PlaceAxesTool,
                          MultiLineTool, FreeFormTool, SegmentTool, CircleTool,
                          AnnotatedRectangleTool, AnnotatedEllipseTool,
                          AnnotatedSegmentTool, AnnotatedCircleTool, LabelTool,
                          AnnotatedPointTool,
                          VCursorTool, HCursorTool, XCursorTool,
                          ObliqueRectangleTool, AnnotatedObliqueRectangleTool)
from plotpy.builder import make


def create_window():
    win = ImageDialog(edit=False, toolbar=True, wintitle="All image and plot tools test")
    for toolklass in (LabelTool, HRangeTool,
                      VCursorTool, HCursorTool, XCursorTool,
                      SegmentTool, RectangleTool, ObliqueRectangleTool,
                      CircleTool, EllipseTool,
                      MultiLineTool, FreeFormTool, PlaceAxesTool,
                      AnnotatedRectangleTool, AnnotatedObliqueRectangleTool,
                      AnnotatedCircleTool, AnnotatedEllipseTool,
                      AnnotatedSegmentTool, AnnotatedPointTool):
        win.add_tool(toolklass)
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
    plot = win.get_plot()
    plot.add_item(image)
    win.exec_()


if __name__ == "__main__":
    test()
    