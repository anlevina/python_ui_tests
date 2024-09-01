import time

import allure

from locators.alerts_frame_windows_locators import BrowserWindowsLocators, AlertsLocators, FramesLocators, \
    NestedFramesLocators, ModalDialogsLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):

    locators = BrowserWindowsLocators()

    @allure.step('Click new window')
    def click_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW).click()

    @allure.step('Click new tab or window')
    def click_new_tab_or_window(self, selector):

        entities = {
            'tab': self.locators.NEW_TAB,
            'window': self.locators.NEW_WINDOW
        }

        self.element_is_visible(entities[selector]).click()

    @allure.step('Get text from a new tab')
    def get_text_from_new_tab(self):
        text_from_new_tab = self.element_is_present(self.locators.NEW_TAB_CONTENT).text
        return text_from_new_tab


class AlertsPage(BasePage):

    locators = AlertsLocators()

    @allure.step('Click simple alert')
    def click_simple_alert(self):
        self.element_is_visible(self.locators.SIMPLE_ALERT).click()

    @allure.step('Click time alert')
    def click_time_alert(self):
        self.element_is_visible(self.locators.TIME_ALERT).click()
        time.sleep(6)

    @allure.step('Click confirmation alert')
    def click_confirmation_alert(self):
        self.element_is_visible(self.locators.CONFIRM_ALERT).click()

    @allure.step('Get confirmation alert message')
    def get_confirmation_alert_message(self):
        message = self.element_is_visible(self.locators.CONFIRM_MESSAGE).text
        return message

    @allure.step('Click prompt alert')
    def click_prompt_alert(self):
        self.element_is_visible(self.locators.PROMPT_ALERT).click()

    @allure.step('Get prompt alert message')
    def get_prompt_alert_message(self):
        message = self.element_is_visible(self.locators.PROMPT_MESSAGE).text
        return message


class FramesPage(BasePage):

    locators = FramesLocators()

    @allure.step('Check frame content')
    def check_frame(self, frame):

        frames = {
            'large_frame': self.locators.LARGE_FRAME,
            'small_frame': self.locators.SMALL_FRAME,
        }

        chosen_frame = self.element_is_present(frames[frame])
        width, height = chosen_frame.get_attribute('width'), chosen_frame.get_attribute('height')
        self.driver.switch_to.frame(chosen_frame)
        frame_text = self.element_is_present(self.locators.FRAME_TITLE).text
        self.driver.switch_to.default_content()
        return width, height, frame_text


class NestedFramesPage(BasePage):

    locators = NestedFramesLocators()

    @allure.step('Check nested frames')
    def check_nested_frames(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_FRAME_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_FRAME_TEXT).text
        return parent_text, child_text


class ModalDialogsPage(BasePage):

    locators = ModalDialogsLocators()

    @allure.step('Click modal dialog')
    def check_modal_dialog(self, modal):

        modals = {
            'small': {
                'open_button': self.locators.SMALL_MODAL,
                'title': self.locators.SMALL_MODAL_TITLE,
                'text': self.locators.SMALL_MODAL_TEXT,
                'close_button': self.locators.SMALL_MODAL_CLOSE
            },
            'large': {
                'open_button': self.locators.LARGE_MODAL,
                'title': self.locators.LARGE_MODAL_TITLE,
                'text': self.locators.LARGE_MODAL_TEXT,
                'close_button': self.locators.LARGE_MODAL_CLOSE
            }
        }

        self.element_is_visible(modals[modal]['open_button']).click()
        title = self.element_is_present(modals[modal]['title']).text
        text = self.element_is_present(modals[modal]['text']).text
        self.element_is_visible(modals[modal]['close_button']).click()
        return title, len(text)

