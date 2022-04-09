# Note - This can be run using something like pyuic5 main_window.ui > skeleton.py

from PyQt5 import QtCore, QtGui, QtWidgets
from camera_module import CameraModule

# This allows us to exit the program when ctrl-c is pressed
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)


class Ui_main_window_(object):
    def setupUi(self, main_window_, camera_module):
        main_window_.setObjectName("main_window_")
        main_window_.resize(177, 221)
        self.central_widget_ = QtWidgets.QWidget(main_window_)
        self.central_widget_.setObjectName("central_widget_")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.central_widget_)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 171, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.vertical_layout_ = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.vertical_layout_.setContentsMargins(4, 4, 4, 4)
        self.vertical_layout_.setObjectName("vertical_layout_")

        self.status_ = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.status_.setObjectName("status_")
        self.vertical_layout_.addWidget(self.status_)

        # Connect the status label to the camera module
        camera_module.status_changed_.connect(self.status_.setText)

        self.start_preview_btn_ = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.start_preview_btn_.setObjectName("start_preview_btn_")
        self.start_preview_btn_.clicked.connect(camera_module.start_preview_clicked)
        self.vertical_layout_.addWidget(self.start_preview_btn_)

        self.end_preview_btn_ = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.end_preview_btn_.setObjectName("end_preview_btn_")
        self.end_preview_btn_.clicked.connect(camera_module.end_preview_clicked)
        self.vertical_layout_.addWidget(self.end_preview_btn_)

        self.take_picture_btn_ = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.take_picture_btn_.setObjectName("take_picture_btn_")
        self.take_picture_btn_.clicked.connect(camera_module.take_picture_clicked)
        self.vertical_layout_.addWidget(self.take_picture_btn_)

        self.start_video_recording_btn_ = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.start_video_recording_btn_.setObjectName("start_video_recording_btn_")
        self.start_video_recording_btn_.clicked.connect(camera_module.start_video_recording_clicked)
        self.vertical_layout_.addWidget(self.start_video_recording_btn_)

        self.stop_video_recording_btn_ = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.stop_video_recording_btn_.setObjectName("stop_video_recording_btn_")
        self.stop_video_recording_btn_.clicked.connect(camera_module.stop_video_recording_clicked)
        self.vertical_layout_.addWidget(self.stop_video_recording_btn_)

        self.save_last_20_seconds_btn_ = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.save_last_20_seconds_btn_.setObjectName("save_last_20_seconds_btn_")
        self.save_last_20_seconds_btn_.clicked.connect(camera_module.save_last_20_seconds_clicked)
        self.vertical_layout_.addWidget(self.save_last_20_seconds_btn_)

        self.file_name_input_ = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.file_name_input_.setObjectName("file_name_input_")
        self.file_name_input_.textChanged.connect(camera_module.file_name_changed)
        self.vertical_layout_.addWidget(self.file_name_input_)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vertical_layout_.addItem(spacerItem)
        main_window_.setCentralWidget(self.central_widget_)
        self.menubar = QtWidgets.QMenuBar(main_window_)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 177, 22))
        self.menubar.setObjectName("menubar")
        self.menutest = QtWidgets.QMenu(self.menubar)
        self.menutest.setObjectName("menutest")
        main_window_.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window_)
        self.statusbar.setObjectName("statusbar")
        main_window_.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menutest.menuAction())

        self.retranslateUi(main_window_)
        QtCore.QMetaObject.connectSlotsByName(main_window_)

    def retranslateUi(self, main_window_):
        _translate = QtCore.QCoreApplication.translate
        main_window_.setWindowTitle(_translate("main_window_", "MainWindow"))
        self.status_.setText(_translate("main_window_", "TextLabel"))
        self.start_preview_btn_.setText(_translate("main_window_", "Start Preview"))
        self.end_preview_btn_.setText(_translate("main_window_", "End Preview"))
        self.take_picture_btn_.setText(_translate("main_window_", "Take Picture"))
        self.start_video_recording_btn_.setText(_translate("main_window_", "Start Video Recording"))
        self.stop_video_recording_btn_.setText(_translate("main_window_", "Stop Video Recording"))
        self.save_last_20_seconds_btn_.setText(_translate("main_window_", "Save last 20 seconds"))
        self.menutest.setTitle(_translate("main_window_", "Options"))


def init():
    print ("Main window shown")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window_ = QtWidgets.QMainWindow()
    ui = Ui_main_window_()

    camera_module = CameraModule()
    ui.setupUi(main_window_, camera_module)
    main_window_.show()

    init()

    app.exec_()

