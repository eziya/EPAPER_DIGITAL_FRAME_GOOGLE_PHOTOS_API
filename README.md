# EPAPER_DIGITAL_FRAME_GOOGLE_PHOTOS_API
Digital frame using Google Photos API <br>
Raspberry Pi + Python + E-Paper Display <br>

1) You must join Google API service and be authorized to use Google Photos Api to download photos from your album.
2) You must replace credential.json with yours.
3) I used 7.5" e-paper library from Waveshare wiki. (https://www.waveshare.com/wiki/7.5inch_e-Paper_HAT)
4) To use library from Waveshare, you may need to configure RPi properly (https://www.waveshare.com/wiki/Pioneer600#Libraries_Installation_for_RPi)
5) I used Imagemagick to convert my photos as bitmap images.
6) I compared image quality of monochrome files and 24bit bitmap files. 24bit bitmap file was better eventhough this e-paper supports only two colors (black & white)
7) Other models of e-paper supports 4 gray colors or 16 gray colors. I guess those models may provides better quality of images.

[![Digital frame example](https://i.ytimg.com/vi/VqnD_69p3YY/1.jpg?time=1539529346423)](https://youtu.be/VqnD_69p3YY)

Description later.
