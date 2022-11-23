#! python3
# copySwitchScreenshots.py - A Python script that crops all images in  
# current working directory to remove Nintendo Switch UI from 4:3 games

import os
from PIL import Image

os.makedirs('croppedImages', exist_ok=True)
# Loop over all files in the working directory.
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')):
        continue    #skip non-image files

    im = Image.open(filename)

    # Crop the image
    print('Cropping %s...' % (filename))
    croppedIm = im.crop((201, 0, 1078, 684))

    # Save changes.
    croppedIm.save(os.path.join('croppedImages', filename))
