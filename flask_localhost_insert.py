import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = Options()
#opts.add_argument('--headless')
browser = Chrome(options=opts)
browser.get('localhost:5000/auth/login')

username_f = browser.find_element('id', 'username')
password_f = browser.find_element('id', 'password')
username_f.send_keys('edebonis')
password_f.send_keys('qvg80280')
password_f.submit()

buttons = browser.find_elements(By.TAG_NAME, 'button')
print(buttons)
for button in buttons:
    if button.text == 'OK':
        button.click()

        a_tags = browser.find_elements(By.TAG_NAME, 'a')
        for tag in a_tags:
            if tag.text == 'Idea nueva':
                tag.click()
                WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID, "title"))).send_keys('Idea nueva   ')
                description = browser.find_element('id', 'description')
                description.send_keys('Descrición de idea nueva')
                public = browser.find_element('id', 'is_public')
                public.click()
                category = browser.find_element('id', 'category_id')
                cat_select = Select(category).select_by_index(1)

                time.sleep(1)
                category.submit()
                break
        break

