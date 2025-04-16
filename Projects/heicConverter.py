#pip --install    

from PIL import Image
from pillow_heif import register_heif_opener
import os
import sys
def main(argv):
    heicFolder = argv[1]
    newpath = heicFolder + "/pngOutput"
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    
    outputFolder = newpath + "/"
    
    register_heif_opener()
    heicFiles = [f for f in os.listdir(heicFolder) if f.endswith(".heic")]

    for photo in heicFiles:
        register_heif_opener()
        tempImg = Image.open(heicFolder + "/" + photo)
        tempfile = photo.replace(".heic", ".png")
        #pngPhoto = photo.replace('.heic', '.png')
        tempImg.save(heicFolder + "/pngOutput/" + tempfile, format="PNG")
    print("Converted all heic Photos in the file to png")
main(sys.argv)