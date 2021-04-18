from selenium import webdriver
import time

def without_key():

    driver = webdriver.Chrome('/home/saqib/work/asnm-crawl/chromedriver/chromedriver')

    driver.get('https://ansm.sante.fr/S-informer/Informations-de-securite-Lettres-aux-professionnels-de-sante')
    driver.maximize_window()
    driver.refresh()

    time.sleep(5)

    details = []

    for i in range(1,10):
        data = driver.find_element_by_xpath('//*[@id="wrapper"]/div[3]/div/article['+ str(i) +']')
        
        category = data.find_element_by_class_name('article-category').text
        product_type = data.find_element_by_class_name('article-health-product').text
        article_date = data.find_element_by_class_name('article-date').text
        article_title = data.find_element_by_class_name('article-title').text
        # print(category, product_type, article_date, article_title)

        details.append([product_type, category, article_date, article_title])

    # for i in details:
    #     print(i)

    # time.sleep(2)
    driver.close()

    return details