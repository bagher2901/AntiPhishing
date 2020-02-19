import random
import string
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def generate_email(option=random.randint(0, 2)):
    # Opens the file, chooses a random line then strips any new lines at the end
    firstname = random.choice(open('firstnames.txt').readlines()).rstrip()
    lastname = random.choice(open('lastnames.txt').readlines()).rstrip()
    domain = random.choice(open('domains.txt').readlines()).rstrip()
    
    # Generate a random number to include in the email
    number = str(random.randint(0, 500))

    # Choose the case for the username based on the option parameter
    if option == 0:
        firstname = firstname.upper()
        lastname = lastname.upper()
    elif option == 1:
        firstname = firstname.lower()
        lastname = lastname.lower()
    else:
        firstname = firstname.title()
        lastname = lastname.title()

    # Join the username, shuffle it randomly and then return it with the domain appended
    username = [firstname, lastname, number]
    random.shuffle(username)
    return ''.join(username) + domain


def generate_password():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(5, 25)))

# Setup web driver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome("chromedriver.exe", options=options)

# Code below for flooding their database
while True:
    try:
        driver.get("WEBSITE HERE")
        
        # Structure for generic login wall

        email = driver.find_element_by_xpath('EMAIL/USERNAME ELEMENT XPATH')
        email.send_keys(generate_email())

        password = driver.find_element_by_xpath('PASSWORD ELEMENT XPATH')
        password.send_keys(generate_password())

        login = driver.find_element_by_xpath('LOGIN BUTTON ELEMENT XPATH')
        login.click()

    except: # Preventing timeouts
        pass
