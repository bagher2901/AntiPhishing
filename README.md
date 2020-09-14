# AntiPhishing
 A small program with the intent to disrupt phishing websites. main.py provides the basic structure for a login wall as well as methods to aid you in destroying their databases.
 
## Functions
`generate_email()`

Returns a randomised email using firstnames.txt, lastnames.txt and domains.txt

*returns string*
<br/><br/>

`generate_password()`

Returns a randomised string of characters and numbers

*returns string*
<br/><br/>

`generate_fullname()`

Returns a randomised name using firstnames.txt and lastnames.txt

*returns string*
<br/><br/>

## Setup
If you want to set this up for a certain website you'll first need to install Selenium.
Run the following command in terminal to install the package API:

`pip install selenium`


Open up main.py within your editor and locate the line:
`driver.get("WEBSITE HERE")`
You'll want to find a website that you know is a phishing website. https://www.phishtank.com/ has listings for known Phishing websites and is updated daily.

The following will be for a generic login wall.

1. Copy the Xpath of the email entry
2. Paste into the string arg for `email = driver.find_element_by_xpath('EMAIL/USERNAME ELEMENT XPATH')`
3. Copy the Xpath of the password entry
4. Paste into the string arg for `password = driver.find_element_by_xpath('PASSWORD ELEMENT XPATH')`
5. Copy the Xpath of the login button
6. Paste into the string arg for `login = driver.find_element_by_xpath('LOGIN BUTTON ELEMENT XPATH')`

If the login wall covers multiple pages where it goes from email, to password and then to clicking logging in, then Selenium will handle it with the same code structure.

