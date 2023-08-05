import random
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


def make_review(product_card_link: str, review_text: str, login_email: str, password: str):

    browser = webdriver.Firefox()

    # step 1 - open product card
    browser.get(product_card_link)
    browser.implicitly_wait(7)
    sleep(random.randrange(5, 8))

    # step 2 - click to 'залишити відгук'
    login_link = browser.find_element(By.CSS_SELECTOR, '.rating--desktop')
    login_link.click()

    # step 3 - input email V
    # in release version login and password should be from txt file
    user_email_input = browser.find_element(By.XPATH, '//*[@id="email"]')
    user_email_input.send_keys(login_email)
    sleep(random.randrange(2, 5))

    # step 4 - click 'увійти'
    enter_button_1 = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/button')
    enter_button_1.click()

    # step 5 - input password
    user_password_input = browser.find_element(By.XPATH, '//*[@id="password"]')
    user_password_input.send_keys(password)
    sleep(random.randrange(2, 5))

    # step 6 - click 'увійти' V
    enter_button_2 = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/button')
    enter_button_2.click()
    sleep(random.randrange(5, 8)) # Kasta is reloading the page

    # step 7 - click 'залишити відгук' V
    review_push_1 = browser.find_element(By.XPATH, '//*[@id="reviewRating"]/div[1]/div[1]/div[2]/span')
    review_push_1.click()
    sleep(random.randrange(3, 6))

    # step 8 - input question
    review_input = browser.find_element(By.XPATH, '//*[@id="reviewInput"]')
    review_input.send_keys(review_text)
    sleep(random.randrange(4, 7))

    # step 9 - click '5 stars' V
    push_rate_5 = browser.find_element(By.CSS_SELECTOR, '#reviewForm > form > div.review-popup__container > div.review-popup__stars.mt-2 > label:nth-child(3)')
    push_rate_5.click()
    sleep(random.randrange(3, 6))

    # step 10 - click 'залишити відгук'
    review_push_2 = browser.find_element(By.XPATH, '//*[@id="reviewForm"]/form/div[2]/button/span')
    review_push_2.click()
    sleep(random.randrange(3, 8))

    browser.close()
