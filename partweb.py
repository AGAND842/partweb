import requests
import sys
import time
from bs4 import BeautifulSoup

def type_effect(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)

code = '''
 __        __  ___       ___  __  
|__)  /\  |__)  |  |  | |__  |__) 
|    /~~\ |  \  |  |/\| |___ |__) 
                                  
{~~~~~~~~~~~~~~~~~~~}
* OWNER ~> AGAND842 *
{~~~~~~~~~~~~~~~~~~~}
'''


type_effect(code)


url = input("[+]website~> ")
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))
