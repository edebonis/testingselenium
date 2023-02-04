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
browser.get('https://www.mercadolibre.com.ar')
title = browser.title
assert 'Mercado Libre' in title
browser.implicit_wait(1)

search = browser.find_element('id', 'cb1-edit')
search.send_keys('moto g100')
search.submit()


ol_results = browser.find_elements(By.TAG_NAME, 'ol')

for ol in ol_results:
    print(ol.text)
