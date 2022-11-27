import re
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from driver import driver
from .variables import WEBSITE, ARTICLE, REJECTED_URL_SUBSTRINGS


def get_category_urls(anchor_elements):
    """
    Accepts the css selector of all a tags of the category.
    Returns a set containing the urls from all a tags.
    """
    driver.get(WEBSITE['url'])
    anchor_elements = driver.find_elements(By.CSS_SELECTOR, anchor_elements)
    urls = set()
    for anchor in anchor_elements:
        url = anchor.get_attribute('href')
        urls.add(url.strip())
    return urls


def get_category_name_url_pairs(category_urls):
    """
    Returns the names of the categories and the category urls
    as key value pairs.
    key: the part after the last / of the category url.
    value: the category url.
    """
    pairs = {}
    for url in category_urls:
        category = url.split('/')[-1]
        pairs[category] = url
    return pairs


def get_recent_articles(category_name_url_pairs):
    """
    Returns the name of the category and the url of the
    first article of each category as key value pairs,
    if the article is less that 4 days old.
    KEY: the category name.
    VALUE: the url of the first article.
    """
    recent_articles = {}
    for name, url in category_name_url_pairs.items():
        driver.get(url)
        post_date_info_list = driver.find_element(
            By.CSS_SELECTOR, ARTICLE['post_date']
        ).text.lower().split(' ')
        time_value = post_date_info_list[0]
        if len(time_value) > 2:
            continue
        time_unit = post_date_info_list[1]
        article_is_recent = not time_unit.startswith(ARTICLE['time_unit']) or \
                            int(time_value) < ARTICLE['time_value']
        if article_is_recent:
            anchor_element = driver.find_element(By.CSS_SELECTOR, ARTICLE['url'])
            article_url = anchor_element.get_attribute('href')
            recent_articles[name] = article_url.strip()
    return recent_articles


def get_unique_pairs(recent_articles):
    """
    Rejects the keys that have the same value with other keys
    in the dictionary, and returns the unique pairs.
    """
    pairs = {}
    urls = []
    for category, url in recent_articles.items():
        if url in urls:
            continue
        urls.append(url)
        pairs[category] = url
    return pairs


def get_url_accepted_pairs(unique_pairs):
    """
    Returns the articles whose url does not contain
    any of the substrings inside REJECTED_URL_SUBSTRINGS
    """
    pairs = {}
    for category, url in unique_pairs.items():
        for substring in REJECTED_URL_SUBSTRINGS:
            if substring in url:
                break
            else:
                pairs[category] = url
    return pairs


def sanitize_image_links(image_element):
    """
    Removes any unwanted characters like spaces and new lines
    from the value of srcset of the image element and returns
    the srcset as a string.
    """
    images_list = re.findall(ARTICLE['images'], image_element.get_attribute('srcset'))
    images = ''
    for image in images_list:
        images += image + ','
    return images[:-1]

def sanitize_body_content(body_content):
    """
    Removes any paragraphs which are less than 11 words long,
    and returns the body content as a string.
    """
    body = ''
    for tag in body_content:
        text = tag.text
        number_of_words = len(text.split(' '))
        text_is_a_paragrapgh = number_of_words > ARTICLE['min_word_number']
        if text_is_a_paragrapgh:
            body += text.strip() + '\n'
    return body[:-2] + '.'


def get_article(content):
    """
    Returns a dictionary with the article content,
    like the title, the author etc.
    """
    try:
        author = content.find_element(By.CSS_SELECTOR, ARTICLE['author'])
        date_time = content.find_element(By.CSS_SELECTOR, ARTICLE['datetime'])
        title = content.find_element(By.CSS_SELECTOR, ARTICLE['title'])
        image_element = content.find_element(By.CSS_SELECTOR, ARTICLE['image'])
        body_content = content.find_elements(By.CSS_SELECTOR, ARTICLE['body'])
    except NoSuchElementException:
        return

    body = sanitize_body_content(body_content)
    if not body or author.text.lower() == WEBSITE['name']:
        return
    post_date = date_time.text.split(' ')[0]
    post_time = date_time.text.split(' ')[-1]
    images = sanitize_image_links(image_element)

    return {
        "website": WEBSITE['name'],
        "images": images.strip(),
        "author": author.text.strip(),
        "post_date": post_date,
        "post_time": post_time,
        "title": title.text.strip(),
        "body": body.strip()
    }


def get_articles(url_accepted_pairs, main_category):
    """
    Returns a list of dictionaries with all available articles.
    """
    articles = []
    for category, url in url_accepted_pairs.items():
        driver.get(url)
        try:
            content = driver.find_element(By.CSS_SELECTOR, ARTICLE['content'])
        except NoSuchElementException:
            continue

        article = get_article(content)
        if not article:
            continue

        article['url'] = url.strip()
        article['main_category'] = main_category.strip()
        article['category'] = category.strip()
        articles.append(article)

    return articles
