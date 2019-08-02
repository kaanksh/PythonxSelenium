from selenium import webdriver
import time

email = "sampleid1420" #your login email id
pwd = "samplepassword1420" #your login password
rec = "makanksha777@gmail.com" #recipient's email id
subj = "Automation Test" #subject of the mail
txt = "This is how automation is performed with the combination of Python and Selenium webdriver." #text body of mail

driver = webdriver.Chrome(executable_path="../driver/chromedriver.exe")
driver.maximize_window()
driver.get("http://www.gmail.com/")
time.sleep(1)
driver.find_element_by_name("identifier").send_keys(email)
driver.find_element_by_id("identifierNext").click()
driver.implicitly_wait(5)
driver.find_element_by_name("password").send_keys(pwd)
driver.find_element_by_id("passwordNext").click()
driver.find_element_by_css_selector('.aic .z0 div').click()
driver.find_element_by_id(":96").send_keys(rec)
driver.find_element_by_id(":8o").send_keys(subj)
driver.find_element_by_id(":9t").send_keys(txt)
driver.find_element_by_id(":8e").click()
time.sleep(4)
driver.close()
driver.quit()

print("An email has been sent successfully.")

