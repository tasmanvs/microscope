from PyQt5.QtCore import QObject, pyqtSignal

import os
import subprocess

import picamera
from picamera.array import PiRGBArray
import time

# Import things for timelapse thread
from threading import Thread

# For capturing to opencv
import numpy as np
import cv2

# This class is used to control the camera module.
# It is used to take pictures and to record videos.
# It also has a signal that is emitted when we want to update the UI.
# Note - Everything is saved as 1920x1080.

# Thread for running timelapse
class TimelapseThread(Thread):
    def __init__(self, camera, delay_seconds, file_name):
        super().__init__()
        self.camera_ = camera
        self.timelapse_delay_seconds_ = delay_seconds
        self.file_name_ = file_name
        self.stop_ = False
        self.counter_ = 0

    def run(self):
        while not self.stop_:
            target_directory = "images/" + self.file_name_
            if not os.path.exists(target_directory):
                os.makedirs(target_directory)

            # We actually want to append 00001, 00002, 00003, etc.
            file_name = target_directory + "/" + self.file_name_ + str(self.counter_).zfill(5) + ".jpg"

            print("Timelapse Thread: Taking picture at location " + file_name)
            self.camera_.capture(file_name)
            self.counter_ += 1
            time.sleep(self.timelapse_delay_seconds_)

        
    def stop(self):
        self.stop_ = True

class CameraModule(QObject):
    # The latest status of the gui
    status_ = "initialized"

    # The camera object that we use to interface with the hardware
    camera_ = picamera.PiCamera()

    # Signal to update the label in the GUI
    status_changed_ = pyqtSignal(str)

    # Signal to update the QGraphicsView in the GUI
    cv_image_changed_ = pyqtSignal(np.ndarray)

    # Counter to keep track of the number of pictures taken
    counter_ = 0

    circular_stream_length_seconds_ = 20

    # Initialize a circular buffer stream
    circular_stream_ = picamera.PiCameraCircularIO(camera_, seconds=circular_stream_length_seconds_)

    target_frame_rate_ = 25

    timelapse_delay_seconds_ = 5
    taking_timelapse_ = False

    file_name_ = "file_name"
    resolution_ = (1920, 1088)

    # Create empty cv image with the correct resolution
    cv_image_ = np.empty((resolution_[1], resolution_[0], 3), dtype=np.uint8)

    def __init__(self):
        super().__init__()
        self.update_status("initialized")
        # Make an images directory if it doesn't exist
        if not os.path.exists("images"):
            os.makedirs("images")

        # Set the framerate to a fixed value of 25
        self.camera_.framerate = self.target_frame_rate_

        # Set camera resolution to 1920x1080
        self.camera_.resolution = self.resolution_

        # Start the circular stream recording. Note - port 2 is used for video recording
        self.camera_.start_recording(self.circular_stream_, format='h264')


    # Define the destructor
    def __del__(self):
        print("Destructor called")
        print("Stopping the camera")
        self.camera_.stop_recording()
        print("Closing the camera")
        self.camera_.close()
        
    def update_status(self, text=None):
        if text is not None:
            self.status_ = text
            # Emit the signal to update the label in the GUI
            print(self.status_)
            self.status_changed_.emit(self.status_)            

    def start_preview_clicked(self):
        self.update_status("Start Preview Clicked")

        if (self.camera_.closed):
            self.camera_ = picamera.PiCamera()

        self.camera_.start_preview()
        
    def end_preview_clicked(self):
        self.update_status("End Preview Clicked")
        self.camera_.stop_preview()

    # Capture a picture to an opencv object
    def opencv_capture_clicked(self):
        self.update_status("Capturing picture to opencv")
        # image = np.empty((self.camera_.resolution[1], self.camera_.resolution[0], 3), dtype=np.uint8)
        # self.camera_.capture(image, format='bgr')
        # image = image.reshape((self.camera_.resolution[0], self.camera_.resolution[1], 3))


        rawCapture = PiRGBArray(self.camera_)
        # grab an image from the camera
        self.camera_.capture(rawCapture, format="bgr")
        image = rawCapture.array
        # display the image on screen and wait for a keypress
        # cv2.imshow("Image", image)
        # cv2.waitKey(0)

        # # Save the cv image to the desktop
        # cv2.imwrite("/home/pi/Desktop/cvimage.jpg", image)
        
        self.cv_image_ = image
        self.cv_image_changed_.emit(self.cv_image_)

    def take_picture_clicked(self):
        self.update_status("Take Picture Clicked")
        # Increment the counter and take a picture with the filename
        self.counter_ += 1
        filepath = "images/" + self.file_name_ + str(self.counter_) + ".jpg"
        self.camera_.capture(filepath)
        self.update_status("Picture Taken at " + filepath)

    def start_video_recording_clicked(self):
        suffix = "_video"
        self.update_status("Start Video Recording Clicked")
        # start recording on another port than the circular buffer
        self.camera_.start_recording("images/" + self.file_name_ + suffix + ".h264", splitter_port=2)
        self.update_status("Started Video Record with " + self.file_name_ + suffix)

    def stop_video_recording_clicked(self):
        suffix = "_video"
        self.update_status("Stop Video Recording Clicked")
        self.camera_.stop_recording()
        self.update_status("Stopped Video Record. Saved file to " + self.file_name_ + suffix)

        #Convert the .h264 file to .mp4
        self.convert_to_mp4(self.file_name_ + suffix)


    def record_circular_buffer_clicked(self):
        suffix = "_circular_buffer_" + str(self.circular_stream_length_seconds_) + "s"

        # Save the circular buffer to a file
        self.update_status("Saving circular buffer to " + self.file_name_ + suffix + ".h264")
        self.circular_stream_.copy_to("images/" + self.file_name_ + suffix + ".h264", seconds=self.circular_stream_length_seconds_)
        self.update_status("Saved circular buffer to " + self.file_name_ + suffix + ".h264")
        # Convert the .h264 file to .mp4
        self.convert_to_mp4(self.file_name_ + suffix)
        

    # This function converts the .h264 file to .mp4 using a subprocess so we don't block the main thread
    def convert_to_mp4(self, file_name):
        self.update_status("Converting file \"images/" + file_name + ".h264\" to \"images/" + file_name + ".mp4\"")
        # Use subprocess to convert the .h264 file to .mp4
        full_file_name = "images/" + file_name + ".h264"
        cmd = "MP4Box -add " + full_file_name + " -fps " + str(self.target_frame_rate_) + " -new " + "images/" + file_name + ".mp4"
        cmd += "&& rm " + full_file_name
        subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    def file_name_changed(self, text):
        self.file_name_ = text
        self.update_status("Set file name to " + self.file_name_)

    def get_status_text(self) -> str:
        return self.status_

    # Functions for timelapse
    def start_timelapse_clicked(self):
        self.update_status("Start Timelapse Clicked")
        self.taking_timelapse_ = True
        self.timelapse_thread_ = TimelapseThread(self.camera_, self.timelapse_delay_seconds_, self.file_name_)
        self.timelapse_thread_.start()
        self.update_status("Started Timelapse thread with " + self.file_name_)

    def stop_timelapse_clicked(self):
        self.update_status("Stop Timelapse Clicked")
        self.taking_timelapse_ = False
        self.timelapse_thread_.stop()
        self.update_status("Stopped Timelapse thread with " + self.file_name_)
        
    # handle timelapse spinbox delay changed
    def timelapse_delay_changed(self, value):
        self.update_status("Timelapse Delay Changed to " + str(value))
        self.timelapse_delay_seconds_ = value

