# microscope

Run the main application using
python3 ui/main_window.py

Copy the file from the macos laptop to the dev raspberry pi
scp ~/Desktop/main_window.ui daisy@192.168.86.150:~/coding/microscope/ui/

Generate a python skeleton file from the qt .ui file using
pyuic5 ui/main_window.ui > ui/skeleton.py

Send this code to the pi running the microscope using
rsync -r ui pi@192.168.86.23:~

Copy images back to computer using

TODO:
- Remove Start/Stop preview buttons. Just start the preview automatically.
- Get file streaming working
- Create a Jira project?
- Add counter for how long we have been recording
- Disable buttons depending on internal state
- Gracefully handle exceptions
- For timelapse, write to a video instead of a series of images

DONE:
- Timelapse
- Wire up camera library
- Get video working
- Get status to update
