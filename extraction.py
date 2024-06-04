import os

def get_features(extractor, imagePath, maskPath):
    return extractor.execute(imagePath, maskPath)

def mask_path(img, roi):
    dose = None
    if '40dose' in img:
        dose = '40dose'
    elif '60dose' in img:
        dose = '60dose'
    else:
        dose = '100dose'
        
    dir = os.getcwd() + '/Axial Masks/' + dose
    # special case, img not formed properly
    if img == '2DLIR_40dose_0-625mm.nii':
        dir = os.getcwd() + '/Axial Masks/Special_2DLIR40dose_0-625mm'
    
    roi_str = '313-' + str(roi)
    if roi == 0:
        roi_str = '313'

    slice = None
    if '0-625mm' in img:
        slice = '0-625mm'
    elif '1-25mm' in img:
        slice = '1-25mm'
    else:
        slice = '2-5mm'
        
    return dir + '/' + roi_str + '_' + slice + '.nii'