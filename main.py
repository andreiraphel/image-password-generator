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
        interval_height = len(msg)
        interval_width = interval_height + hidden_interval

        selected_pixels = [(x,y) for x in range(0, height, interval_height) for y in range(0, width, interval_width)]

        string_pass = ""
        for x in selected_pixels:
            color = pixels[x][2]
            if color not in range(32, 126):
                string_pass += chr(97)
            else:
                string_pass += chr(color)

        password = string_pass[1:65]
        print(password)
    
                
        
# Letter to binary function
def letterToBinary(n):
    return ''.join(format(ord(n), 'b'))

if __name__ == '__main__':
    main()