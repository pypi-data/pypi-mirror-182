import SimpleITK as sitk

class NiftiReader():

    def __init__(self, path):
        self.sitk= sitk.ReadImage(path)

    def get_array(self):
        array= sitk.GetArrayFromImage(self.sitk)
        return array 

    def get_origin(self):
        origin= self.sitk.GetOrigin()
        return origin 

    def get_spacing(self):
        spacing= self.sitk.GetSpacing()
        return spacing 

    def get_size(self):
        size= self.sitk.GetSize()
        return size

    def get_direction(self):
        direction= self.sitk.GetDirection()
        return direction

    def save_image(self, dest_path: str, compressed: bool = False):
        sitk.WriteImage(self.sitk, dest_path, compressed)
    
