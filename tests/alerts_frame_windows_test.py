import allure
import pytest

from pages_actions.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, \
    ModalDialogsPage


@allure.suite('Alerts, Frames and Windows page')
class TestAlertsFrameWindows:

    @allure.feature('New tabs and windows')
    class TestNewEntity:

        @allure.title('Open new tab or window')
        @pytest.mark.parametrize('entity', [
            'tab',
            'window'
        ])
        def test_open_new_entity(self, driver, entity):
            open_new_entity = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            open_new_entity.open()
            open_new_entity.remove_footer()
            open_new_entity.click_new_tab_or_window(entity)
            opened_url = open_new_entity.switch_to_tab(driver)
            visible_text = open_new_entity.get_text_from_new_tab()

            assert opened_url == 'https://demoqa.com/sample', 'Different url has been opened in new tab'
            assert visible_text == 'This is a sample page', 'Different content has been shown in new tab'

    @allure.feature('Web page alerts')
    class TestAlerts:

        @allure.title('Click simple alert')
        def test_click_simple_alert(self, driver):
            click_simple_alert = AlertsPage(driver, 'https://demoqa.com/alerts')
            click_simple_alert.open()
            click_simple_alert.remove_footer()
            click_simple_alert.click_simple_alert()
            alert_message = click_simple_alert.switch_to_alert(driver)
            click_simple_alert.accept_alert(driver)

            assert alert_message == 'You clicked a button', 'Alert has not been opened or has shown another message'

        @allure.title('Click alert that appears after 5 seconds')
        def test_click_time_alert(self, driver):
            click_time_alert = AlertsPage(driver, 'https://demoqa.com/alerts')
            click_time_alert.open()
            click_time_alert.remove_footer()
            click_time_alert.click_time_alert()
            alert_message = click_time_alert.switch_to_alert(driver)
            click_time_alert.accept_alert(driver)

            assert alert_message == 'This alert appeared after 5 seconds', \
                'Alert has not been opened or has shown another message'

        @allure.title('Confirm alert')
        def test_accept_confirmation_alert(self, driver):
            click_confirmation_alert = AlertsPage(driver, 'https://demoqa.com/alerts')
            click_confirmation_alert.open()
            click_confirmation_alert.remove_footer()
            click_confirmation_alert.click_confirmation_alert()
            click_confirmation_alert.switch_to_alert(driver)
            click_confirmation_alert.accept_alert(driver)
            alert_message = click_confirmation_alert.get_confirmation_alert_message()
            print(alert_message)

            assert alert_message == 'You selected Ok', 'Another message has been shown'

        @allure.title('Dismiss alert')
        def test_dismiss_confirmation_alert(self, driver):
            click_confirmation_alert = AlertsPage(driver, 'https://demoqa.com/alerts')
            click_confirmation_alert.open()
            click_confirmation_alert.remove_footer()
            click_confirmation_alert.click_confirmation_alert()
            click_confirmation_alert.switch_to_alert(driver)
            click_confirmation_alert.dismiss_alert(driver)
            alert_message = click_confirmation_alert.get_confirmation_alert_message()
            print(alert_message)

            assert alert_message == 'You selected Cancel', 'Another message has been shown'

        @allure.title('Send text value to alert')
        @pytest.mark.parametrize('alert_text', [
            'word',
            'sentence with spaces',
            'special characters !@#$%^&*()_+}{:"><',
            'longlonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglongword'
        ])
        def test_send_keys_to_alert(self, driver, alert_text):

            click_confirmation_alert = AlertsPage(driver, 'https://demoqa.com/alerts')
            click_confirmation_alert.open()
            click_confirmation_alert.remove_footer()
            click_confirmation_alert.click_prompt_alert()
            click_confirmation_alert.switch_to_alert(driver)
            click_confirmation_alert.send_keys_to_alert(driver, alert_text)
            click_confirmation_alert.accept_alert(driver)
            alert_message = click_confirmation_alert.get_prompt_alert_message()

            assert alert_message == f'You entered {alert_text}', 'Another message is expected'

    @allure.feature('Web page frames')
    class TestFrames:

        @allure.title('Check frame and its content')
        @pytest.mark.parametrize('frame, expected_width, expected_height', [
            ('large_frame', '500px', '350px'),
            ('small_frame', '100px', '100px')
        ])
        def test_frame_is_present(self, driver, frame, expected_width, expected_height):
            frames_page = FramesPage(driver, 'https://demoqa.com/frames')
            frames_page.open()
            frames_page.remove_footer()
            width, height, text = frames_page.check_frame(frame)

            assert width == expected_width, 'Another width of frame is expected'
            assert height == expected_height, 'Another height of frame is expected'
            assert text == 'This is a sample page', 'Another text of frame is expected'

    @allure.feature('Web page nested frames')
    class TestNestedFrames:

        @allure.title('Check parent and child frames and their content')
        def test_both_frames_are_present(self, driver):
            nested_frames_page = NestedFramesPage(driver, 'https://demoqa.com/nestedframes')
            nested_frames_page.open()
            nested_frames_page.remove_footer()
            parent_text, child_text = nested_frames_page.check_nested_frames()

            assert parent_text == 'Parent frame', 'Another text of parent frame is expected'
            assert child_text == 'Child Iframe', 'Another text of child frame is expected'

    @allure.feature('Modal dialogs')
    class TestModalDialogs:

        @allure.title('Click modal and check its content')
        @pytest.mark.parametrize('modal, expected_title, expected_text_length', [
            ('small', 'Small Modal', 47),
            ('large', 'Large Modal', 574)
        ])
        def test_modal_dialog(self, driver, modal, expected_title, expected_text_length):
            modal_dialogs_page = ModalDialogsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialogs_page.open()
            modal_dialogs_page.remove_footer()
            title, text_length = modal_dialogs_page.check_small_modal_dialog(modal)

            assert title == expected_title, 'Another modal dialog title is expected'
            assert text_length == expected_text_length, 'Another modal dialog text is expected'
