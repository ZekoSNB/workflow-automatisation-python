
import json,time,argparse
from selenium import webdriver
from selenium.webdriver.common.by import By

with open('json/passwords.json', 'r') as f:
    data = json.load(f)
    f.close()

parser = argparse.ArgumentParser(description='Name of the github repository')
parser.add_argument('name', type=str)
args = parser.parse_args()

reponame = args.name

username = data["username"]
password = data["password"]

chromedriver = '/home/zeko/Documents/wawpy/source/chromesource/chromedriver'

driver = webdriver.Chrome(chromedriver)

driver.get('https://github.com/login')

driver.find_element(By.XPATH, '//*[@id="login_field"]').send_keys(username)
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
driver.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[13]').click()

driver.get('https://github.com/new')

driver.find_element(By.XPATH, '//*[@id="react-aria-2"]').send_keys(reponame)

time.sleep(10)
