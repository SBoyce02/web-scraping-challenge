 # Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas as pd


def scrape():

    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)



    url = 'https://redplanetscience.com/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    # Examine the results, then determine element that contains sought info
    print(soup.prettify())


    newest_title = soup.body.find('div', class_= 'content_title').text
    newest_title


    newest_paragraph = soup.body.find('div', class_= 'article_teaser_body').text
    newest_paragraph

    # part 2 -JPL Mars Space Images - Featured Image
    #activity that found code = https://ku.bootcampcontent.com/ku-coding-boot-camp/ku-virt-data-pt-01-2021-u-c/-/blob/master

    # Visit the following URL
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    featured_image= soup.find('img', class_ = 'headerimage fade-in')['src']

    featured_image

    featured_image_url = url + featured_image
    featured_image_url


    #part 3 Mars Facts

    url ='https://galaxyfacts-mars.com/'

    tables = pd.read_html(url)
    tables

    df=tables[0]
    df.columns = ['Mars-Earth Comparison', 'Mars', 'Earth']
    df.head()

    clean_df = df.iloc[1:]
    clean_df.set_index('Mars-Earth Comparison',inplace=True)
    clean_df.head()

    table_html = clean_df.to_html()
    table_html

browser.quit()