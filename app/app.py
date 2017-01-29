#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time

from config import info

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://mi-pay.three.ie/UnregisteredTopup')
    assert 'Instant Top Up' in driver.title

    # Step 1 - Number and amount
    phone_num_field = driver.find_element_by_name("PhoneNumber")
    phone_num_field.clear()
    phone_num_field.send_keys(info['number'])
    amount_select = Select(driver.find_element_by_id('Amount'))
    amount_select.select_by_value(info['topup_amount'])
    submit_btn = driver.find_element_by_id('submitButton')
    submit_btn.click()

    # Step 2 - Personal Info
    email_field = driver.find_element_by_name('Email')
    email_field.clear()
    email_field.send_keys(info['email'])
    firstname_field = driver.find_element_by_name('FirstName')
    firstname_field.clear()
    firstname_field.send_keys(info['firstname'])
    lastname_field = driver.find_element_by_name('LastName')
    lastname_field.clear()
    lastname_field.send_keys(info['lastname'])
    address_line1_field = driver.find_element_by_name('Address1')
    address_line1_field.clear()
    address_line1_field.send_keys(info['address']['line1'])
    address_line2_field = driver.find_element_by_name('Address2')
    address_line2_field.clear()
    address_line2_field.send_keys(info['address']['line2'])
    city_field = driver.find_element_by_name('City')
    city_field.clear()
    city_field.send_keys(info['address']['city'])
    postcodal_field = driver.find_element_by_name('PostalCode')
    postcodal_field.clear()
    postcodal_field.send_keys(info['address']['postal_code'])
    country_select = Select(driver.find_element_by_id('Country'))
    country_select.select_by_visible_text(info['address']['country'])
    submit_btn = driver.find_element_by_id('submitButton')
    submit_btn.click()

    # Step 3 - Credit Card
    card_type_select = Select(driver.find_element_by_id('CardType'))
    card_type_select.select_by_visible_text(info['credit_card']['type'])
    cardnumber_field = driver.find_element_by_name('CardNumber')
    cardnumber_field.clear()
    cardnumber_field.send_keys(info['credit_card']['number'])
    expiry_month_select = Select(driver.find_element_by_id('Month'))
    expiry_month_select.select_by_value(info['credit_card']['exp_month'])
    expiry_year_select = Select(driver.find_element_by_id('Year'))
    expiry_year_select.select_by_value(info['credit_card']['exp_year'])
    cvc_field = driver.find_element_by_name('SecurityCode')
    cvc_field.clear()
    cvc_field.send_keys(info['credit_card']['cvc'])
    submit_btn = driver.find_element_by_id('submitButton')
    submit_btn.click()

    # Step 4 - Confirm
    ts_and_cs_box = driver.find_element_by_name('AcceptTermsAndCond')
    ts_and_cs_box.click()
    submit_btn = driver.find_element_by_id('submitButton')
    submit_btn.click()
