#!/usr/bin/env python
import sys
import re
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from config import info


def is_valid_phone_number(number):
    """Checks phone number is valid"""
    num_regex = r'08[2-9]\d{7}'
    if re.match(num_regex, number) is not None:
        return True
    return False


def is_valid_topup_amount(amount):
    """Checks the top-up amount conforms to Three's options"""
    try:
        amount = float(amount)
    except:
        return False

    if ((10.00 <= amount <= 30.00 and amount % 5 == 0) or
            (30.00 <= amount <= 50.00 and amount % 10 == 0)):
        return True
    return False


def setup(sysargs):
    """If arguments are supplied, overrides the config values.
    Checks that the phone number and top-up amount are valid."""
    if len(sysargs) == 3:
        info['number'] = sysargs[1]
        info['topup_amount'] = sysargs[2]

    if not is_valid_phone_number(info['number']):
        print('Supplied phone number does not seem like a valid '
              'Irish phone number...')
        sys.exit(1)

    if not is_valid_topup_amount(info['topup_amount']):
        print('Supplied top-up amount doesn\'t match Three\'s options. '
              'Must be: 10.00, 15.00, 20.00, 25.00, 30.00, 40.00 or 50.00.')
        sys.exit(1)


if __name__ == '__main__':
    setup(sys.argv)

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
