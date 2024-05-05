import requests
import sys
import time
from bs4 import BeautifulSoup

def type_effect(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)

code = '''
 __        __  ___       ___  __  
|__)  /\  |__)  |  |  | |__  |__) 
|    /~~\ |  \  |  |/\| |___ |__) 
                                  
{───────────────────────────────────────────────────}
OWNER ~> AGAND842
What does this tool do? When this tool is run, it takes the address of a site from us, and then when we give it, it shows us all the parts of the site.
{───────────────────────────────────────────────────}
'''


type_effect(code)


url = input("[+]website~> ")
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))
