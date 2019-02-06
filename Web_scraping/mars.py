
from bs4 import BeautifulSoup as bs
import pandas as pd
from splinter import Browser
import requests
import pymongo
import time

def scrape():
    executable_path = {'executable_path': '/Users/michaelduffner/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser')

    news_title = soup.find('div',class_ = "content_title").text
    news_p = soup.find('div',"article_teaser_body").text

    print(news_title)
    print(news_p)

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(5)
    browser.click_link_by_partial_text('more info')
    html = browser.html
    soup = bs(html,'html.parser')

    image_url = soup.find('figure', class_='lede').a['href']
    featured_image_url = "https://www.jpl.nasa.gov/" + image_url

    print(featured_image_url)

    url="https://twitter.com/marswxreport?lang=en"

    response=requests.get(url)
    

    soup = bs(response.text, 'html.parser')




    tweets= soup.find("p", class_="TweetTextSize")


    mars_weather= tweets.text


    url = "http://space-facts.com/mars/"

    table = pd.read_html(url)
    table_df = table[0]
    table_df = table_df.rename(columns={0:"Category", 1:"Value"})
    table_df = table_df.set_index("Category")
    table_df

    hem = []

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser')


    hemispheres=[]
    hemisphere_data = soup.findAll("div", class_="description")

for data in hemisphere_data:
        name = data.a.h3.text
        print(name)
        browser.click_link_by_partial_text(name)
        time.sleep(3)
        browser.click_link_by_partial_text('Open')
        time.sleep(2)
        html = browser.html
        soup = bs(html, 'html.parser')
        img_src = soup.find('img', class_="wide-image")['src']

        img_src_full = f"https://astrogeology.usgs.gov" + img_src
        print(img_src_full)
        name = name[:-9]
        hemispheres_images = {"title":name, "img_url":img_src_full}
        hemispheres.append(hemispheres_images)
        print(hemispheres)
        browser.click_link_by_partial_text('Close')
        time.sleep(3)
        browser.click_link_by_partial_text('Back')
