import requests
import pyfiglet
import html2text

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
