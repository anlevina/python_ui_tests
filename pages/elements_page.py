import base64
import os
import random

import allure
import requests
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from generator.generator import generated_person, generated_file
from pages.base_page import BasePage
from locators.elements_page_locators import (TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators,
                                             WebPageLocators, DifferentClicksLocators, LinksLocators,
                                             DownloadUploadLocators, DynamicPropertiesLocators)


class TextBoxPage(BasePage):

    locators = TextBoxPageLocators()

    @allure.step('Fill all fields')
    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()

        return full_name, email, current_address, permanent_address

    @allure.step('Check filled form')
    def check_filled_form(self):
        full_name = self.element_is_visible(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_visible(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_visible(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_visible(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]

        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):

    locators = CheckBoxPageLocators()

    @allure.step('Open full list of checkboxes')
    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    @allure.step('Click random checkboxes')
    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    @allure.step('Get checked checkboxes')
    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        checked_items = []
        for box in checked_list:
            item_title = box.find_element(By.XPATH, self.locators.ITEM_TITLE)
            checked_items.append(item_title.text)
        print(checked_items)

        return (str(checked_items).replace(' ', '').replace('doc', '')
                .replace('.', '').lower())

    @allure.step('Get results')
    def get_output_results(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        checked_output_items = []
        for item in result_list:
            checked_output_items.append(item.text)
        print(checked_output_items)

        return str(checked_output_items).replace(' ', '').lower()


class RadioButtonPage(BasePage):

    locators = RadioButtonPageLocators()

    @allure.step('Click radio button')
    def click_radio_button(self, button):

        buttons = {
            'yes': self.locators.YES_RADIOBUTTON,
            'impressive': self.locators.IMPRESSIVE_RADIOBUTTON
        }

        self.element_is_visible(buttons[button]).click()

    @allure.step('Get results')
    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):

    locators = WebPageLocators()

    @allure.step('Click add button')
    def click_add_button(self):
        self.element_is_visible(self.locators.ADD_BUTTON).click()

    @allure.step('Fill person fields')
    def fill_person_fields(self):
        person_info = next(generated_person())
        first_name = person_info.first_name
        last_name = person_info.last_name
        email = person_info.email
        age = person_info.age
        salary = person_info.salary
        department = person_info.department
        if len(department) > 24:
            department = department[:24]

        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.AGE).send_keys(age)
        self.element_is_visible(self.locators.SALARY).send_keys(salary)
        self.element_is_visible(self.locators.DEPARTMENT).send_keys(department)

        return [first_name, last_name, str(age), email, str(salary), department]

    @allure.step('Click submit button')
    def click_submit_button(self):
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @allure.step('Click added person')
    def click_added_person(self):
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
        return data

    @allure.step('Search for person in web page table')
    def search_person_in_web_table(self, key_word):
        self.element_is_visible(self.locators.SEARCH_FIELD).click()
        self.element_is_visible(self.locators.SEARCH_FIELD).send_keys(key_word)

    @allure.step('Check person in web page table')
    def check_person_in_web_table(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element(By.XPATH, self.locators.PARENT_ROW)
        return row.text.splitlines()

    @allure.step('Click edit button')
    def click_edit_button(self):
        edit_button = self.element_is_visible(self.locators.EDIT_BUTTON).click()

    @allure.step('Update data for person')
    def update_person(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.AGE).clear()
        self.element_is_visible(self.locators.AGE).send_keys(age)
        return str(age)

    @allure.step('Click delete button')
    def click_delete_button(self):
        delete_button = self.element_is_visible(self.locators.DELETE_BUTTON).click()

    @allure.step('Check that table is empty')
    def table_is_empty(self):
        return self.element_is_visible(self.locators.NO_ROWS_FOUND).text

    @allure.step('Check amount of rows in table')
    def check_amount_of_rows(self):
        list_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)

    @allure.step('Change amount of rows')
    def change_amount_of_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            row_button = self.element_is_visible(self.locators.ROWS_AMOUNT)
            self.go_to_element(row_button)
            row_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f'option[value="{x}"')).click()
            data.append(self.check_amount_of_rows)

        return count


class DifferentClicksPage(BasePage):

    locators = DifferentClicksLocators()

    @allure.step('Perform double click')
    def double_click(self):
        self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK))

    @allure.step('Check double click message')
    def double_click_message(self):
        double_click_message = self.element_is_visible(self.locators.DOUBLE_CLICK_MESSAGE)
        return double_click_message.text

    @allure.step('Perform right click')
    def right_click(self):
        self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK))

    @allure.step('Check right click message')
    def right_click_message(self):
        right_click_message = self.element_is_visible(self.locators.RIGHT_CLICK_MESSAGE)
        return right_click_message.text

    @allure.step('Perform single click')
    def single_click(self, driver):
        single_click_button = driver.find_element(By.XPATH, self.locators.SINGLE_CLICK)
        single_click_button.click()

    @allure.step('Check single click message')
    def single_click_message(self):
        single_click_message = self.element_is_visible(self.locators.SINGLE_CLICK_MESSAGE)
        return single_click_message.text


class LinksPage(BasePage):

    locators = LinksLocators()

    @allure.step('Check new tab simple link')
    def check_new_tab_simple_link(self):
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        link_href = simple_link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            simple_link.click()
            url = self.switch_to_tab(self.driver)
            return link_href, url
        else:
            return request.status_code

    @allure.step('Check new tab dynamic link')
    def check_new_tab_dynamic_link(self):
        simple_link = self.element_is_visible(self.locators.DYNAMIC_LINK)
        link_href = simple_link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            simple_link.click()
            url = self.switch_to_tab(self.driver)
            return link_href, url
        else:
            return link_href, request.status_code

    @allure.step('Check broken link')
    def check_broken_link(self, link):

        links = {
            'created': {
                'button': self.locators.CREATED,
                'url': 'https://demoqa.com/created'
            },
            'no_content': {
                'button': self.locators.NO_CONTENT,
                'url': 'https://demoqa.com/no-content'
            },
            'moved': {
                'button': self.locators.MOVED,
                'url': 'https://demoqa.com/moved'
            },
            'bad_request': {
                'button': self.locators.BAD_REQUEST,
                'url': 'https://demoqa.com/bad-request'
            },
            'unauthorized': {
                'button': self.locators.UNAUTHORIZED,
                'url': 'https://demoqa.com/unauthorized'
            },
            'forbidden': {
                'button': self.locators.FORBIDDEN,
                'url': 'https://demoqa.com/forbidden'
            },
            'not_found': {
                'button': self.locators.NOT_FOUND,
                'url': 'https://demoqa.com/invalid-url'
            }
        }

        request = requests.get(links[link]['url'])
        if request.status_code == 200:
            self.element_is_present(links[link]['button']).click()
        else:
            return request.status_code


class DownloadUploadPage(BasePage):

    locators = DownloadUploadLocators()

    @allure.step('Upload a file')
    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_visible(self.locators.UPLOAD_FILE).send_keys(path)
        os.remove(path)
        return file_name.split('\\')[-1]

    @allure.step('Check that file has been uploaded')
    def check_uploaded_file(self):
        file_path = self.element_is_present(self.locators.UPLOADED_FILE_PATH).text
        return file_path.split('\\')[-1]

    @allure.step('Download file')
    def download_file(self):
        image_link = self.element_is_visible(self.locators.DOWNLOAD_FILE).get_attribute('href')
        decoded_image_link = base64.b64decode(image_link)
        image_path = rf'C:\Users\Ana\PycharmProjects\python_ui_tests\image_for_test{random.randint(0, 10)}.jpeg'
        with open(image_path, 'wb+') as f:
            offset = decoded_image_link.find(b'\xff\xd8')
            f.write(decoded_image_link[offset:])
            check_file = os.path.exists(image_path)
            f.close()
        os.remove(image_path)
        return check_file


class DynamicPropertiesPage(BasePage):

    locators = DynamicPropertiesLocators()

    @allure.step('Check that element is enabled after certain time')
    def check_enabled_after_button_is_clickable(self):
        try:
            self.element_is_visible(self.locators.ENABLED_AFTER).click()
        except TimeoutException:
            return False
        return True

    @allure.step('Check that element has changed colour after certain time')
    def check_color_change_button_color(self):
        color_button = self.element_is_present(self.locators.COLOR_CHANGE)
        color = color_button.value_of_css_property('color')
        return color

    @allure.step('Check that element has became visible after certain time')
    def check_visible_after_button_is_shown(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER)
        except TimeoutException:
            return False
        return True
