from os import path
import json,time,argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

with open('/home/zekousek/Documents/workflow-automatisation-python/source/json/passwords.json', 'r') as f:
    data = json.load(f)
    f.close()

parser = argparse.ArgumentParser(description='Name of the github repository')
parser.add_argument('name', type=str)
args = parser.parse_args()

reponame = args.name

username = data["username"]
password = data["password"]
chromedriver = '/home/zekousek/Documents/workflow-automatisation-python/source/chromesource/chromedriver'
options = Options()
service = Service(log_path=path.devnull)
# chrome_options.binary_location('/usr/bin/brave-browser')
options.add_argument('--headless')

def web_run():
    driver = webdriver.Firefox(options=options, service=service)

    driver.get('https://github.com/login')
    driver.find_element(By.XPATH, '//*[@id="login_field"]').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[13]').click()

    driver.get('https://github.com/new')
    driver.find_element(By.XPATH, '//*[@id="react-aria-2"]').send_keys(reponame)
    time.sleep(0.5)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/main/react-app/div/div/form/div[5]/button').click()

    
if __name__ == '__main__':
    web_run()
