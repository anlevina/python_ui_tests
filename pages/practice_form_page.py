import os
import random

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from generator.generator import (generated_person, generated_file, generated_subject, generated_state_and_city,
                                 generated_date)
from locators.practice_form_locators import PracticeFormPageLocators
from pages.base_page import BasePage


class PracticeFormPage(BasePage):

    locators = PracticeFormPageLocators()

    @allure.step('Set date item from list')
    def set_date_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break

    @allure.step('Set date of birth')
    def set_dob(self):
        dob = next(generated_date())
        dob_field = self.element_is_visible(self.locators.DATE_OF_BIRTH)
        dob_value_before = dob_field.get_attribute('value')
        dob_field.click()
        self.set_date_item_from_list(self.locators.YEAR_LIST, dob.year)
        self.set_date_item_from_list(self.locators.MONTH_LIST, dob.month)
        self.set_date_item_from_list(self.locators.DAYS_LIST, dob.day)
        dob_value_after = dob_field.get_attribute('value')
        return dob_value_before, dob_value_after

    @allure.step('Set hobbies')
    def set_hobbies(self):
        hobbies = [self.locators.HOBBY_SPORTS, self.locators.HOBBY_READING, self.locators.HOBBY_MUSIC]
        hobbies_sample = random.sample(hobbies, k=(random.randint(1,3)))
        data = []
        for i in hobbies_sample:
            selected_hobby = self.element_is_visible(i)
            selected_hobby.click()
            data.append(selected_hobby.text)
        data_to_string = ', '.join(data)
        return data_to_string

    @allure.step('Set subjects')
    def set_subjects(self):
        subjects = generated_subject()
        data = []
        for subject in subjects:
            input_subject = self.element_is_visible(self.locators.SUBJECTS_FIELD)
            input_subject.send_keys(subject)
            input_subject.send_keys(Keys.RETURN)
            data.append(subject)
        return data

    @allure.step('Get subjects')
    def get_subjects(self):
        selected_subjects = self.elements_are_visible(self.locators.SUBJECTS_ELEMENTS)
        data = []
        for subject in selected_subjects:
            data.append(subject.text)
        data_to_string = ', '.join(data)
        return data_to_string

    @allure.step('Set state and city')
    def set_state_and_city(self, driver):
        state, city = generated_state_and_city()

        state_and_city_list = ['state', 'city']

        state_and_city_dict = {
            'state': {
                'locator': self.locators.SELECT_STATE,
                'name': state
            },
            'city': {
                'locator': self.locators.SELECT_CITY,
                'name': city
            },
        }

        for entity in state_and_city_list:
            state_dropdown = self.element_is_visible(state_and_city_dict[entity]['locator'])
            state_dropdown.click()
            option_to_select_state = driver.find_element(By.XPATH,
                            f'//div[@id="stateCity-wrapper"]//div[text()="{state_and_city_dict[entity]['name']}"]')
            option_to_select_state.click()

    @allure.step('Get state and city')
    def get_state_and_city(self):
        state_and_city_list = self.elements_are_visible(self.locators.STATE_AND_CITY_FIELDS)
        state_and_city = []
        for entity in state_and_city_list:
            state_and_city.append(entity.text)
        state, city = state_and_city[0], state_and_city[1]
        return state, city

    @allure.step('Upload file')
    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_visible(self.locators.UPLOAD_PICTURE).send_keys(path)
        os.remove(path)
        return path.split('\\')[-1]

    @allure.step('Fill all fields')
    def fill_all_fields(self):
        person_info = next(generated_person())
        first_name = person_info.first_name
        last_name = person_info.last_name
        email = person_info.email
        mobile = person_info.mobile
        if len(mobile) > 10:
            mobile = mobile[:10]

        current_address = person_info.current_address

        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        gender = self.element_is_visible(self.locators.RANDOM_GENDER)
        gender.click()
        self.element_is_visible(self.locators.MOBILE).send_keys(mobile)
        dob_value_before, dob_value_after = self.set_dob()
        hobbies = self.set_hobbies()
        self.set_subjects()
        selected_subjects = self.get_subjects()
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.set_state_and_city(self.driver)
        state, city = self.get_state_and_city()

        return (first_name, last_name, email, gender.text, mobile, dob_value_before, dob_value_after, selected_subjects,
                hobbies, current_address, state, city)

    @allure.step('Fill only mandatory fields')
    def fill_only_mandatory_fields(self):
        person_info = next(generated_person())
        first_name = person_info.first_name
        last_name = person_info.last_name
        mobile = person_info.mobile
        if len(mobile) > 10:
            mobile = mobile[:10]

        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        gender = self.element_is_visible(self.locators.RANDOM_GENDER)
        gender.click()
        self.element_is_visible(self.locators.MOBILE).send_keys(mobile)
        dob_value_before, dob_value_after = self.set_dob()

        return first_name, last_name, gender.text, mobile, dob_value_before, dob_value_after

    @allure.step('Click submit button')
    def submit(self):
        self.element_is_visible(self.locators.SUBMIT).click()

    @allure.step('Click close button')
    def close(self):
        self.element_is_visible(self.locators.CLOSE).click()

    @allure.step('Get results from final table')
    def form_result(self):
        result_list = self.elements_are_visible(self.locators.RESULT_TABLE)
        result_text = [i.text for i in result_list]

        return result_text




