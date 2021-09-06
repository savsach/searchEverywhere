from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print("What would you like to search? \n")
search = input(">")


driverG = webdriver.Firefox()
driverG.get("https://google.com/")
driverG.maximize_window()
driverG.implicitly_wait(3)
driverG.find_element_by_css_selector('input[title="Search"]').send_keys(f"{search} " + Keys.ENTER)


driverD = webdriver.Firefox()

driverD.get("https://duckduckgo.com/")
driverD.maximize_window()
driverD.implicitly_wait(3)
driverD.find_element_by_id('search_form_input_homepage').send_keys(f"{search}" + Keys.ENTER)


driverB = webdriver.Firefox()

driverB.get("https://www.bing.com/")
driverB.maximize_window()
driverB.implicitly_wait(3)
driverB.find_element_by_id('sb_form_q').send_keys(f"{search}" + Keys.ENTER)




