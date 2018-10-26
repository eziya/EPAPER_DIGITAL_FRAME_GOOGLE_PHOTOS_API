#!/usr/bin/python
#-*- encoding: utf8 -*-
from __future__ import print_function
import os, random, time, sys, datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import wget
import epd7in5
import Image
import ImageDraw

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/photoslibrary",
          "https://www.googleapis.com/auth/photoslibrary.readonly",
          "https://www.googleapis.com/auth/photoslibrary.readonly.appcreateddata"]

def main():

    #To fix the path issue when script runs by crontab
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    #create directory for download
    print("Check image directory...")

    if not os.path.exists("images"):
        os.makedirs("images")

    #delete 7 days old images
    print("Delete 7 days old images...")

    now = time.time()

    for filename in os.listdir('./images'):
        file_full_path = os.path.join('.', filename)
        if os.path.isfile(file_full_path):
            if os.stat(file_full_path).st_mtime < now - (7 * 86400):
                os.remove(file_full_path)

    #OAuth2 authentication process
    print("OAuth2 authentication process...")

    store = file.Storage("token.json")
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets("credentials.json", SCOPES)
        creds = tools.run_flow(flow, store)
    service = build("photoslibrary", "v1", http=creds.authorize(Http()))

    #Search image files
    print("Search image files...")
    dtToday = datetime.date.today()
    dt7DaysAgo = dtToday - datetime.timedelta(days=7)
    nextPageToken = ""

    while True:

        results = service.mediaItems().search(
            body={
                "albumId": "[YOUR ALBUM ID HERE]",
                "pageToken": nextPageToken,
                # "filters":{
                #     "dateFilter":{
                #         "ranges":[
                #             {"startDate":{"year":dt7DaysAgo.year,"month":dt7DaysAgo.month,"day":dt7DaysAgo.day},
                #              "endDate":{"year":dtToday.year,"month":dtToday.month,"day":dtToday.day}
                #              }
                #         ]
                #     },
                #     "mediaTypeFilter":{
                #         "mediaTypes":["PHOTO"]
                #     }
                # }
            }
        ).execute()

        items = results.get("mediaItems", [])
        if not items:
            print("No media found.")
            quit()

        # Download & conver image files
        print("Dowload & Convert image files...")
        for item in items:
            filename = item["filename"].encode("utf8")
            baseUrl = item["baseUrl"].encode("utf8")
            bmpname = filename.split('.')[0] + ".bmp"

            print("\nfilename:{0}, {1}".format(filename, baseUrl))

            # check duplication & download
            file_full_path = os.path.join("images", bmpname)
            if not os.path.isfile(file_full_path):
                wget.download(baseUrl, "./images/" + filename)
                command = "convert images/{0} -background black -gravity center -colorspace Gray -separate -average -resize x384 -extent 640x384 images/{1}".format(
                    filename, bmpname)

                os.system(command)

        #check next page, if not break
        nextPageToken = results.get("nextPageToken");

        if nextPageToken is not None and nextPageToken != "":
            print("nextPageToken: " + nextPageToken)
        else:
            print("Final page")
            break

    #delete all jpg files
    print("Deleting all jpg files...")
    command = "rm -rf ./images/*.jpg"
    os.system(command)
    command = "rm -rf ./images/*.JPG"
    os.system(command)

    #display random image
    epd = epd7in5.EPD()
    epd.init()

    filename = random.choice(os.listdir('./images'))

    image = Image.open('./images/' + filename)
    epd.display_frame(epd.get_frame_buffer(image))

if __name__ == "__main__":
    main()
