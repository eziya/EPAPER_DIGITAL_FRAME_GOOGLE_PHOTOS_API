# EPAPER_DIGITAL_FRAME_GOOGLE_PHOTOS_API
Digital frame using Google Photos API <br>
Raspberry Pi + Google Photos API + E-Paper Display <br>

# Preparations <br>
1) Raspberry Pi <br>
2) Waveshare E-Paper (https://www.waveshare.com/wiki/7.5inch_e-Paper_HAT) <br>
3) Google API service credential file (credential.json)

# Steps <br>
1) Join Google API service and be authorized to use Google Photos API to download photos from your album.
2) You must replace credential.json with yours.
3) Configure your Raspberry Pi to use waveshare EPD library (https://www.waveshare.com/wiki/Pioneer600#Libraries_Installation_for_RPi)
4) If you use different models of E-Paper, Download an example and replace library files (epd7in5.py, epdif.py)
5) I used Imagemagick to convert my downloaded photos as bitmap images.
6) I compared image quality of monochrome and grayscale options. grayscale was better eventhough my e-paper supports only two colors (black & white). 
7) There're other models which supports 4 gray colors or 16 gray colors. I guess those models may provide better quality of images.

# Details
It's written in Korean but you may find helpful explanations and captures.
https://blog.naver.com/eziya76/221340156473
https://blog.naver.com/eziya76/221340903346
https://blog.naver.com/eziya76/221341923863
https://blog.naver.com/eziya76/221362430003

<a href="http://www.youtube.com/watch?feature=player_embedded&v=VqnD_69p3YY
" target="_blank"><img src="http://img.youtube.com/vi/VqnD_69p3YY/0.jpg" 
alt="E-Paper + Python + Google Photos API" width="240" height="180" border="10" /></a>
