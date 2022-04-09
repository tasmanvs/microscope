echo "Retrieving ui/main_window.ui from tsmith-mbp16"
scp -r tsmith@tsmith-mbp16:~/Desktop/main_window.ui ui/

echo "Creating skeleton.py from the ui file"
pyuic5 ui/main_window.ui > ui/skeleton.py