import os
import re
import urllib.request
from bs4 import BeautifulSoup

# Download parameters
image_type = "Project"
movie = "Godfather"
url = "https://www.google.com/search?q="+movie+"&source=lnms&tbm=isch"

# Create Soup Object and find images from the search
header = {'User-Agent': 'Mozilla/5.0'}
soup = BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url, headers=header)), "html.parser")
images = [a['src'] for a in soup.find_all("img", {"src": re.compile("gstatic.com")})][:5]
for img in images:
    print("Image Source:", img)

# Go through all the urls and download images
for img in images:
    raw_img = urllib.request.urlopen(img).read()
    cntr = len([i for i in os.listdir(".") if image_type in i]) + 1 # jeżeli już takie numerki w nazwie są to dociągaj jako kolejne
    f = open(image_type + "_"+ str(cntr)+".jpg", 'wb') # zapisanie obrazka
    f.write(raw_img)
    f.close()
