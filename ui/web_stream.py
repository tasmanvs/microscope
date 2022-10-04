import io
import picamera
import logging
import socketserver
from threading import Condition
from http import server

from threading import Thread

import subprocess



PAGE="""\
<html>
<head>
</head>
<body>
<!-- Display the img stream full screen -->
<img src="stream.mjpg" width="100%" height="100%" />
</body>
</html>
"""

class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)

class StreamingHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/index.html')
            self.end_headers()
        elif self.path == '/index.html':
            content = PAGE.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
        elif self.path == '/stream.mjpg':
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()
            try:
                while True:
                    with output.condition:
                        output.condition.wait()
                        frame = output.frame
                    self.wfile.write(b'--FRAME\r\n')
                    self.send_header('Content-Type', 'image/jpeg')
                    self.send_header('Content-Length', len(frame))
                    self.end_headers()
                    self.wfile.write(frame)
                    self.wfile.write(b'\r\n')
            except Exception as e:
                logging.warning(
                    'Removed streaming client %s: %s',
                    self.client_address, str(e))
        else:
            self.send_error(404)
            self.end_headers()

class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True


# Thread for running the camera web stream
class CameraWebStream(Thread):
    def __init__(self, camera):
        super().__init__()
        self.camera_ = camera
        self.stop_ = False

    def run(self):
        global output
        output = StreamingOutput()

        self.camera_.start_recording(output, format='mjpeg', splitter_port=3)
        try:
            address = ('', 8000)
            server = StreamingServer(address, StreamingHandler)
            # Print the url of the stream
            # If you are running this on the pi, you can access the stream at
            # http://<pi ip address>:8000

            pi_ip_address = subprocess.check_output("hostname -I | cut -d' ' -f1", shell=True).decode("utf-8")
            # Remove the newline character
            pi_ip_address = pi_ip_address[:-1]

            print("Stream available at http://" + pi_ip_address + ":8000")
            server.serve_forever()
        finally:
            self.camera_.stop_recording(splitter_port=3)
        




# class CameraWebStream(object):
#     def __init__(self, camera):
#         self.camera = camera
#         self.output = StreamingOutput()

#     def start(self):
#         self.camera.start_recording(self.output, format='mjpeg', splitter_port=3)
#         try:
#             address = ('', 8000)
#             server = StreamingServer(address, StreamingHandler)

#             # Print the url of the stream
#             # If you are running this on the pi, you can access the stream at
#             # http://<pi ip address>:8000

#             pi_ip_address = subprocess.check_output("hostname -I | cut -d' ' -f1", shell=True).decode("utf-8")
#             # Remove the newline character
#             pi_ip_address = pi_ip_address[:-1]

#             print("Stream available at http://" + pi_ip_address + ":8000")

#             server.serve_forever()

#         finally:
#             camera.stop_recording(splitter_port=3)



# camera_web_stream = CameraWebStream()
# camera_web_stream.start()


# with picamera.PiCamera(resolution='1920x1088', framerate=24) as camera:
#     output = StreamingOutput()
#     camera.start_recording(output, format='mjpeg', splitter_port=3)
    
#     try:
#         address = ('', 8000)
#         server = StreamingServer(address, StreamingHandler)

#         # Print the url of the stream
#         # If you are running this on the pi, you can access the stream at
#         # http://<pi ip address>:8000

#         pi_ip_address = subprocess.check_output("hostname -I | cut -d' ' -f1", shell=True).decode("utf-8")
#         # Remove the newline character
#         pi_ip_address = pi_ip_address[:-1]

#         print("Stream available at http://" + pi_ip_address + ":8000")

#         server.serve_forever()

#     finally:
#         camera.stop_recording(splitter_port=3)