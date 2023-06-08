from os import path
import json,time,argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

#* Opens the JSON file and reads it and saves it into data
with open('/home/zekousek/Documents/workflow-automatisation-python/source/json/passwords.json', 'r') as f:
    data = json.load(f)
    f.close()

#* Taking data from command line for the name of the repository
parser = argparse.ArgumentParser(description='Name of the github repository')
parser.add_argument('name', type=str)
args = parser.parse_args()

#* Taking data from JSON files and argparse and saves it into variables
reponame = args.name
username = data["username"]
password = data["password"]

#* Add options to webdriver
options = Options()
#* This option prevents selenium from creating .log file
service = Service(log_path=path.devnull)
#* This option runs Firefox without a window
options.add_argument('--headless')

def web_run():
    #* Opens the webdriver, but you won't see it
    driver = webdriver.Firefox(options=options, service=service)
    #* Logins to Github Login page and sends the username and password and click Login button
    driver.get('https://github.com/login')
    driver.find_element(By.XPATH, '//*[@id="login_field"]').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[13]').click()
    
    #* After login is going to create a new repository 
    driver.get('https://github.com/new')
    driver.find_element(By.XPATH, '//*[@id="react-aria-2"]').send_keys(reponame)

    #* Paused due to Github checking if the repo-name is available
    time.sleep(0.5)

    driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/main/react-app/div/div/form/div[5]/button').click()
    driver.quit()
    
if __name__ == '__main__':
    web_run()
