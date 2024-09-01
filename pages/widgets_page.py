import random
import time

import allure
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date
from locators.widgets_page_locators import AccordianLocators, AutocompleteLocators, DatePickerLocators, SliderLocators, \
    ProgressBarLocators, TabsLocators, TooltipsLocators, MenuLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):

    locators = AccordianLocators()

    @allure.step('Check accordian with one paragraph')
    def check_accordian_with_one_paragraph(self, accordian_number):

        accordian = {
            'first': {
                'header': self.locators.FIRST_SECTION,
                'content': self.locators.FIRST_SECTION_TEXT
            },
            'second': {
                'header': self.locators.SECOND_SECTION,
                'content': self.locators.SECOND_SECTION_TEXT
            },
            'third': {
                'header': self.locators.THIRD_SECTION,
                'content': self.locators.THIRD_SECTION_TEXT
            }
        }
        accordian_header = self.element_is_visible(accordian[accordian_number]['header'])
        accordian_header.click()
        accordian_content = self.element_is_visible(accordian[accordian_number]['content']).text
        print(len(accordian_content))
        print(accordian_header.text)

        return accordian_header.text, len(accordian_content)

    @allure.step('Check accordian with several paragraphs')
    def check_accordian_with_several_paragraphs(self):

        accordian_header = self.element_is_visible(self.locators.SECOND_SECTION)
        accordian_header.click()
        paragraphs = self.elements_are_visible(self.locators.SECOND_SECTION_TEXT)
        text_len = 0
        for paragraph in paragraphs:
            paragraph_content = paragraph.text
            text_len += len(paragraph_content)
        return accordian_header.text, text_len


class AutocompletePage(BasePage):

    locators = AutocompleteLocators()

    @allure.step('Add colors to multiple autocomplete field')
    def add_colors_to_multiple_autocomplete(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 7))

        for color in colors:
            input_multi = self.element_is_visible(self.locators.MULTIPLE_COLOR_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)

        return colors

    @allure.step('Remove value from multiple autocomplete field')
    def remove_value_from_multiple_color_field(self):
        count_value_before = len(self.elements_are_visible(self.locators.MULTIPLE_COLOR_BOX))
        remove_buttons_list = self.elements_are_visible(self.locators.MULTIPLE_COLOR_REMOVE)
        for value in remove_buttons_list:
            value.click()
            break
        count_value_after = len(self.elements_are_present(self.locators.MULTIPLE_COLOR_BOX))

        return count_value_before, count_value_after

    @allure.step('Check colors in multiple autocomplete field')
    def check_color_in_multiple_input(self):
        color_list = self.elements_are_present(self.locators.MULTIPLE_COLOR_BOX)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    @allure.step('Add color to single input field')
    def add_color_to_single_input(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        single_color = self.element_is_visible(self.locators.SINGLE_COLOR_INPUT)
        single_color.send_keys(color)
        single_color.send_keys(Keys.ENTER)
        return color[0]

    @allure.step('Check color in single input field')
    def check_single_color(self):
        color = self.element_is_visible(self.locators.SINGLE_COLOR_VALUE)
        return color.text


class DatePickerPage(BasePage):

    locators = DatePickerLocators()

    @allure.step('Set date by text')
    def set_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    @allure.step('Find day in list')
    def set_day_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                time.sleep(1)
                break

    @allure.step('Find year in list')
    def find_year_in_list(self, years_list, year):
        while True:
            visible_years_elements = self.elements_are_visible(years_list)
            visible_years = [i.text for i in visible_years_elements]
            if year in visible_years:
                return visible_years
            elif int(year) < int(visible_years[-2]):
                for i in range(11):
                    self.element_is_visible(self.locators.PREVIOUS_YEARS).click()
            elif int(year) > int(visible_years[2]):
                for i in range(11):
                    self.element_is_visible(self.locators.UPCOMING_YEARS).click()

    @allure.step('Set date')
    def set_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        input_date_before = input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_day_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        input_date_after = input_date.get_attribute('value')
        return input_date_before, input_date_after

    @allure.step('Set date and time')
    def set_date_and_time(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        input_date_time_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_visible(self.locators.DATE_AND_TIME_SELECT_YEAR).click()
        self.find_year_in_list(self.locators.DATE_AND_TIME_SELECT_YEAR_LIST, date.year)
        self.set_day_item_from_list(self.locators.DATE_AND_TIME_SELECT_YEAR_LIST, date.year)
        self.element_is_visible(self.locators.DATE_AND_TIME_SELECT_MONTH).click()
        self.set_day_item_from_list(self.locators.DATE_AND_TIME_SELECT_MONTH_LIST, date.month)
        self.set_day_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        self.set_day_item_from_list(self.locators.DATE_AND_TIME_SELECT_TIME_LIST, date.time)
        input_date_time_after = input_date.get_attribute('value')
        return input_date_time_before, input_date_time_after


class SliderPage(BasePage):

    locators = SliderLocators()

    @allure.step('Check slider value')
    def check_slider_value(self):
        slider_value = self.element_is_visible(self.locators.SLIDER_VALUE_INPUT)
        return slider_value.get_attribute('value')

    @allure.step('Move slider')
    def move_slider(self):

        slider_input = self.element_is_visible(self.locators.SLIDER_BAR_INPUT)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(0, 100), 0)


class ProgressBarPage(BasePage):

    locators = ProgressBarLocators()

    @allure.step('Check progress bar value')
    def check_progress_bar_value(self):
        progress_bar_value = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        return progress_bar_value

    @allure.step('Click start/stop button')
    def click_start_stop_button(self):
        self.element_is_visible(self.locators.START_STOP_BUTTON).click()
        time.sleep(random.randint(2, 6))
        self.element_is_visible(self.locators.START_STOP_BUTTON).click()


class TabsPage(BasePage):

    locators = TabsLocators()

    @allure.step('Check content of tabs')
    def check_tabs(self, tab_name):

        tabs = {
            'what': {
                    'title': self.locators.TAB_WHAT,
                    'content': self.locators.TAB_WHAT_CONTENT
                },
            'origin': {
                    'title': self.locators.TAB_ORIGIN,
                    'content': self.locators.TAB_ORIGIN_CONTENT
                },
            'use': {
                    'title': self.locators.TAB_USE,
                    'content': self.locators.TAB_USE_CONTENT
                }
        }

        tab_name_to_click = self.element_is_visible(tabs[tab_name]['title'])
        tab_name_to_click.click()
        tab_content = self.element_is_present(tabs[tab_name]['content']).text
        return tab_name_to_click.text, len(tab_content)


class TooltipsPage(BasePage):

    locators = TooltipsLocators()

    @allure.step('Get text from tooltip')
    def get_tooltip_text(self, hover_element, wait_element):
        element = self.element_is_present(hover_element)
        self.action_move_to_element(element)
        time.sleep(1)
        self.element_is_visible(wait_element)
        time.sleep(1)
        tooltip_text = self.element_is_visible(self.locators.TOOLTIPS_TEXT).text
        return tooltip_text

    @allure.step('Check tooltip text by element')
    def check_tooltip_text_by_element(self, tooltip_element):

        tooltips = {
            'button': {
                    'hover_element': self.locators.BUTTON,
                    'tooltip_element': self.locators.BUTTON_TOOLTIP
                },
            'field': {
                    'hover_element': self.locators.FIELD,
                    'tooltip_element': self.locators.FIELD_TOOLTIP
                },
            'word': {
                    'hover_element': self.locators.WORD,
                    'tooltip_element': self.locators.WORD_TOOLTIP
                },
            'number': {
                    'hover_element': self.locators.NUMBER,
                    'tooltip_element': self.locators.NUMBER_TOOLTIP
                }
        }

        tooltip_text = self.get_tooltip_text(tooltips[tooltip_element]['hover_element'],
                                             tooltips[tooltip_element]['tooltip_element'])
        return tooltip_text


class MenuPage(BasePage):

    locators = MenuLocators()

    @allure.step('Check menu items')
    def check_menu_items(self):

        menu_item_list = self.elements_are_present(self.locators.MENU_ITEMS_LIST)
        data = []
        for item in menu_item_list:
            self.action_move_to_element(item)
            data.append(item.text)
        return data

