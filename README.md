# web-scraping-challenge

<h2>Web Scraping Challenge Homework<h2>. 
  

<h3>Steps<h3>.
  
<h4>Step 1: Scraping<h4>. 

Everything in this section is contained in 
Step 1: Scrape NASA Mars News
  (https://mars.nasa.gov/news/page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest)
  
Obtain news title and news paragraph

Step 2: Scrape JPL Mars Space Images

(https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)

Obtain image url

Step 3: Scrape Twitter for Mars Weather

Incomplete - unable to get twitter information

Step 4: Scrape to get Mars facts

(https://space-facts.com/mars/)

Obtain a table with mars facts

Step 5: Scrape for images of Mars Hemispheres

(https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)

Get images of the 4 Mars hemispheres

<h4>Step 2. MongoDB and Flask Application<h4>. 
  
- Convert jupyter notebook to python script (scrape_mars.py)
- Script automatically launches and scrapes data
- Create an index.html page
- Create a new app (app.py) that calls the scrape_mars script and launches the index.html page. The app also creates a DB within mongo DB to store. 
a dictionary created in the script

