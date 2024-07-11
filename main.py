from PIL import Image

im = Image.open('W:/pass/google-1.png')

print(im.format, im.size, im.mode)

im.show()