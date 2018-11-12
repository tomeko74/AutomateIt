import bs4

myfile = open('python.html')
soup = bs4.BeautifulSoup(myfile, "html.parser")

# Making the soup
print("\nBeautifulSoup Object:", type(soup))

# Find Elements By tags
print(soup.find_all('a'))
print(soup.find_all('strong'))

# Find Elements By id
print(soup.find('div', {"id":"inventor"}))
print(soup.select('#inventor'))

# Find Elements by css
print(soup.select('.wow')[0].text) # By css
print(soup.select('.wow')) # By css
print("\n\n")

print("Facebook URL:", soup.find_all('a')[0]['href'])
print("nazwa linku:", soup.find_all('a')[0].text)
print("Facebook URL:", soup.find_all('a'))
print("Inventor:", soup.find('div', {"id":"inventor"}).text)
print("Span content:", soup.select('span')[0].getText())




