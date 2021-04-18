from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def with_key():

    driver = webdriver.Chrome('/home/saqib/work/asnm-crawl/chromedriver/chromedriver')

    driver.get('https://ansm.sante.fr/S-informer/Informations-de-securite-Lettres-aux-professionnels-de-sante')
    driver.maximize_window()
    driver.refresh()

    search_field = driver.find_elements_by_id('filter_text')[0]
    search_field.clear()
    search_field.send_keys('covid')
    search_field.send_keys(Keys.ENTER)

    # print(search_field)

    details = []

    for i in range(1,10):
        data = driver.find_element_by_xpath('//*[@id="wrapper"]/div/div/article['+ str(i) +']')

        category = data.find_element_by_xpath('//*[@id="wrapper"]/div/div/article[1]/a/span[1]').text
        product_type = data.find_element_by_xpath('//*[@id="wrapper"]/div/div/article[1]/a/span[2]').text
        article_date = data.find_element_by_class_name('article-date').text
        article_title = data.find_element_by_class_name('article-title').text
        # print(product_type, category, article_date, article_title)

        details.append([category, product_type, article_date, article_title])

    # print(details)
    # for i in details:
    #     print(i)


    # time.sleep(2)
    driver.close()

    return details