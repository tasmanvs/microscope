class CameraModule(object):
    condition = 'New'

    def __init__(self):
        pass
        # self.brand = brand
        # self.model = model
        # self.color = color

    def take_picture(self, file_name):
        self.condition = 'Used'

    def print(self):
        print("test")

    def start_preview_clicked(self):
        print("Start Preview Clicked")
        