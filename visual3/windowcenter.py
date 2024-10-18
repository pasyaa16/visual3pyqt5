from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QApplication, QDesktopWidget

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Label1", self)
        self.label.move(200, 0)
        self.button = QPushButton("Button1", self)
        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle("Belajar PyQt5")
        self.center_window()

    def center_window(self):
        frame_geom = self.frameGeometry()
        screen_center = QDesktopWidget().availableGeometry().center()
        frame_geom.moveCenter(screen_center)
        self.move(frame_geom.topLeft())

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()
