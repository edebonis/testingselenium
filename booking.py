import time
import tkinter as tk
from tkcalendar import Calendar, DateEntry
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Form:
    def __init__(self):
        self.website = "https://www.booking.com"
        self.window = tk.Tk()
        self.window.geometry("240x200")
        self.window.resizable(width=0,height=0)
        self.window.title("Scraping Booking.com")
        self.country_label = tk.Label(self.window, text="Country")
        self.country = tk.Entry(self.window)
        self.country.insert(0, "Argentina")
        self.location_label = tk.Label(self.window, text="Location")
        self.location = tk.Entry(self.window)
        self.location.insert(0, "Salta")
        self.date_label = tk.Label(self.window, text="Date")
        self.date_entry = DateEntry(self.window)
        self.scrape_btn = tk.Button(self.window, text="Scrape", command=self.scrape)
        self.country_label.pack()
        self.country.pack()
        self.location_label.pack()
        self.location.pack()
        self.date_label.pack()
        self.date_entry.pack()
        self.scrape_btn.pack(padx=6, pady=16)
        self.window.mainloop()

    def scrape(self):
        country = self.country.get()
        location = self.location.get()
        date = self.date_entry.get()
        print(country, location, date)
        opts = Options()
        # opts.add_argument('--headless')
        browser = Chrome(options=opts)
        browser.get(self.website)
        title = browser.title
        assert 'Booking' in title
        browser.implicitly_wait(5)
        search = browser.find_element('name', 'ss')
        date_form = browser.find_elements(By.TAG_NAME, 'span')
        for span in date_form:
            print(span.get_attribute('innerHTML'))
        search.send_keys(f"{location}, {country}")
        date_form.click()
        browser.implicitly_wait(5)
        time.sleep(5)
        #date_form.send_keys(date)

        #search.submit()

        #ol_results = browser.find_elements(By.TAG_NAME, 'ol')




if __name__ == '__main__':
    form = Form()


