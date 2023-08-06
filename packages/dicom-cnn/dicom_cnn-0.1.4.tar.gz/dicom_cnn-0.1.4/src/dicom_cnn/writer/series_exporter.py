from __future__ import annotations
import os
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dicom_cnn.series.series import Series

import SimpleITK as sitk
import numpy as np

class SeriesExporter():

    series: Series = None

    def __init__(self, series: Series):
        self.series = series

    def get_array(self) -> np.ndarray:
        return self.series.get_numpy_array()

    def get_sitk_image(self,nifti_orientation = False) -> sitk.Image:
        array = self.get_array()
        dicom_direction = self.series.get_series_direction()
        origin = self.series.get_image_origin(nifti_origin=True)

        if nifti_orientation == True:
            array = np.flip(array, axis = 0) ## jambes en haut tête en bas
            array = np.flip(array, axis = 1) ## sur le ventre

        sitk_img = sitk.GetImageFromArray(array)
        pixel_spacing = self.series.get_pixel_spacing()
        sitk_img.SetSpacing(pixel_spacing)

        if nifti_orientation == True:

            nifti_origin = list(origin)
            nifti_direction = list(dicom_direction)

            normal = [nifti_direction[1]*nifti_direction[5] - nifti_direction[2]*nifti_direction[4],
                        nifti_direction[2]*nifti_direction[3] - nifti_direction[0]*nifti_direction[5],
                        nifti_direction[0]*nifti_direction[4] - nifti_direction[1]*nifti_direction[3],]

            for i in range(3):
                nifti_direction[i] = nifti_direction[i]*pixel_spacing[0]
                nifti_direction[i+3] = -nifti_direction[i+3]*pixel_spacing[1]
                nifti_direction[i+6] = normal[i]*pixel_spacing[2]

            nifti_origin[1] = array.shape[1]*pixel_spacing[1] + (nifti_origin[1]-pixel_spacing[1])
            sitk_img.SetDirection(tuple(nifti_direction))
            sitk_img.SetOrigin(tuple(nifti_origin))
            
        else:
            sitk_img.SetDirection(dicom_direction)
            sitk_img.SetOrigin(origin)
        
        sitk_img = sitk.Cast(sitk_img, sitk.sitkInt16)
        return sitk_img

    def write_image_to_nifti(self, file_path, filename, compress = False, nifti_orientation = False) -> None:
        extension = '.nii'
        if(compress): extension = '.nii.gz'
        path = os.path.join(file_path, filename + extension)
        image_sitk = self.get_sitk_image(nifti_orientation)
        sitk.WriteImage(image_sitk, path)
