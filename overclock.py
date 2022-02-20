import sys
from PyQt6 import QtGui, QtCore, QtWidgets
from PyQt6.QtCore import Qt


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None, flags=Qt.WindowType.Window):
        super(MainWindow, self).__init__(parent, flags=flags)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.widget = Widget(self)
        self.setCentralWidget(self.widget)


class Widget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(Widget, self).__init__(parent)
        self.text_edit = QtWidgets.QPlainTextEdit()
        self.setStyleSheet(
            """QPlainTextEdit { 
                color: #2c2c2c;
                background: rgba(0, 0, 0, 0);
            }"""
                           )

        opacity = QtWidgets.QGraphicsOpacityEffect()
        opacity.setOpacity(0.7)
        self.text_edit.setGraphicsEffect(opacity)

        self.layout = QtWidgets.QVBoxLayout(self)
        timer = QtCore.QTimer(self, timeout=self.update_time)
        self.update_time()
        timer.start(1000)

        self.layout.addWidget(self.text_edit, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.layout)

    @QtCore.pyqtSlot()
    def update_time(self):
        time = QtCore.QTime.currentTime()
        text = time.toString("hh:mm")
        pen = QtGui.QPen(QtGui.QColor("#e8e8e8"), 2,
                         Qt.PenStyle.SolidLine,
                         Qt.PenCapStyle.SquareCap,
                         Qt.PenJoinStyle.MiterJoin
                         )
        text_format = QtGui.QTextCharFormat()
        font = QtGui.QFont("Helvetica [Cronyx]", 50, QtGui.QFont.Weight.Bold)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferQuality)
        text_format.setFont(font)
        text_format.setTextOutline(pen)
        self.text_edit.setCurrentCharFormat(text_format)
        self.text_edit.setPlainText(text)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    screen_geometry = QtGui.QGuiApplication.primaryScreen().geometry()
    screen_height = screen_geometry.height()
    screen_width = screen_geometry.width()
    main_window = MainWindow(flags=
                             Qt.WindowType.WindowStaysOnTopHint |
                             Qt.WindowType.WindowTransparentForInput |
                             Qt.WindowType.BypassWindowManagerHint |
                             Qt.WindowType.FramelessWindowHint
                             )
    main_window.adjustSize()
    window_height = 130
    window_width = 220
    main_window.setGeometry(
        screen_width - window_width - 20,
        screen_height - window_height - 25,
        window_width,
        window_height
    )
    main_window.show()
    app.exec()
