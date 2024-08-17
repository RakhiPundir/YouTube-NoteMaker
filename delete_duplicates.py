import os
from PIL import Image
import imagehash

def delete_duplicates(image_folder='frames'):
    images_hashes = {}
    for image_filename in os.listdir(image_folder):
        image_path = os.path.join(image_folder, image_filename)
        with Image.open(image_path) as img:
            img_hash = imagehash.phash(img)
            if img_hash in images_hashes:
                os.remove(image_path)
            else:
                images_hashes[img_hash] = image_filename

# delete_duplicates()
