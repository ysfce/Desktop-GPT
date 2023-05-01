from undetected_chromedriver import Chrome, ChromeOptions
from time import sleep
import os
import sys

email = "email"
password = "password"

options = ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
chrome = Chrome(options=options)

chrome.get("https://chat.openai.com/")

chrome.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/button[1]").click()
sleep(3)
chrome.find_element_by_xpath("/html/body/div/main/section/div/div/div/div[1]/div/form/div[1]/div/div/div/input").send_keys(email)
chrome.find_element_by_xpath("/html/body/div/main/section/div/div/div/div[1]/div/form/div[2]/button").click()
sleep(3)
chrome.find_element_by_xpath("/html/body/div/main/section/div/div/div/form/div[1]/div/div[2]/div/input").send_keys(password)
chrome.find_element_by_xpath("/html/body/div/main/section/div/div/div/form/div[2]/button").click()
sleep(2.5)
chrome.find_element_by_xpath("/html/body/div[3]/div/div/div/div[2]/div/div/div[2]/div[4]/button").click()
chrome.find_element_by_xpath("/html/body/div[3]/div/div/div/div[2]/div/div/div[2]/div[4]/button[2]").click()
chrome.find_element_by_xpath("/html/body/div[3]/div/div/div/div[2]/div/div/div[2]/div[4]/button[2]").click()
sleep(1)
# for döngüsü eklenecek
a=0
while True:
    a+=2
    prompt = input("Send a message: ")
    if (prompt==""):
        a-=2
        continue
    chrome.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/main/div[2]/form/div/div[2]/textarea").send_keys(prompt)
    chrome.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/main/div[2]/form/div/div[2]/button").click()
    sleep(2.5)
    message = chrome.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/main/div[1]/div/div/div/div[{}]/div/div[2]/div[1]/div/div".format(a)).text
    sleep(2.5)
    while True:
        if (message==(chrome.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/main/div[1]/div/div/div/div[{}]/div/div[2]/div[1]/div/div".format(a)).text)):
            break
        else:
            message=chrome.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/main/div[1]/div/div/div/div[{}]/div/div[2]/div[1]/div/div".format(a)).text
        for char in "\|/-":
            sys.stdout.write("\r" + "thinking" + " " + char)
            sys.stdout.flush()
            sleep(0.1)
        sleep(2)
        sys.stdout.write("\r" + " " * len("thinking") + "\r")
        sys.stdout.flush()

    for char in message:
        print(char, end="", flush=True)
        sleep(0.01)
    print(" ")

chrome.close()