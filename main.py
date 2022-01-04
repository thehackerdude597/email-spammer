import selenium
from selenium import webdriver
import requests
import random
from bs4 import BeautifulSoup
import time





class spamObjects():
    def main():
        path_of_driver = input("What is the path of chrome webdriver (requried)?: ")
        limit = int(input("How many times would you like to spam: "))
        message = input("What is the message you want to send?: ")
        subject = input("What is the subject of your email?: ")
        email_to_send = input("Send to: ")
        
        driver = webdriver.Chrome(executable_path=path_of_driver)
        for i in range(limit):

            url = requests.get("https://www.behindthename.com/random/random.php?number=2&sets=1&gender=both&surname=&all=yes").text

            call = BeautifulSoup(url, 'html.parser')
            locate = call.find('a', class_="plain")
            print("Your automated random name is: " + locate.text)
            generated_name = locate.text
            email_domains = ['@icloud.com', '@ifruit.com', '@yahoo.com', '@gmail.com', "@hotmail.com", "@outlook.com", '@yopmail.com']
            domain = random.choice(email_domains)
            email = generated_name + domain
            print(email)




                
            pull_source = driver.get("https://emkei.cz")
                #Entering basic info given from the suspect
            from_name = driver.find_element_by_xpath("""//*[@id="fromname"]""")
            from_name.click()
            from_name.send_keys(generated_name)
            from_email = driver.find_element_by_xpath("""//*[@id="from"]""")
            from_email.click()
            from_email.send_keys(email)
            to = driver.find_element_by_xpath("""//*[@id="rcpt"]""")        
            to.click()
            to.send_keys(email_to_send)
            sub = driver.find_element_by_xpath("""//*[@id="subject"]""")
            sub.click()
            sub.send_keys(subject)
            mes = driver.find_element_by_xpath("""//*[@id="text"]""")
            mes.click()
            mes.send_keys(message)
            send = driver.find_element_by_xpath("""//*[@id="sendfrm"]/table[3]/tbody/tr[4]/td[2]/input[2]""")
            send.click()





spamObjects.main()
