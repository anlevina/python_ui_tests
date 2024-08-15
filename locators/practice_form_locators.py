import random

from selenium.webdriver.common.by import By


class PracticeFormPageLocators:

    FIRST_NAME = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    RANDOM_GENDER = (By.CSS_SELECTOR,
                     f'label[class="custom-control-label"][for="gender-radio-{random.randint(1, 3)}"]')
    # GENDER_MALE = (By.CSS_SELECTOR, 'label[class="custom-control-label"][for="gender-radio-1"]')
    # GENDER_FEMALE = (By.CSS_SELECTOR, 'label[class="custom-control-label"][for="gender-radio-2"]')
    # GENDER_OTHER = (By.CSS_SELECTOR, 'label[class="custom-control-label"][for="gender-radio-3"]')
    MOBILE = (By.CSS_SELECTOR, 'input[id="userNumber"]')
    DATE_OF_BIRTH = (By.CSS_SELECTOR, 'input[id="dateOfBirthInput"]')
    YEAR_DROPDOWN = (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')
    YEAR_LIST = (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"] option[value]')
    MONTH_DROPDOWN = (By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
    MONTH_LIST = (By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"] option[value]')
    DAYS_LIST = (By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]')
    SUBJECTS_FIELD = (By.CSS_SELECTOR, 'input[id="subjectsInput"]')
    SUBJECTS_ELEMENTS = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue subjects-auto-complete__multi-value"]')
    HOBBY_SPORTS = (By.CSS_SELECTOR, 'label[class="custom-control-label"][for="hobbies-checkbox-1"]')
    HOBBY_READING = (By.CSS_SELECTOR, 'label[class="custom-control-label"][for="hobbies-checkbox-2"]')
    HOBBY_MUSIC = (By.CSS_SELECTOR, 'label[class="custom-control-label"][for="hobbies-checkbox-3"]')
    UPLOAD_PICTURE = (By.CSS_SELECTOR, 'input[id="uploadPicture"]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    SELECT_STATE = (By.CSS_SELECTOR, 'div[id="state"]')
    SELECT_CITY = (By.CSS_SELECTOR, 'div[id="city"]')
    STATE_AND_CITY_FIELDS = (By.CSS_SELECTOR, 'div[class=" css-1uccc91-singleValue"]')

    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')
    CLOSE = (By.CSS_SELECTOR, 'button[id="closeLargeModal"]')

    RESULT_TABLE = (By.XPATH, '//div[@class="table-responsive"]//td[2]')
