#!/usr/bin/env python
# coding: utf-8

# In[13]:


#Import dependencies
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import pandas as pd


# In[14]:


from webdriver_manager.chrome import ChromeDriverManager


# In[15]:


#Testing Scraping via web browser
executable_path = {"executable_path": ChromeDriverManager().install()}
browser = Browser("chrome", **executable_path, headless=False)


# <h2>1. NASA Mars News

# In[16]:


#Load URL to be scraped
n_url = 'https://mars.nasa.gov/news/'


# In[ ]:





# In[17]:


browser.visit(n_url)
html = browser.html
soup = bs(html, 'html.parser')


# In[18]:


print(soup.prettify())


# In[19]:


#Extract info from slide
art = soup.find_all('li', class_='slide')
art


# In[20]:


#Get first title in art
c_ti = art[0].find('div', class_ = 'content_title')
#Extract text
n_ti = c_ti.text.strip()
#Get first body in art
art_body = art[0].find('div', class_ = 'article_teaser_body')
#Extract text
n_p = art_body.text.strip()


# In[21]:


#Print content
print("Title: ",n_ti)
print("Paragraph: ",n_p)
#Quit browser
browser.quit()


# <h2>2. JPL Mars Space Images

# In[27]:


#Launch web browser
executable_path = {"executable_path": ChromeDriverManager().install()}
browser = Browser("chrome", **executable_path, headless=False)


# In[28]:


#load URL
j_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'


# In[29]:


browser.visit(j_url)
html = browser.html
j_soup = bs(html, 'html.parser')


# In[30]:


j_img = j_soup.find_all('a', class_="fancybox")


# In[31]:


image = []
for x in j_img:
    pic = x['data-fancybox-href']
    image.append(pic)

featured_image_url = 'https://www.jpl.nasa.gov' + pic
featured_image_url


# In[32]:


browser.quit()


# <h2>3. Mars Weather

# In[33]:


#Launch web browser
executable_path = {"executable_path": ChromeDriverManager().install()}
browser = Browser("chrome", **executable_path, headless=False)


# In[34]:


w_url = 'https://twitter.com/marswxreport?lang=en'


# In[35]:


browser.visit(w_url)
w_html = browser.html
w_soup = bs(w_html, "html.parser")


# In[36]:


w_soup


# In[37]:


m_tw = [w_soup.find_all('p', class_="TweetTextSize"), w_soup.find_all('span', class_="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0")]


# In[38]:


m_tw


# In[39]:


browser.quit()


# In[ ]:


#Couldn't find within the soup response anything resembling the text within 
#tweets to extract


# <h2> 4. Mars Facts

# In[40]:


f_url = 'https://space-facts.com/mars/'


# In[41]:


fact_table = pd.read_html(f_url)
fact_table


# In[42]:


f_df = fact_table[0]


# In[43]:


f_df


# In[44]:


f_df.columns = ['Parameter', 'Measurement']
f_df


# In[45]:


html_fact = f_df.to_html()


# In[46]:


print(html_fact)


# In[47]:


#Save to html
f_df.to_html('html_mars_table.html')


# <h2>5. Mars Hemispheres

# In[85]:


#Launch web browser
executable_path = {"executable_path": ChromeDriverManager().install()}
browser = Browser("chrome", **executable_path, headless=False)


# In[103]:


#URL name and image
base_url = 'https://astrogeology.usgs.gov'
url = base_url + '/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'


# In[104]:


#Browser visit and data extraction
browser.visit(url)
html = browser.html
hemi_soup = bs(html, 'html.parser')


# In[105]:


hemi_soup


# In[106]:


items = hemi_soup.find_all('div', class_='item')


# In[107]:


items


# In[109]:


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
    
    hemisphere_image_urls.append(image_dict)

print(hemisphere_image_urls)


# In[112]:


for i in range(len(hemisphere_image_urls)):
    print(hemisphere_image_urls[i]['title'])
    print(hemisphere_image_urls[i]['img_url'] + '\n')


# In[113]:


browser.quit()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[84]:





# In[ ]:





# In[ ]:





# In[ ]:




