import random
import time

import allure
import pytest

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, DifferentClicksPage, \
    LinksPage, DownloadUploadPage, DynamicPropertiesPage


@allure.suite('Elements page')
class TestElements:

    @allure.feature('Text box')
    class TestTextBox:

        @allure.title('Fill text box fields')
        def test_fill_text_boxes(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            text_box_page.remove_footer()
            input_data = text_box_page.fill_all_fields()
            output_data = text_box_page.check_filled_form()

            assert output_data[0] == input_data[0], 'Full name is different.'
            assert output_data[1] == input_data[1], 'Email is different.'
            assert output_data[2] == input_data[2], 'Current address is different.'
            assert output_data[3] == input_data[3], 'Permanent address is different.'

    @allure.feature('Check box')
    class TestCheckBox:

        @allure.title('Enable random check boxes')
        def test_enable_check_boxes(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.remove_footer()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkboxes = check_box_page.get_checked_checkboxes()
            output_items = check_box_page.get_output_results()

            assert input_checkboxes == output_items, 'Lists of input and output items are different.'

    @allure.feature('Radio buttons')
    class TestRadioButton:

        @allure.title('Click radio buttons')
        @pytest.mark.parametrize('button, expected_text', [
            ('yes', 'Yes'),
            ('impressive', 'Impressive'),
        ])
        def test_click_radio_buttons(self, driver, button, expected_text):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.remove_footer()
            radio_button_page.click_radio_button(button)
            output = radio_button_page.get_output_result()

            assert output == expected_text, f'Another text is expected'

    @allure.feature('Web tables')
    class TestWebTables:

        @allure.title('Add new person to web table')
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            web_table_page.remove_footer()
            web_table_page.click_add_button()
            new_person = web_table_page.fill_person_fields()
            web_table_page.click_submit_button()
            table_results = web_table_page.click_added_person()

            assert new_person in table_results, 'Created person does not exist in table'

        @allure.title('Add new person and search for it in web table')
        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            web_table_page.remove_footer()
            web_table_page.click_add_button()
            key_word = web_table_page.fill_person_fields()[random.randint(1,5)]
            web_table_page.click_submit_button()
            web_table_page.search_person_in_web_table(key_word)
            table_results = web_table_page.check_person_in_web_table()

            assert key_word in table_results, 'Created person has not been found in table'

        @allure.title('Add new person and update it in web table')
        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            web_table_page.remove_footer()
            web_table_page.click_add_button()
            lastname = web_table_page.fill_person_fields()[1]
            web_table_page.click_submit_button()
            web_table_page.search_person_in_web_table(lastname)
            web_table_page.click_edit_button()
            age = web_table_page.update_person()
            web_table_page.click_submit_button()
            added_person_row = web_table_page.check_person_in_web_table()

            assert age in added_person_row, 'Person has not been changed'

        @allure.title('Add new person and delete it from web table')
        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            web_table_page.remove_footer()
            web_table_page.click_add_button()
            lastname = web_table_page.fill_person_fields()[1]
            web_table_page.click_submit_button()
            web_table_page.search_person_in_web_table(lastname)
            web_table_page.click_delete_button()
            no_rows_found = web_table_page.table_is_empty()

            assert no_rows_found == 'No rows found', 'Person has not been deleted'

        @allure.title('Change amount of rows per page on web table page')
        def test_web_table_change_rows_per_page(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            web_table_page.remove_footer()
            count = web_table_page.change_amount_of_rows()

            assert count == [5, 10, 20, 25, 50, 100], \
                'Number of rows in the table has not been changed or has changed incorrectly'

    @allure.feature('Different types of clicks')
    class TestDifferentClicks:

        @allure.title('Perform double click')
        def test_double_click(self, driver):
            different_clicks_page = DifferentClicksPage(driver, 'https://demoqa.com/buttons')
            different_clicks_page.open()
            different_clicks_page.remove_footer()
            different_clicks_page.double_click()
            double_click_message = different_clicks_page.double_click_message()

            assert double_click_message == 'You have done a double click'

        @allure.title('Perform right click')
        def test_right_click(self, driver):
            different_clicks_page = DifferentClicksPage(driver, 'https://demoqa.com/buttons')
            different_clicks_page.open()
            different_clicks_page.remove_footer()
            different_clicks_page.right_click()
            right_click_message = different_clicks_page.right_click_message()

            assert right_click_message == 'You have done a right click'

        @allure.title('Perform dynamic click')
        def test_single_click(self, driver):
            different_clicks_page = DifferentClicksPage(driver, 'https://demoqa.com/buttons')
            different_clicks_page.open()
            different_clicks_page.remove_footer()
            different_clicks_page.single_click(driver)
            single_click_message = different_clicks_page.single_click_message()

            assert single_click_message == 'You have done a dynamic click'

    @allure.feature('Normal and broken links')
    class TestLinks:

        @allure.title('Click simple link which opens in new tab')
        def test_simple_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            links_page.remove_footer()
            link_href, url = links_page.check_new_tab_simple_link()

            assert link_href == url, 'Another link in a new tab is expected'

        @allure.title('Click broken links with not 200 OK response')
        @pytest.mark.parametrize('link, expected_status_code', [
            ('created', 201),
            ('no_content', 204),
            ('moved', 301),
            ('bad_request', 400),
            ('unauthorized', 401),
            ('forbidden', 403),
            ('not_found', 404)
        ])
        def test_broken_link(self, driver, link, expected_status_code):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            links_page.remove_footer()
            response_code = links_page.check_broken_link(link)

            assert response_code == expected_status_code, 'Another response code is expected'

    @allure.feature('Downloading and uploading files')
    class TestDownloadUploadFile:

        @allure.title('Success file upload')
        def test_upload_file_success(self, driver):
            download_upload_page = DownloadUploadPage(driver, 'https://demoqa.com/upload-download')
            download_upload_page.open()
            download_upload_page.remove_footer()
            path = download_upload_page.upload_file()
            file_path = download_upload_page.check_uploaded_file()

            assert path == file_path, 'The file has not been uploaded'

        @allure.title('Success file download')
        def test_download_file_success(self, driver):
            download_upload_page = DownloadUploadPage(driver, 'https://demoqa.com/upload-download')
            download_upload_page.open()
            download_upload_page.remove_footer()
            check = download_upload_page.download_file()

            assert check is True, 'The file has not been downloaded'

    @allure.feature('Dynamic properties')
    class TestDynamicProperties:

        @allure.title('Click button that is clickable after 5 seconds')
        def test_enabled_after_5_seconds_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            dynamic_properties_page.remove_footer()
            click_check = dynamic_properties_page.check_enabled_after_button_is_clickable()

            assert click_check is True

        @allure.title('Check color of button whose color is changed after 5 seconds')
        def test_color_change_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            dynamic_properties_page.remove_footer()
            color_before = dynamic_properties_page.check_color_change_button_color()
            time.sleep(6)
            color_after = dynamic_properties_page.check_color_change_button_color()

            assert color_before != color_after, 'Color of the button has not changed'
            assert color_after == 'rgba(220, 53, 69, 1)', 'The color has changed to a wrong value'

        @allure.title('Click button that is visible after 5 seconds')
        def test_visible_after_5_seconds_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            dynamic_properties_page.remove_footer()
            appear_check = dynamic_properties_page.check_visible_after_button_is_shown()

            assert appear_check is True
