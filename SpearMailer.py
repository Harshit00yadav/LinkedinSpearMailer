import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time


def run(playwright: Playwright) -> None:
    EOP = input("Email or phone : ")
    password = input("password : ")
    name = input("enter target profile : ")
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #------------- LOGIN ----------------------------
    page.goto("https://www.linkedin.com/uas/login")
    page.get_by_label("Email or phone").fill(EOP)
    page.get_by_label("Password").fill(password)
    page.get_by_label("Sign in", exact=True).click()
    #-------------- LOCATE PROFILE -------------------
    page.get_by_role("link", name="My Network").click()
    page.get_by_role("link", name="Connections").click()
    page.get_by_placeholder("Search by name").fill(name)
    page.get_by_role("link", name=f"Member’s name {name}").click()
    #----------------- SEND MESSAGE ------------------
    page.get_by_role("button", name=f"Message {name.split(' ')[0]}").click()
    with open(r"./messages_per_person.txt", "r") as message:
        time.sleep(10)
        for line in message.readlines():
            time.sleep(2.5)
            page.get_by_label("Write a message…").get_by_role("paragraph").click()
            page.get_by_label("Write a message…").fill(line)
            page.get_by_role("button", name="Send", exact=True).click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

