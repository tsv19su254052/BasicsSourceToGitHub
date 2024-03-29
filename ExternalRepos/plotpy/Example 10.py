import numpy as np
import guidata.qt.QtCore as QtCore
import guidata.qt.QtGui as QtGui
import guidata.dataset.datatypes as gdt
import guidata.dataset.dataitems as gdi
import guidata.dataset.qtwidgets as gdq
import guidata.configtools as configtools
import plotpy.plot as gqp
import plotpy.curve as gqc
import plotpy.image as gqi
import plotpy.tools as gqt


class DotArrayParam(gdt.DataSet):
    """Dot array"""
    g1 = gdt.BeginGroup("Size of the area")
    dim_h = gdi.FloatItem("Width", default=20, min=0, unit="mm")
    dim_v = gdi.FloatItem("Height", default=20, min=0, unit="mm")
    _g1 = gdt.EndGroup("Size of the area")

    g2 = gdt.BeginGroup("Grid pattern properties")
    step_x = gdi.FloatItem("Step in X-axis", default=1, min=1, unit="mm")
    step_y = gdi.FloatItem("Step in Y-axis", default=1, min=1, unit="mm")
    size = gdi.FloatItem("Dot size", default=.2, min=0, max=2, slider=True, unit="mm")
    color = gdi.ColorItem("Dot color", default="red")
    _g2 = gdt.EndGroup("Grid pattern properties")

    def update_image(self, obj):
        self._update_cb()

    def update_param(self, obj):
        pass


class DotArrayItem(gqi.RawImageItem):
    def __init__(self, imageparam=None):
        super(DotArrayItem, self).__init__(np.zeros((1, 1)), imageparam)
        self.update_border()

    def boundingRect(self):
        param = self.imageparam
        if param is not None:
            return QtCore.QRectF(QtCore.QPointF(-.5 * param.size, -.5 * param.size), QtCore.QPointF(param.dim_h + .5 * param.size, param.dim_v + .5 * param.size))

    def types(self):
        return (gqi.IImageItemType,)

    def draw_image(self, painter, canvasRect, srcRect, dstRect, xMap, yMap):
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        param = self.imageparam
        xcoords = gqc.vmap(xMap, np.arange(0, param.dim_h + 1, param.step_x))
        ycoords = gqc.vmap(yMap, np.arange(0, param.dim_v + 1, param.step_y))
        rx = .5 * param.size * xMap.pDist() / xMap.sDist()
        ry = .5 * param.size * yMap.pDist() / yMap.sDist()
        color = QtGui.QColor(param.color)
        painter.setPen(QtGui.QPen(color))
        painter.setBrush(QtGui.QBrush(color))
        for xc in xcoords:
            for yc in ycoords:
                painter.drawEllipse(QtCore.QPointF(xc, yc), rx, ry)


class CustomHelpTool(gqt.HelpTool):
    def activate_command(self, plot, checked):
        QtGui.QMessageBox.information(plot, "Help",
                                      """**to be customized**
      Keyboard/mouse shortcuts:
        - single left-click: item (curve, image, ...) selection
        - single right-click: context-menu relative to selected item
        - shift: on-active-curve (or image) cursor
        - alt: free cursor
        - left-click + mouse move: move item (when available)
        - middle-click + mouse move: pan
        - right-click + mouse move: zoom""")


class DotArrayDialog(gqp.ImageDialog):
    def __init__(self):
        self.item = None
        self.stamp_gbox = None
        super(DotArrayDialog, self).__init__(wintitle="Dot array example",
                                             #            icon="path/to/your_icon.png",
                                             toolbar=True, edit=True)
        self.resize(900, 600)

    def register_tools(self):
        self.register_standard_tools()
        self.add_separator_tool()
        self.add_tool(gqt.SaveAsTool)
        self.add_tool(gqt.CopyToClipboardTool)
        self.add_tool(gqt.PrintTool)
        self.add_tool(CustomHelpTool)
        self.activate_default_tool()
        plot = self.get_plot()
        plot.enableAxis(plot.yRight, False)
        plot.set_aspect_ratio(lock=True)

    def create_plot(self, options):
        logo_path = configtools.get_image_file_path("plotpy.svg")
        logo = QtGui.QLabel()
        logo.setPixmap(QtGui.QPixmap(logo_path))
        logo.setAlignment(QtCore.Qt.AlignCenter)
        self.plot_layout.addWidget(logo, 1, 1)
        logo_txt = QtGui.QLabel("Powered by <b>plotpy</b>")
        logo_txt.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.plot_layout.addWidget(logo_txt, 2, 1)
        self.stamp_gbox = gdq.DataSetEditGroupBox("Dots", DotArrayParam)
        try:
            # plotpy v3:
            self.stamp_gbox.SIG_APPLY_BUTTON_CLICKED.connect(self.apply_params)
        except AttributeError:
            # plotpy v2:
            from guidata.qt.QtCore import SIGNAL
            self.connect(self.stamp_gbox, SIGNAL("apply_button_clicked()"), self.apply_params)
        self.plot_layout.addWidget(self.stamp_gbox, 0, 1)
        options = dict(title="Main plot")
        gqp.ImageDialog.create_plot(self, options, 0, 0, 3, 1)

    def show_data(self, param):
        plot = self.get_plot()
        if self.item is None:
            param._update_cb = lambda: self.stamp_gbox.get()
            self.item = DotArrayItem(param)
            plot.add_item(self.item)
        else:
            self.item.update_border()
        plot.do_autoscale()

    def apply_params(self):
        param = self.stamp_gbox.dataset
        self.show_data(param)


if __name__ == "__main__":
    # -- Create QApplication
    import guidata
    _app = guidata.qapplication()
    dlg = DotArrayDialog()
    dlg.apply_params()
    dlg.exec_()
    