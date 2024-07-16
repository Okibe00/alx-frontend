from bs4 import BeautifulSoup


with open('33-styleguide.html') as fp:
	soup = BeautifulSoup(fp, features="lxml")
	print(soup.find("caption").text)

