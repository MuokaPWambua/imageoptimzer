import os
import io
from PIL import Image
from werkzeug.utils import secure_filename
from flask import request

# path to image upload
upload_path = os.path.abspath('uploads')


def image_extention(filename):
# to check if image extenstion type
    exts = {'jpg', 'jpeg', 'png', 'ico', 'gif'}
    ext = filename.rsplit('.', 1)[1].lower()

    if ext in exts:
        print (filename)
        return True
    return False    

def optimizer(image, size, extend_name):
    """ this function takes image file for resizing
    according to the given size and a name to extend to the original filename"""
    try:
        
        filename = secure_filename(image.filename)
        ext = filename.split('.')[-1]
        name = filename.split('.')[0]

        filepath = f'{os.path.join(path, name)}-{extend_name}.{ext}'
        
        #opening image for optimizing

        img = Image.open(image)
        img.thumbnail(size, Image.LANCZOS)
        img.save(filepath, optimize=True, quality=95)

        #  url to save to the database
        urlpath = str(request.url_root)[:-1] + filepath

        print (urlpath)

        return urlpath

    except Execption as e:
        print(e)
        

def optimized():
    # return an array of the image urlpaths in diffent sizes 
    thumb = 30, 30
    small = 320, 320
    medium = 768, 768
    large = 990, 990
    xlarge = 1080, 1080

    try:
        thumbnail = optimizer(image, thumb, 'thumbnail')
        small_image = optimizer(image, small, '320px')
        medium_image = optimizer(image, medium, '640px')
        large_image = optimizer(image, large, '768px')
        xlarge_image = optimizer(image, xlarge, '1080px')
        print ('resized and saved')

        return thumbnail, small_image, medium_image, large_image, xlarge_image
    except Exception as e:
        print(e)


def save(file):
    # saves file after verifying its an image file
    if not file:
        print("a file is required")
        return
    if image_extention(file.filename):
        return optimized(file)
    return    
