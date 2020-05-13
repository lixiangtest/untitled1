from selenium import webdriver
import selenium


def test_login():
    driver = webdriver.Chrome()
    driver.get("https://home.testing-studio.com/t/topic/58/6")
