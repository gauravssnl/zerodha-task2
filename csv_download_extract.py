# This file will download latest Bhav Copy CSV in Zip Format

import urllib.request
import datetime
import zipfile


def download_csv_zip_extract():
    # get today's date and use this to generate URL for downloading latest CSV in ZIP format
    today = str(datetime.date.today())
    year, month, day = today.split("-")
    date = "{}-{}-{}".format(day, month, year)
    print("Today's Date: ", date)

    base_url = "https://www.bseindia.com/download/BhavCopy/Equity/EQ{}{}{}_CSV.ZIP".format(
        int(day) - 1, month, year[2:])
    print("URL : ", base_url)
    filename = base_url.split("/")[-1]
    print("Filename : ", filename)
    file = urllib.request.urlretrieve(base_url, filename)
    print("File downloaded successfully.")
    zip_ref = zipfile.ZipFile(filename, 'r')
    zip_ref.extractall()
    zip_ref.close()
    print("Zip file extracted successfully.")


if __name__ == '__main__':
    download_csv_zip_extract()
