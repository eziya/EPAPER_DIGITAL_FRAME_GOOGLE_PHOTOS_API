import os, random, time
import epd7in5
import Image
import ImageDraw
import ImageFont
import imagedata

EPD_WIDTH = 640
EPD_HEIGHT = 384

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    epd = epd7in5.EPD()
    epd.init()

    # select a random image file
    filename = random.choice(os.listdir('./images'))
    #filename = 'test3.bmp'

    image = Image.open('./images/' + filename)
    epd.display_frame(epd.get_frame_buffer(image))
    #epd.display_frame(imagedata.MONOCOLOR_BITMAP)

if __name__ == "__main__":
    main()
