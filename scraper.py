from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import datetime
import time

#driver setup
driver = webdriver.Firefox()
driver.get("http://pitchfork.com/reviews/albums")

#scraping info
albums = driver.find_elements_by_class_name('review')
album_links = [album.find_element_by_class_name('review__link').get_attribute('href') for album in albums]


titles = [album.find_element_by_class_name('review__title-album').text.lower() for album in albums]
authors = [album.find_element_by_class_name('display-name--linked').text.lower()[4:] for album in albums]
artists = [album.find_element_by_class_name('review__title-artist').text.lower() for album in albums]

def _get_review_info(link):
    """Function navigates to the input link, then scrapes the following data:
    Title, score, author, author type, publication data, content.
    """
    driver.get(link)
    author = driver.find_element_by_class_name('authors-detail__display-name').text.lower()
    author_type = driver.find_element_by_class_name('authors-detail__title').text.lower()
    content = driver.find_element_by_class_name("contents").text
    genre = driver.find_element_by_class_name("genre-list__link").text.lower()
    pub_datetime = driver.find_element_by_class_name("pub-date").get_attribute('datetime')
    score = driver.find_element_by_class_name('score-circle').text
    title = driver.find_element_by_class_name('review__title-album')


    return {
        "author": author,
        "author_type": author_type,
        "content": content,
        "genre": genre,
        "pub_datetime": pub_datetime,
        "score": score,
        "title": title,
    }

review_data = [_get_review_info(´link) for link in review_links while (datetime.today() - pub_datetime] <= 7]





1. one by one go to pages
2. pull out text, date published
3. go through p tags, avoid links and only grab text from the links.

# reviewid
# title
# artist
# url
# score
# best_new_music
# author
# author_type
# pub_date
# pub_weekday
# pub_day
# pub_month
# pub_year
[
    { title: string, author: string, date: datetime, review_text: string, score: number}
]

3. stop at certain datetime (i.e. current datetime minus 7 days)
4. store as a list of dictionaries

driver.get(album_links[0])

url =
artist =
score =
best_new_music =
pub_date =
author =
author_type =
title = driver.find_element_by_class_name()
date =

content = driver.find_element_by_class_name('contents')