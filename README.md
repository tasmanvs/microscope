# microscope

Run the main application using
python3 ui/main_window.py

Use the dev raspberry pi to update the skeleton file using the update_skeleton.sh script
ssh pi@192.168.86.61 'bash -s' <  scripts/update_skeleton.sh

Send this code to the pi running the microscope using
rsync -r ui pi@192.168.86.29:~

Copy images back to computer using
rsync -r pi@192.168.86.29:~/images ~/Pictures/Microscope

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
