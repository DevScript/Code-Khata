import requests
from bs4 import BeautifulSoup
import smtplib  
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
import time
import datetime
import sys


def price_checker(url):
    time.sleep(30)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")
    pars_price = soup.find_all("div", {"class": "My(6px) Pos(r) smartphone_Mt(6px)"})[0].find_all(text=True, recursive=True)
    price = float(pars_price[0].replace(',', ''))
    market_status = pars_price[2]
    print(price)
    return price, market_status

def gmail_sender(epass='password', addr_from='your@address.com', addr_to='your@address.com', email_theme='Message from Python script!', message=None):

    msg = MIMEMultipart()  
    msg['From'] = addr_from 
    msg['To'] = addr_to  
    msg['Subject'] = email_theme  

    body = message
    msg.attach(MIMEText(body, 'plain')) 

    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.starttls()  
    server.login(addr_from, epass) 
    server.send_message(msg)  
    server.quit()



def market_status_checker():
    #print(datetime.date.today())
    current_time = int(datetime.datetime.today().strftime("%H"))
    if current_time >= 12 and current_time < 21:
        return True
    else:
        return False


def close_counter(value):
    time.sleep(1)
    for i in range(value + 1):
        print(f'----------------- {value - i} -----------------')
        time.sleep(1)
    sys.exit()


def main():
    url = 'https://finance.yahoo.com/quote/LKOH.ME?p=LKOH.ME&.tsrc=fin-srch'
    print('Price Controller launched!')
    while True:
        while market_status_checker() == True:
            price, market_status = price_checker(url)

            if price >= 5300:
                gmail_sender(message=f'Price = {price}')
                print(f'Attention! Price is {price}!')
                close_counter(30)
        else:
            print('Market is closed!')
            time.sleep(300)


if __name__ == '__main__':
    main()
