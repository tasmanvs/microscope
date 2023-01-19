# Note - This can be run using something like pyuic5 main_window.ui > skeleton.py

from PyQt5 import QtCore, QtGui, QtWidgets
from camera_module import CameraModule

# This allows us to exit the program when ctrl-c is pressed
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)


class Ui_main_window_(object):
    def setupUi(self, main_window_, camera_module):
        main_window_.setObjectName("main_window_")
        main_window_.resize(683, 567)
        self.central_widget_ = QtWidgets.QWidget(main_window_)
        self.central_widget_.setObjectName("central_widget_")
        self.layoutWidget = QtWidgets.QWidget(self.central_widget_)
        self.layoutWidget.setGeometry(QtCore.QRect(1, 1, 173, 469))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 20, 180, 70))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.start_timelapse_btn_ = QtWidgets.QPushButton(self.layoutWidget1)
        self.start_timelapse_btn_.setObjectName("start_timelapse_btn_")
        self.horizontalLayout_2.addWidget(self.start_timelapse_btn_)
        self.stop_timelapse_btn_ = QtWidgets.QPushButton(self.layoutWidget1)
        self.stop_timelapse_btn_.setObjectName("stop_timelapse_btn_")
        self.horizontalLayout_2.addWidget(self.stop_timelapse_btn_)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.timelapse_delay_spinbox_ = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.timelapse_delay_spinbox_.setObjectName("timelapse_delay_spinbox_")
        self.horizontalLayout.addWidget(self.timelapse_delay_spinbox_)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.vertical_layout_ = QtWidgets.QVBoxLayout()
        self.vertical_layout_.setContentsMargins(4, 4, 4, 4)
        self.vertical_layout_.setObjectName("vertical_layout_")
        self.status_ = QtWidgets.QLabel(self.layoutWidget)
        self.status_.setObjectName("status_")
        self.vertical_layout_.addWidget(self.status_)
        self.opencv_capture_ = QtWidgets.QPushButton(self.layoutWidget)
        self.opencv_capture_.setObjectName("opencv_capture_")
        self.vertical_layout_.addWidget(self.opencv_capture_)
        self.start_preview_btn_ = QtWidgets.QPushButton(self.layoutWidget)
        self.start_preview_btn_.setObjectName("start_preview_btn_")
        self.vertical_layout_.addWidget(self.start_preview_btn_)
        self.end_preview_btn_ = QtWidgets.QPushButton(self.layoutWidget)
        self.end_preview_btn_.setObjectName("end_preview_btn_")
        self.vertical_layout_.addWidget(self.end_preview_btn_)
        self.take_picture_btn_ = QtWidgets.QPushButton(self.layoutWidget)
        self.take_picture_btn_.setObjectName("take_picture_btn_")
        self.vertical_layout_.addWidget(self.take_picture_btn_)
        self.start_video_recording_btn_ = QtWidgets.QPushButton(self.layoutWidget)
        self.start_video_recording_btn_.setObjectName("start_video_recording_btn_")
        self.vertical_layout_.addWidget(self.start_video_recording_btn_)
        self.stop_video_recording_btn_ = QtWidgets.QPushButton(self.layoutWidget)
        self.stop_video_recording_btn_.setObjectName("stop_video_recording_btn_")
        self.vertical_layout_.addWidget(self.stop_video_recording_btn_)
        self.save_last_20_seconds_btn_ = QtWidgets.QPushButton(self.layoutWidget)
        self.save_last_20_seconds_btn_.setObjectName("save_last_20_seconds_btn_")
        self.vertical_layout_.addWidget(self.save_last_20_seconds_btn_)
        self.file_name_input_ = QtWidgets.QLineEdit(self.layoutWidget)
        self.file_name_input_.setObjectName("file_name_input_")
        self.vertical_layout_.addWidget(self.file_name_input_)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vertical_layout_.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.vertical_layout_)
        self.image_label_ = QtWidgets.QLabel(self.central_widget_)
        self.image_label_.setGeometry(QtCore.QRect(180, 0, 251, 231))
        self.image_label_.setObjectName("image_label_")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.central_widget_)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(180, 350, 481, 121))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.recent_images_hlayout_ = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.recent_images_hlayout_.setContentsMargins(0, 0, 0, 0)
        self.recent_images_hlayout_.setObjectName("recent_images_hlayout_")
        self.thumbnail_0 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.thumbnail_0.setObjectName("thumbnail_0")
        self.recent_images_hlayout_.addWidget(self.thumbnail_0)
        self.thumbnail_1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.thumbnail_1.setObjectName("thumbnail_1")
        self.recent_images_hlayout_.addWidget(self.thumbnail_1)
        self.thumbnail_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.thumbnail_2.setObjectName("thumbnail_2")
        self.recent_images_hlayout_.addWidget(self.thumbnail_2)
        self.thumbnail_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.thumbnail_3.setObjectName("thumbnail_3")
        self.recent_images_hlayout_.addWidget(self.thumbnail_3)
        main_window_.setCentralWidget(self.central_widget_)
        self.menubar = QtWidgets.QMenuBar(main_window_)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 683, 37))
        self.menubar.setObjectName("menubar")
        self.menutest = QtWidgets.QMenu(self.menubar)
        self.menutest.setObjectName("menutest")
        main_window_.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window_)
        self.statusbar.setObjectName("statusbar")
        main_window_.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menutest.menuAction())

        # Connect the status label to the camera module
        # Hook up slots
        camera_module.status_changed_.connect(self.status_.setText)
        camera_module.cv_image_changed_.connect(self.cv_image_changed)
        self.start_preview_btn_.clicked.connect(camera_module.start_preview_clicked)
        self.end_preview_btn_.clicked.connect(camera_module.end_preview_clicked)
        self.take_picture_btn_.clicked.connect(camera_module.take_picture_clicked)
        self.start_video_recording_btn_.clicked.connect(camera_module.start_video_recording_clicked)
        self.stop_video_recording_btn_.clicked.connect(camera_module.stop_video_recording_clicked)
        self.save_last_20_seconds_btn_.clicked.connect(camera_module.record_circular_buffer_clicked)
        self.file_name_input_.textChanged.connect(camera_module.file_name_changed)
        self.opencv_capture_.clicked.connect(camera_module.opencv_capture_clicked)

        # Update the image queue thumbnails
        camera_module.image_queue_changed_.connect(self.update_image_queue_thumbnails)

        # Hook up timelapse slots
        self.start_timelapse_btn_.clicked.connect(camera_module.start_timelapse_clicked)
        self.stop_timelapse_btn_.clicked.connect(camera_module.stop_timelapse_clicked)
        self.timelapse_delay_spinbox_.valueChanged.connect(camera_module.timelapse_delay_changed)

        QtCore.QMetaObject.connectSlotsByName(main_window_)
        self.retranslateUi(main_window_)

    def retranslateUi(self, main_window_):
        _translate = QtCore.QCoreApplication.translate
        main_window_.setWindowTitle(_translate("main_window_", "MainWindow"))
        self.groupBox.setTitle(_translate("main_window_", "Timelapse"))
        self.start_timelapse_btn_.setText(_translate("main_window_", "Start"))
        self.stop_timelapse_btn_.setText(_translate("main_window_", "Stop"))
        self.label.setText(_translate("main_window_", "Delay (Seconds)"))
        self.status_.setText(_translate("main_window_", "TextLabel"))
        self.opencv_capture_.setText(_translate("main_window_", "OpenCV Capture"))
        self.start_preview_btn_.setText(_translate("main_window_", "Start Preview"))
        self.end_preview_btn_.setText(_translate("main_window_", "End Preview"))
        self.take_picture_btn_.setText(_translate("main_window_", "Take Picture"))
        self.start_video_recording_btn_.setText(_translate("main_window_", "Start Video"))
        self.stop_video_recording_btn_.setText(_translate("main_window_", "Stop Video"))
        self.save_last_20_seconds_btn_.setText(_translate("main_window_", "Save last 20 seconds"))
        self.image_label_.setText(_translate("main_window_", "ImageLabel"))
        self.thumbnail_0.setText(_translate("main_window_", "ImageLabel"))
        self.thumbnail_1.setText(_translate("main_window_", "ImageLabel"))
        self.thumbnail_2.setText(_translate("main_window_", "ImageLabel"))
        self.thumbnail_3.setText(_translate("main_window_", "ImageLabel"))
        self.menutest.setTitle(_translate("main_window_", "Options"))


    def cv_image_to_qimage(self, cv_image):
        height, width, channel = cv_image.shape
        bytes_per_line = channel * width
        q_image = QtGui.QImage(cv_image.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)

        return q_image


    # Convert the cv image to a QImage and display it in the Graphics View using a label
    def cv_image_changed(self, cv_image):
        q_image = self.cv_image_to_qimage(cv_image)
        self.image_label_.setPixmap(QtGui.QPixmap.fromImage(q_image))

        # Scale the image label down to 30% of the qimage size
        self.image_label_.resize(int(q_image.width() * 0.3), int(q_image.height() * 0.3))
        self.image_label_.setScaledContents(True)
        self.image_label_.show()

    # Update the image queue thumbnail from the paths in the image queue. Note that the image queue size may be less than 4
    def update_image_queue_thumbnails(self, image_queue):
        thumbnail_list = [self.thumbnail_0, self.thumbnail_1, self.thumbnail_2, self.thumbnail_3]
        for i in range(len(image_queue)):
            q_image = QtGui.QImage(image_queue[i])
            thumbnail_list[i].setPixmap(QtGui.QPixmap.fromImage(q_image))

            # Scale the image label down to 30% of the qimage size
            thumbnail_list[i].resize(int(q_image.width() * 0.3), int(q_image.height() * 0.3))
            thumbnail_list[i].setScaledContents(True)
            thumbnail_list[i].show()

        # Clear the remaining thumbnails
        for i in range(len(image_queue), len(thumbnail_list)):
            thumbnail_list[i].clear()
        

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

    # Handle keyboard interrupt gracefully
    try:
        app.exec_()
    except KeyboardInterrupt:
        print("\nExiting...")
        camera_module.stop_timelapse_clicked()
        camera_module.stop_video_recording_clicked()
        camera_module.end_preview_clicked()
        
        sys.exit(0)

