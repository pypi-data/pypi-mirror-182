from PyQt5 import QtWidgets, QtCore, QtGui
import sys

# Coded by Xenely


# Структурные классы
class Alignment:

    left = QtCore.Qt.AlignLeft
    center = QtCore.Qt.AlignCenter
    right = QtCore.Qt.AlignRight


class PenType:

    dot = QtCore.Qt.DotLine
    dash = QtCore.Qt.DashLine
    solid = QtCore.Qt.SolidLine
    dashdot = QtCore.Qt.DashDotLine
    dashdotdot = QtCore.Qt.DashDotDotLine


class BrushType:

    hor = QtCore.Qt.HorPattern
    ver = QtCore.Qt.VerPattern
    nobrush = QtCore.Qt.NoBrush
    solid = QtCore.Qt.SolidPattern
    bdiag = QtCore.Qt.BDiagPattern
    fdiag = QtCore.Qt.FDiagPattern
    cross = QtCore.Qt.CrossPattern
    dense1 = QtCore.Qt.Dense1Pattern
    dense2 = QtCore.Qt.Dense2Pattern
    dense3 = QtCore.Qt.Dense3Pattern
    dense4 = QtCore.Qt.Dense4Pattern
    dense5 = QtCore.Qt.Dense5Pattern
    dense6 = QtCore.Qt.Dense6Pattern
    dense7 = QtCore.Qt.Dense7Pattern
    diagcross = QtCore.Qt.DiagCrossPattern


class RenderHints:

    antialiasing = QtGui.QPainter.Antialiasing
    text_antialiasing = QtGui.QPainter.TextAntialiasing
    qt4_compatible_painting = QtGui.QPainter.Qt4CompatiblePainting
    smooth_pixmap_transform = QtGui.QPainter.SmoothPixmapTransform
    non_cosmetic_default_pen = QtGui.QPainter.NonCosmeticDefaultPen
    lossless_image_rendering = QtGui.QPainter.LosslessImageRendering
    hight_quality_antialiasing = QtGui.QPainter.HighQualityAntialiasing


# Классы оверлея
class OverlayFont:

    def __init__(self, font_family: str, size: int) -> None:

        self.__font = QtGui.QFont()
        self.__font.setFamily(font_family)
        self.__font.setPixelSize(size)

    def set_family(self, font_family: str) -> None:

        self.__font.setFamily(font_family)

    def set_size(self, size: int) -> None:

        self.__font.setPixelSize(size)

    def get_font(self) -> QtGui.QFont:

        return self.__font


class Overlay(QtWidgets.QWidget):

    def __init__(self, update_inverval_ms: int) -> None:

        super().__init__()

        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_DisableHighDpiScaling)

        # Прозрачность
        self.setWindowFlags(QtCore.Qt.Tool | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.WindowTransparentForInput)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Статические переменные
        self.draw_list = []
        self.geometry_list = []
        self.__overlay_painter = QtGui.QPainter()
        self.__render_hint = RenderHints.hight_quality_antialiasing

        # Таймер, необходим для обновления оверлея
        self.__timer = QtCore.QTimer(self)
        self.__timer.setInterval(update_inverval_ms)
        self.__timer.timeout.connect(lambda: self.update())
        self.__timer.start()

    # Ф-ия рисовальщик
    def paintEvent(self, event: object) -> None:

        self.__overlay_painter.begin(self)
        self.__overlay_painter.setRenderHint(self.__render_hint)

        if self.geometry_list:
            self.setGeometry(*self.geometry_list)
            self.geometry_list.clear()

        for shape in self.draw_list:

            if shape["type"] == "rect":
                self.__set_rect(event, self.__overlay_painter, shape["x"], shape["y"], shape["width"], shape["height"], shape["line_size"], shape["line_type"], shape["color"])
            if shape["type"] == "ellipse":
                self.__set_ellipse(event, self.__overlay_painter, shape["x"], shape["y"], shape["width"], shape["height"], shape["line_size"], shape["line_type"], shape["color"])
            if shape["type"] == "line":
                self.__set_line(event, self.__overlay_painter, shape["x1"], shape["y1"], shape["x2"], shape["y2"], shape["line_size"], shape["line_type"], shape["color"])
            if shape["type"] == "text":
                self.__set_text(event, self.__overlay_painter, shape["x"], shape["y"], shape["width"], shape["height"], shape["text"], shape["font"], shape["align"], shape["color"])
            if shape["type"] == "polygon":
                self.__set_polygon(event, self.__overlay_painter, shape["points"], shape["line_size"], shape["line_type"], shape["color"])

        self.__overlay_painter.end()

    def set_render_hint(self, render_hint: RenderHints) -> None:

        self.__render_hint = render_hint

    def set_timer_interval(self, update_ms_interval: int) -> None:

        self.__timer.setInterval(update_ms_interval)

    # Скрытые методы
    def __set_rect(self, event: object, painter: object, x: int, y: int, w: int, h: int, line_size: int, line_type: PenType, color: tuple[int, ...]) -> None:

        if line_size <= 0:
            painter.setPen(QtGui.QPen(QtGui.QColor(*color), line_size, line_type))
            painter.setBrush(QtGui.QBrush(QtGui.QColor(*color), BrushType.solid))
            painter.drawRect(x, y, w, h)

        else:
            painter.setPen(QtGui.QPen(QtGui.QColor(*color), line_size, line_type))
            painter.setBrush(QtGui.QBrush(QtGui.QColor(*color), BrushType.nobrush))
            painter.drawRect(x, y, w, h)

    def __set_ellipse(self, event: object, painter: object, x: int, y: int, w: int, h: int, line_size: int, line_type: PenType, color: tuple) -> None:

        if line_size <= 0:
            painter.setPen(QtGui.QPen(QtGui.QColor(*color), line_size, line_type))
            painter.setBrush(QtGui.QBrush(QtGui.QColor(*color), BrushType.nobrush))
            painter.drawEllipse(x, y, w, h)

        else:
            painter.setPen(QtGui.QPen(QtGui.QColor(*color), line_size, line_type))
            painter.setBrush(QtGui.QBrush(QtGui.QColor(*color), BrushType.nobrush))
            painter.drawEllipse(x, y, w, h)

    def __set_line(self, event: object, painter: object, x1: int, y1: int, x2: int, y2: int, line_size: int, line_type: object, color: tuple) -> None:

        painter.setPen(QtGui.QPen(QtGui.QColor(*color), line_size, line_type))
        painter.drawLine(x1, y1, x2, y2)

    def __set_text(self, event: object, painter: object, x: int, y: int, w: int, h: int, text: str, font: OverlayFont, align: object, color: tuple):

        painter.setPen(QtGui.QPen(QtGui.QColor(*color)))
        painter.setFont(font.get_font())
        painter.drawText(QtCore.QRect(x, y, w, h), align, text)

    def __set_polygon(self, event: object, painter: object, points: list, line_size: int, line_type: object, color: tuple) -> None:

        if line_size <= 0:
            painter.setPen(QtGui.QPen(QtGui.QColor(*color), line_size, line_type))
            painter.setBrush(QtGui.QBrush(QtGui.QColor(*color), BrushType.solid))

            polygon = []
            for point in points:
                polygon.append(QtCore.QPoint(point["x"], point["y"]))

            polygon = QtGui.QPolygon(polygon)

        else:
            painter.setPen(QtGui.QPen(QtGui.QColor(*color), line_size, line_type))
            painter.setBrush(QtGui.QBrush(QtGui.QColor(*color), BrushType.nobrush))

            polygon = []
            for point in points:
                polygon.append(QtCore.QPoint(point["x"], point["y"]))

            polygon = QtGui.QPolygon(polygon)

        painter.drawPolygon(polygon)


# Инициализация
def application_init() -> QtWidgets.QApplication:

    return QtWidgets.QApplication(sys.argv)


def application_start(application: QtWidgets.QApplication) -> None:

    application.exec()
