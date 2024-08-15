import allure
import pytest

from pages_actions.widgets_page import AccordianPage, AutocompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    TooltipsPage, MenuPage


@allure.suite('Widgets')
class TestWidgets:

    @allure.feature('Accodrian')
    class TestAccordian:

        @allure.title('Click accordian and check its content')
        @pytest.mark.parametrize('accordian_number, expected_header, expected_text_length', [
            ('first', 'What is Lorem Ipsum?', 574),
            ('third', 'Why do we use it?', 613)
        ])
        def test_accordian_with_one_paragraph(self, driver, accordian_number, expected_header, expected_text_length):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            accordian_page.remove_footer()
            accordian_header, text_len = accordian_page.check_accordian_with_one_paragraph(accordian_number)

            assert accordian_header == expected_header, 'Another header value is expected'
            assert text_len == expected_text_length, 'Another content text is expected'

        @allure.title('Click accordian and check its content which contains several paragraphs')
        def test_accordian_with_several_paragraphs(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            accordian_page.remove_footer()
            accordian_header, text_len = accordian_page.check_accordian_with_several_paragraphs()

            assert accordian_header == 'Where does it come from?', 'Another header value is expected'
            assert text_len == 1058, 'Another content text is expected'

    @allure.feature('Autocomplete')
    class TestAutocomplete:

        @allure.title('Enter several colors')
        def test_multiple_colors_autocomplete(self, driver):

            autocomplete_page = AutocompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.remove_footer()
            generated_colors = autocomplete_page.add_colors_to_multiple_autocomplete()
            colors_after_input = autocomplete_page.check_color_in_multiple_input()
            colors_before, colors_after = autocomplete_page.remove_value_from_multiple_color_field()

            assert colors_after_input == generated_colors, \
                'Before and after colors lists contain different elements'
            assert colors_before != colors_after-1, 'More or less than 1 color were removed'

        @allure.title('Enter single color')
        def test_single_color_autocomplete(self, driver):

            autocomplete_page = AutocompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.remove_footer()
            color = autocomplete_page.add_color_to_single_input()
            result_color = autocomplete_page.check_single_color()

            assert result_color == color, 'Input and result colors lists contain different elements'

    @allure.feature('Date and time picker')
    class TestDatePicker:

        @allure.title('Set date via web calender widget')
        def test_set_date(self, driver):
            datepicker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            datepicker_page.open()
            datepicker_page.remove_footer()
            date_before, date_after = datepicker_page.set_date()

            assert date_after != date_before, 'Date has not been set'

        @allure.title('Set date and time via web calender widget')
        def test_set_date_and_time(self, driver):
            datepicker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            datepicker_page.open()
            datepicker_page.remove_footer()
            date_before, date_after = datepicker_page.set_date_and_time()

            assert date_after != date_before, 'Date and time have not been set'

    @allure.feature('Slider')
    class TestSlider:

        @allure.title('Move slider')
        def test_move_slider(self, driver):
            slider_page = SliderPage(driver, 'https://demoqa.com/slider')
            slider_page.open()
            slider_page.remove_footer()
            slider_value_before = slider_page.check_slider_value()
            slider_page.move_slider()
            slider_value_after = slider_page.check_slider_value()

            assert slider_value_after != slider_value_before, 'Slider has not been moved'

    @allure.feature('Progress bar')
    class TestProgressBar:

        @allure.title('Click and stop progress bar')
        def test_progress_bar(self, driver):
            progress_bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar_page.open()
            progress_bar_page.remove_footer()
            progress_bar_page.click_start_stop_button()
            progress_bar_value_after = progress_bar_page.check_progress_bar_value()

            assert progress_bar_value_after != '0%', 'Progress bar value has not changed'

    @allure.feature('Tabs')
    class TestTabs:

        @allure.title('Click tabs and check their content')
        @pytest.mark.parametrize('tab, expected_tab_name, expected_content_length', [
            ('what', 'What', 574),
            ('origin', 'Origin', 1059),
            ('use', 'Use', 613)
        ])
        def test_click_tabs(self, driver, tab, expected_tab_name, expected_content_length):
            tabs_page = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs_page.open()
            tabs_page.remove_footer()
            tab_name, tab_content_len = tabs_page.check_tabs(tab)

            assert tab_name == expected_tab_name, 'Tab name has not been shown'
            assert tab_content_len == expected_content_length, 'Another tab content is expected'

    @allure.feature('Tooltips')
    class TestTooltips:

        @allure.title('Hover tooltips and check their content')
        @pytest.mark.parametrize('tooltip, expected_tooltip_text', [
            ('button', 'You hovered over the Button'),
            ('field', 'You hovered over the text field'),
            ('word', 'You hovered over the Contrary'),
            ('number', 'You hovered over the 1.10.32'),
        ])
        def test_tooltips(self, driver, tooltip, expected_tooltip_text):
            tooltips_page = TooltipsPage(driver, 'https://demoqa.com/tool-tips')
            tooltips_page.open()
            tooltips_page.remove_footer()
            tooltip_text = tooltips_page.check_tooltip_text_by_element(tooltip)

            assert tooltip_text == expected_tooltip_text, 'Another tooltip text is expected'

    @allure.feature('Menu')
    class TestMenu:

        @allure.title('Check menu elements')
        def test_tooltips(self, driver):
            menu_page = MenuPage(driver, 'https://demoqa.com/menu')
            menu_page.open()
            menu_page.remove_footer()
            menu_items = menu_page.check_menu_items()

            assert len(menu_items) == 8, 'Another amount of menu items is expected'


