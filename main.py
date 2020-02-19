import random
import string
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def generate_email():
    file = open("firstnames.txt", "r")
    firstname = file.read().splitlines()
    firstname = firstname[random.randint(0, len(firstname) - 1)]
    option = random.randint(0, 2)
    if option == 0:
        firstname = firstname.upper()
    elif option == 1:
        firstname = firstname.lower()
    else:
        firstname = firstname.title()

    file = open("lastnames.txt", "r")
    lastname = file.read().splitlines()
    lastname = lastname[random.randint(0, len(lastname) - 1)]
    option = random.randint(0, 2)
    if option == 0:
        lastname = lastname.upper()
    elif option == 1:
        lastname = lastname.lower()
    else:
        lastname = lastname.title()

    domains = ["@gmail.com", "@hotmail.co.uk", "@outlook.com", "@aol.com", "@mail.com"]
    number = str(random.randint(0, 500))

    finalCombo = {0: firstname + number + lastname,
                  1: lastname + number + firstname,
                  2: firstname + lastname + number,
                  3: lastname + firstname + number}

    return finalCombo[random.randint(0, 3)] + domains[random.randint(0, len(domains)-1)]


def generate_password():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(5, 25)))

if __name__ == "__main__":
    #Setup web driver
    driver = webdriver.Chrome("chromedriver.exe", options=webdriver.ChromeOptions())

    #Start main loop
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
        # Allow the user to exit the program by using using Control-C 
        except (KeyboardInterrupt, SystemExit): 
            print("Exiting program...")
            raise
        # Preventing timeouts
        except:
            pass
