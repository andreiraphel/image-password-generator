from PIL import Image

# Open the image file
def main():
    with Image.open('W:/pass/google-1.png') as img:
        height, width = img.size
        pixels = img.load()

        # Change these !!!
        # Hidden message
        msg = 'secret'
        hidden_interval = 10

        binary_list = []
        for x in msg:
            binary_list.append(stringToBinary(x))
        
        # Pixel interval
        print(len(msg))
        interval_height = len(msg)
        interval_width = interval_height + hidden_interval

        print(binary_list)
        selected_pixels = [(x,y) for x in range(0, height, interval_height) for y in range(0, width, interval_width)]

def stringToBinary(n):
    return ''.join(format(ord(n), 'b'))

if __name__ == '__main__':
    main()