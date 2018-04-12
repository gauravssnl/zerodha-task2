import urllib.request
import urllib
import datetime
import zipfile


def download_csv_zip_extract():
	# get today's date and use this to generate URL for downloading latest CSV in ZIP format
	today = str(datetime.date.today())
	year, month, day = today.split("-")
	date = "{}-{}-{}".format(day, month, year)
	print("Today's Date: ", date)

	base_url = "https://www.bseindia.com/download/BhavCopy/Equity/EQ{}{}{}_CSV.ZIP".format(day, month, year[2:])
	print(base_url)
	filename = base_url.split("/")[-1]
	print(filename)
	file = urllib.request.urlretrieve(base_url, filename)
	zip_ref = zipfile.ZipFile(filename, 'r')
	zip_ref.extractall()
	zip_ref.close()




if __name__ == '__main__':
	download_csv_zip_extract()
