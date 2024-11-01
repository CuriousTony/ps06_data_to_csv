import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_data():
    driver = webdriver.Chrome()
    driver.get('https://www.divan.ru/sankt-peterburg/category/stulya')
    time.sleep(3)

    try:
        raw_content = driver.find_elements(By.CSS_SELECTOR, 'div.WdR1o')
        try:
            with open('Kitchen_chairs.csv', 'w', encoding='utf-8-sig', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Название', 'Цена', 'Ссылка'])
                for content in raw_content:
                    name = content.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]').text
                    price = content.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU.KIkOH').text
                    link = content.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8.qUioe.ProductName.ActiveProduct').get_attribute('href')
                    writer.writerow([name, price, link])
        except Exception as ex:
            print(f"Ошибка в ходе записи в файл - {ex}")

    except Exception as e:
        print(f"Ошибка в CSS селекторах - {e}")

    finally:
        print('driver.quit()')
        driver.quit()


get_data()
