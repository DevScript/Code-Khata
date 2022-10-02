from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/') #opening the site using selenium

input('Scan the QR code and then press "enter"')
name_of_recipient = input('To whom do you want to send the message:') #to whom do you want to send the texts
msg = input('Enter your message:')

user = driver.find_element_by_xpath(f'//span[@title = "{name_of_recipient}"]') #finding the user to whom we have to send
user.click()
textbox = driver.find_element_by_class_name('_3uMse') #text box in which the message is sent

for i in range(200):
    textbox.send_keys(msg) #writing the message on the text box
    send = driver.find_element_by_class_name('_1U1xa')  #for the send button
    send.click() #clicking the send button
    time.sleep(5) #waiting for 5 seconds before sending the message again

driver.quit()
