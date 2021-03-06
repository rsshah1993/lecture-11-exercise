from bs4 import BeautifulSoup

f = open("hello.html")
html = f.read()
soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())

all_list_items = soup.find_all('li')
all_divs = soup.find_all("div")
all_goodbye_elements = soup.find_all(class_ = 'goodbye')
all_french_list_items = soup.find_all('li', class_ = "french")
all_hello_elements = soup.find_all(id = "hello-list")
all_goodbye_elements = soup.find_all(id = "goodbye-list")

# print('list items:', all_list_items)
# print('------')
# print('divs:', all_divs)
# print('------')
# print('goodbye elements:', all_goodbye_elements)
# print('------')
# print('french stuff:', all_french_list_items)
# print('------')
# print('hello id elements:', all_hello_elements)
# print('------')
#
#
#
# print(type(all_list_items[0]))
# print('------')
#
#
#
# for li in all_list_items:
#   print(li.string)
# print('------')


for child in all_hello_elements[0].children:
  print(child.string)
print('------')



print('List items within the hello tag')
hello_list_items = all_hello_elements[0].find_all('li')
print (hello_list_items)
print('------')



img_tag = soup.find('img')
print('The img source:')
print(img_tag['src'])
print('------')

print('list items within the goodbye tag')
goodbye_list_items = all_goodbye_elements[0].find_all('li')
for items in goodbye_list_items:
    print(items.string)
print('------')


print('The img width:')
print(img_tag['width'])

print('------')


find_a_items = soup.find_all('a')
print(find_a_items[0]['href'])
