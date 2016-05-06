import urllib2
from urllib import urlretrieve
import urlparse
from bs4 import BeautifulSoup
import os


def get_images():
	url = "http://en.wikipedia.org/wiki/Main_Page"
	soup = BeautifulSoup(urllib2.urlopen(url))
	imglist=soup.select('a.image > 	img')
	for img in imglist:
		img_url = urlparse.urljoin(url, img['src'])
    	file_name = img['src'].split('/')[-1]
    	urlretrieve(img_url, file_name)

def get_links():
	fish_url='http://http://en.wikipedia.org/wiki/Main_Page/'
	page= urllib2.urlopen(fish_url)
	html_doc = page.read()
	soup= BeautifulSoup(html_doc)
	for link in soup.find_all('a'):
		links=link.get('href')
		links=str(links)
		print ("new link",	links)
		
def main():
	print "1. All the data in the webpage"
	print "2. All the links in the webpage"
	print "3. All the images in the webpage"
	choice= input('Enter your choice: ')
	if(choice==1):
		fish_url='http://http://en.wikipedia.org/wiki/Main_Page/'
		page= urllib2.urlopen(fish_url)
		html_doc = page.read()
		soup= BeautifulSoup(html_doc)
		print(soup.prettify())
	if(choice==2):
		get_links()
	if (choice==3):
		get_images()	
			
main()