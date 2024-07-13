from PIL import Image
from image_converter import image_converter

# Open the image file
def main():

    # Change this !!!
    # Image path
    image_path = 'W:/pass/google-1.png'

    with Image.open(image_path) as img:
        height, width = img.size
        pixels = img.load()

        # Change these !!!
        # Hidden message
        msg = 'secret'
        hidden_interval = 10

        binary_list = []
        for x in msg:
            binary_list.append(letterToBinary(x))
        
        # Pixel interval
        print(len(msg))
        interval_height = len(msg)
        interval_width = interval_height + hidden_interval

        print(binary_list)
        selected_pixels = [(x,y) for x in range(0, height, interval_height) for y in range(0, width, interval_width)]

# Letter to binary function
def letterToBinary(n):
    return ''.join(format(ord(n), 'b'))

if __name__ == '__main__':
    main()