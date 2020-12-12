#!/usr/bin/env python
# coding: utf-8

#Import dependencies
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import pandas as pd
import time


#from webdriver_manager.chrome import ChromeDriverManager

def debugger(contents):
    file = open('_temp.txt',"w",encoding="utf-8")
    file.write(contents)
    file.close()

def scrape():
    init_browser():
    executable_path = {"executable_path": ChromeDriverManager().install()}
    browser = Browser("chrome", **executable_path, headless=False)
    browser = init_browser
    mars_dict = {}


    #NASA Mars News
    #Load URL to be scraped
    n_url = 'https://mars.nasa.gov/news/'
    browser.visit(n_url)
    time.sleep(3)
    html = browser.html
    soup = bs(html, 'html.parser')
    art = soup.find_all('li', class_='slide')
    c_ti = art[0].find('div', class_ = 'content_title')
    
    #**************************
    n_ti = c_ti.text.strip()
    #**************************

    art_body = art[0].find('div', class_ = 'article_teaser_body')
    
    #**************************
    n_p = art_body.text.strip()
    #**************************



    #JPL Mars Space Images
    j_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(j_url)
    time.sleep(3)
    html = browser.html
    j_soup = bs(html, 'html.parser')
    j_img = j_soup.find_all('a', class_="fancybox")
    image = []
    for x in j_img:
        pic = x['data-fancybox-href']
        image.append(pic)

    #****************************************************
    featured_image_url = 'https://www.jpl.nasa.gov' + pic
    #****************************************************

    #Mars Weather
    w_url = 'https://twitter.com/marswxreport?lang=en'

    browser.visit(w_url)
    time.sleep(3)
    w_html = browser.html
    w_soup = bs(w_html, "html.parser")


    #m_tw = [w_soup.find_all('p', class_="TweetTextSize"), w_soup.find_all('span', class_="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0")]
    #Couldn't find within the soup response anything resembling the text within 
    #tweets to extract


    #Mars Facts

    f_url = 'https://space-facts.com/mars/'
    fact_table = pd.read_html(f_url)
    fact_table
    f_df = fact_table[0]
    f_df.columns = ['Parameter', 'Measurement']
    #*************************
    html_fact = f_df.to_html()
    #*************************

    #Mars Hemispheres

    #URL name and image
    base_url = 'https://astrogeology.usgs.gov'
    url = base_url + '/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    time.sleep(3)
    html = browser.html
    hemi_soup = bs(html, 'html.parser')
    items = hemi_soup.find_all('div', class_='item')

    hemisphere_image_urls = []

# Iterate through each hemisphere data
    for i in items:
        # Collect Title
        hemisphere = i.find('div', class_="description")
        title = hemisphere.h3.text
        
        # Collect image link by browsing to hemisphere page
        hemisphere_link = hemisphere.a["href"]    
        browser.visit(usgs_url + hemisphere_link)
        
        image_html = browser.html
        image_soup = bs(image_html, 'html.parser')
        
        image_link = image_soup.find('div', class_='downloads')
        image_url = image_link.find('li').a['href']

        # Create Dictionary to store title and url info
        image_dict = {}
        image_dict['title'] = title
        image_dict['img_url'] = image_url
        
        #***************************************
        hemisphere_image_urls.append(image_dict)
        #***************************************
    
    #Mars Dictionary

    mars_dict = {
        "news_title": n_ti,
        "news_paragraph": n_p,
        "featured_image_url": featured_image_url,
        "mars_weather": "Empty",
        "fact_table": str(html_fact),
        "hemisphere_images": hemisphere_image_urls
    }

    return mars_dict

    browser.quit()





