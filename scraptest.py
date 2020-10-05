from bs4 import BeautifulSoup as bs
import requests

link = 'https://www.amazon.in/OnePlus-Mirror-Black-128GB-Storage/product-reviews/B07DJHV6VZ/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'

page = requests.get(link)

print(page)
print(page.content)

soup = bs(page.content,'html.parser')
print(soup.prettify())

names = soup.find_all('span',class_='a-profile-name')
print(names)
cust_name = []
for i in range(0,len(names)):
    cust_name.append(names[i].get_text())
cust_name

cust_name.pop(0)
print(cust_name.pop(0))

cust_name.pop(0)
print(cust_name.pop(0))

print(cust_name)

title = soup.find_all('a',class_='review-title-content')
print(title)

review_title = []
for i in range (0,len(title)):
    review_title.append(title[i].get_text())
review_title

review_title[:] = [titles.lstrip('\n') for titles in review_title]
print(review_title)

rating = soup.find_all('i',class_='review-rating')
print(rating)

rate = []
for i in range(0,len(rating)):
    rate.append(rating[i].get_text())
rate

print(len(rate))
print(rate.pop(0))
print(rate.pop(0))
print(rate)

review = soup.find_all("span",{"data-hook":"review-body"})
print(review)

review_content = []
for i in range(0,len(review)):
    review_content.append(review[i].get_text())
review_content

print(len(review_content))

import pandas as pd
df = pd.DataFrame()
print(df)

df ['Customer Name'] = cust_name
print(df)

df['Review title'] = review_title
df['Rating'] = rate
df['Reviews'] = review_content

print(df)
