import requests
import pyfiglet
import html2text
from bs4 import BeautifulSoup

continue_option ='Y'
link_number =0
while continue_option=='Y' or continue_option == 'y':
    link_number =1
    list_of_links= []
    result = pyfiglet.figlet_format("BREWSER", font = "slant" ) 
    print(result)

    url = input("Enter Url: ")
    try:
        body = requests.get(url)
    except:
        print("Shadow Realm hasn't seen people like you in a while!Wanna visit?")
        exit()

    print("*"*50)
    if body.status_code == 200:
        web_page = html2text.html2text(body.text)
    elif body.status_code == 404:
        print("ERROR 404, Teleporting You to Shadow Realm!")
        exit()
    elif body.status_code == 500:
        print("Internal Server Error")
        exit()
    else:
        web_page = html2text.html2text(body.text)

    print(web_page)
    print("*"*50)

    soup = BeautifulSoup(body.text,"html.parser")
    
    show_links=input("Do you want to see the links?(Y/N): ")

    if show_links=='Y' or show_links=='y':
        for link in soup.find_all('a', href=True):
            print(link_number,")",link['href'].lstrip('/'))
            list_of_links.append(link['href'].lstrip('/'))
            link_number+=1

    print(list_of_links)
    
    continue_option = input("Do you want to continue?(Y/N): ")

print("Developed by NecromancertheDark")
