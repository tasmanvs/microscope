from PyQt5.QtCore import QObject, pyqtSignal

import os

import picamera


class CameraModule(QObject):
    # The latest status of the gui
    status_ = "initialized"

    # The camera object that we use to interface with the hardware
    camera_ = picamera.PiCamera()

    # Signal to update the label in the GUI
    status_changed_ = pyqtSignal(str)

    # Counter to keep track of the number of pictures taken
    counter_ = 0

    def __init__(self):
        super().__init__()
        self.status_ = "initialized"
        self.print_status()
        # Make an images directory if it doesn't exist
        if not os.path.exists("images"):
            os.makedirs("images")
        
    def print_status(self):
        print(self.status_)
        # Emit the signal to update the label in the GUI
        self.status_changed_.emit(self.status_)

    def start_preview_clicked(self):
        self.status_ = "Start Preview Clicked"
        self.print_status()

        if (self.camera_.closed):
            self.camera_ = picamera.PiCamera()

        self.camera_.start_preview()
        
    def end_preview_clicked(self):
        self.status_ = "End Preview Clicked"
        self.print_status()
        self.camera_.stop_preview()

    def take_picture_clicked(self):
        self.status_ = "Take Picture Clicked"
        self.print_status()
        # Increment the counter and take a picture with the filename
        self.counter_ += 1
        filepath = "images/" + self.file_name_ + str(self.counter_) + ".jpg"
        self.camera_.capture(filepath)
        self.status_ = "Picture Taken at " + filepath
        self.print_status()

    
    def file_name_changed(self, text):
        self.file_name_ = text
        self.status_ = "Set file name to " + self.file_name_
        self.print_status()

    def get_status_text(self) -> str:
        return self.status_