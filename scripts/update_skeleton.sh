echo "Copying the ui file from the mac"
scp tasman@tasmans-mbp:~/Documents/microscope/ui/main_window.ui .

echo "Creating skeleton.py from the ui file"
python -m PyQt5.uic.pyuic main_window.ui > skeleton.py

echo "Sending the skeleton.py back to the mac"
scp skeleton.py tasman@tasmans-mbp:~/Documents/microscope/ui/