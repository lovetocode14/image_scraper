import urllib.request
from PIL import Image

img = urllib.request.urlretrieve('https://icdn.digitaltrends.com/image/digitaltrends/iphone-6-plus-studio-back-plus.jpg',
                                 "file")

imgRetrieved = Image.open("file")
imgRetrieved.show()
