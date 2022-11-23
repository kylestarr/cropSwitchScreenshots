# cropSwitchScreenshots
A Python script that crops all images in current working directory to remove Nintendo Switch UI from 4:3 games

## How to use

1. [Install Pillow (Python) via Pip](https://pillow.readthedocs.io/en/stable/installation.html)
```
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
```
2. Download cropSwitchScreenshots.py
3. Place cropSwitchScreenshots.py in the directory with the images you wish to crop
4. Open Terminal
5. In Terminal, `cd` into the directory with the images you wish to crop. On macOS, you can drag and drop the directory (folder) into the Terminal window to get the exact path.
6. In Terminal un `python3 cropSwitchScreenshots.py`

In the original directory of images, you will find a new directory named **croppedImages**. This new directory contains cropped copies of the original images without the added Switch UI.
