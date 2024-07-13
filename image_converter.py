from PIL import Image

# Change this !!!
path = 'W:/pass/twitter.webp'
output = 'W:/pass/twitter.png'

def image_converter(path, output):
    with Image.open(path) as img:
        img.save(output)