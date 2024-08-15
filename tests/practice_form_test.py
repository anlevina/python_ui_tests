import allure

from pages.practice_form_page import PracticeFormPage


@allure.suite('Practice form page')
class TestPracticeForm:

    @allure.feature('Filling practice form fields')
    class TestFillPracticeFormFields:

        @allure.title('Fill all fields')
        def test_fill_all_practice_form_fields(self, driver):
            practice_form_page = PracticeFormPage(driver, 'https://demoqa.com/automation-practice-form')
            practice_form_page.open()
            practice_form_page.remove_footer()
            (first_name, last_name, email, gender, mobile, dob_before, dob_after, subjects, hobbies,
             current_address, state, city) = (practice_form_page.fill_all_fields())
            file_name = practice_form_page.upload_file()
            practice_form_page.submit()
            result_from_table = practice_form_page.form_result()
            practice_form_page.close()

            assert f'{first_name} {last_name}' == result_from_table[0], 'Another first or last name is expected'
            assert email == result_from_table[1], 'Another email is expected'
            assert gender == result_from_table[2], 'Another gender is expected'
            assert mobile == result_from_table[3], 'Another mobile is expected'
            assert dob_after != dob_before, 'Date of birth has not been changed or set.'
            assert subjects == result_from_table[5], 'Another subject is expected'
            assert hobbies == result_from_table[6], 'Another hobby is expected'
            assert file_name == result_from_table[7], 'File has not been uploaded'
            assert current_address == result_from_table[8], 'Another current address is expected'
            assert f'{state} {city}' == result_from_table[9], 'Another state or city is expected'

        @allure.title('Fill mandatory fields only')
        def test_fill_only_mandatory_practice_form_fields(self, driver):
            practice_form_page = PracticeFormPage(driver, 'https://demoqa.com/automation-practice-form')
            practice_form_page.open()
            practice_form_page.remove_footer()
            first_name, last_name, gender, mobile, dob_before, dob_after = practice_form_page.fill_only_mandatory_fields()
            practice_form_page.submit()
            result_from_table = practice_form_page.form_result()
            practice_form_page.close()

            assert f'{first_name} {last_name}' == result_from_table[0], 'Another first or last name is expected'
            assert gender == result_from_table[2], 'Another gender is expected'
            assert mobile == result_from_table[3], 'Another mobile is expected'
            assert dob_after != dob_before, 'Date of birth has not been changed or set.'


