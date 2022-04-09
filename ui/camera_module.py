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

    # Initialize a circular buffer stream
    circular_stream_ = picamera.PiCameraCircularIO(camera_, seconds=20)

    def __init__(self):
        super().__init__()
        self.status_ = "initialized"
        self.print_status()
        # Make an images directory if it doesn't exist
        if not os.path.exists("images"):
            os.makedirs("images")

        # Start the circular stream recording
        self.camera_.start_recording(self.circular_stream_, format='h264')
        
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

    def start_video_recording_clicked(self):
        self.status_ = "Start Video Recording Clicked"
        self.print_status()
        # start recording on another port than the circular buffer
        self.camera_.start_recording("images/" + self.file_name_ + ".h264", splitter_port=2)
        self.status_ = "Started Video Record with " + self.file_name_
        self.print_status()

    def stop_video_recording_clicked(self):
        self.status_ = "Stop Video Recording Clicked"
        self.print_status()
        self.camera_.stop_recording()
        self.status_ = "Stopped Video Record. Saved file to " + self.file_name_
        self.print_status()
        #Convert the .h264 file to .mp4 on a separate thread
        self.status_ = "Converting file \"images/" + self.file_name_ + ".h264\" to \"images/" + self.file_name_ + ".mp4\""
        self.print_status()
        os.system("MP4Box -add images/" + self.file_name_ + ".h264 images/" + self.file_name_ + ".mp4")
        self.status_ = "Converted file \"images/" + self.file_name_ + ".h264\" to \"images/" + self.file_name_ + ".mp4\""
        self.print_status()
        # Delete the .h264 file
        self.status_ = "Deleting file \"images/" + self.file_name_ + ".h264\""
        self.print_status()
        os.system("rm images/" + self.file_name_ + ".h264")
        self.status_ = "Deleted file \"images/" + self.file_name_ + ".h264\""
        self.print_status()
        

    def save_last_20_seconds_clicked(self):
        # Save the circular buffer to a file
        self.status_ = "Saving circular buffer to " + self.file_name_
        self.print_status()
        self.circular_stream_.copy_to("images/" + self.file_name_ + ".h264")
        self.status_ = "Saved circular buffer to " + self.file_name_
        self.print_status()

    
    def file_name_changed(self, text):
        self.file_name_ = text
        self.status_ = "Set file name to " + self.file_name_
        self.print_status()

    def get_status_text(self) -> str:
        return self.status_