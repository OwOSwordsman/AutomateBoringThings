import time
from selenium import webdriver


def main():
    browser = webdriver.Firefox()
    browser.get("https://clickspeedtest.com/")
    clicker = browser.find_element_by_css_selector("#clicker")

    for _ in range(100):
        clicker.click()

    """
    button = browser.find_element_by_css_selector("#action-button")
    button.click()
    button = browser.find_element_by_css_selector('#mobile_search')
    button.click()
    searchbar = browser.find_element_by_css_selector(".search-input")
    searchbar.send_keys('boruto')
    searchbar.submit()
    """


if __name__ == "__main__":
    main()
    input()
