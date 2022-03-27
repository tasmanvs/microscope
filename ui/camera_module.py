class CameraModule(object):
    condition = 'New'
    status_ = "initialized"

    def __init__(self):
        pass
        # self.brand = brand
        # self.model = model
        # self.color = color

    def take_picture(self, file_name):
        self.condition = 'Used'

    def print_status(self):
        print(self.status_)

    def start_preview_clicked(self):
        self.status_ = "Start Preview Clicked"
        self.print_status()
        
    def end_preview_clicked(self):
        self.status_ = "End Preview Clicked"
        self.print_status()

    def take_picture_clicked(self):
        self.status_ = "Take Picture Clicked"
        self.print_status()
    
    def file_name_changed(self, text):
        self.file_name_ = text
        self.status_ = "Set file name to " + self.file_name_
        self.print_status()

    def get_status_text(self) -> str:
        return self.status_