from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    FULL_NAME = (By.CSS_SELECTOR, 'input[id="userName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="permanentAddress"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')


class CheckBoxPageLocators:

    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, 'button[title="Expand all"]')
    ITEM_LIST = (By.CSS_SELECTOR, 'span[class="rct-title"]')
    CHECKED_ITEMS = (By.CSS_SELECTOR, 'svg[class="rct-icon rct-icon-check"]')
    ITEM_TITLE = './/ancestor::span[@class="rct-text"]'

    OUTPUT_RESULT = (By.CSS_SELECTOR, 'span[class="text-success"]')


class RadioButtonPageLocators:

    YES_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="yesRadio"]')
    IMPRESSIVE_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="impressiveRadio"]')
    NO_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="noRadio"]')

    OUTPUT_RESULT = (By.CSS_SELECTOR, 'span[class="text-success"]')


class WebPageLocators:

    ADD_BUTTON = (By.CSS_SELECTOR, 'button[id="addNewRecordButton"]')
    FIRST_NAME = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    AGE = (By.CSS_SELECTOR, 'input[id="age"]')
    SALARY = (By.CSS_SELECTOR, 'input[id="salary"]')
    DEPARTMENT = (By.CSS_SELECTOR, 'input[id="department"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[id="submit"]')

    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, 'div[class="rt-tr-group"]')

    SEARCH_FIELD = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
    EDIT_BUTTON = (By.CSS_SELECTOR, 'span[title="Edit"]')
    NO_ROWS_FOUND = (By.CSS_SELECTOR, 'div[class="rt-noData"]')
    ROWS_AMOUNT = (By.CSS_SELECTOR, 'select[aria-label="rows per page"]')
    PARENT_ROW = './/ancestor::div[@class="rt-tr-group"]'


class DifferentClicksLocators:

    DOUBLE_CLICK = (By.CSS_SELECTOR, 'button[id="doubleClickBtn"]')
    RIGHT_CLICK = (By.CSS_SELECTOR, 'button[id="rightClickBtn"]')
    SINGLE_CLICK = './/div[3]/button'

    DOUBLE_CLICK_MESSAGE = (By.CSS_SELECTOR, 'p[id="doubleClickMessage"]')
    RIGHT_CLICK_MESSAGE = (By.CSS_SELECTOR, 'p[id="rightClickMessage"]')
    SINGLE_CLICK_MESSAGE = (By.CSS_SELECTOR, 'p[id="dynamicClickMessage"]')


class LinksLocators:

    SIMPLE_LINK = (By.CSS_SELECTOR, 'a[id="simpleLink"]')
    DYNAMIC_LINK = (By.CSS_SELECTOR, 'a[id="dynamicLink"]')

    CREATED = (By.CSS_SELECTOR, 'a[id="created"]')
    NO_CONTENT = (By.CSS_SELECTOR, 'a[id="no-content"]')
    MOVED = (By.CSS_SELECTOR, 'a[id="moved"]')
    BAD_REQUEST = (By.CSS_SELECTOR, 'a[id="bad-request"]')
    UNAUTHORIZED = (By.CSS_SELECTOR, 'a[id="unauthorized"]')
    FORBIDDEN = (By.CSS_SELECTOR, 'a[id="forbidden"]')
    NOT_FOUND = (By.CSS_SELECTOR, 'a[id="invalid-url"]')


class DownloadUploadLocators:

    DOWNLOAD_FILE = (By.CSS_SELECTOR, 'a[id="downloadButton"]')
    UPLOAD_FILE = (By.CSS_SELECTOR, 'input[id="uploadFile"]')
    UPLOADED_FILE_PATH = (By.CSS_SELECTOR, 'p[id="uploadedFilePath"]')


class DynamicPropertiesLocators:

    ENABLED_AFTER = (By.CSS_SELECTOR, 'button[id="enableAfter"]')
    COLOR_CHANGE = (By.CSS_SELECTOR, 'button[id="colorChange"]')
    VISIBLE_AFTER = (By.CSS_SELECTOR, 'button[id="visibleAfter"]')


