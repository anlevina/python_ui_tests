from selenium.webdriver.common.by import By


class AccordianLocators:

    FIRST_SECTION = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    FIRST_SECTION_TEXT = (By.CSS_SELECTOR, 'div[id="section1Content"]')
    SECOND_SECTION = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    SECOND_SECTION_TEXT = (By.CSS_SELECTOR, 'div[id="section2Content"] p')
    THIRD_SECTION = (By.CSS_SELECTOR, 'div[id="section3Heading"]')
    THIRD_SECTION_TEXT = (By.CSS_SELECTOR, 'div[id="section3Content"] p')


class AutocompleteLocators:

    MULTIPLE_COLOR_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
    MULTIPLE_COLOR_BOX = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    MULTIPLE_COLOR_REMOVE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"] svg path')
    SINGLE_COLOR_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')
    SINGLE_COLOR_VALUE = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')


class DatePickerLocators:

    DATE_INPUT = (By.CSS_SELECTOR, 'input[id="datePickerMonthYearInput"]')
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]')

    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, 'input[id="dateAndTimePickerInput"]')
    DATE_AND_TIME_SELECT_MONTH = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-read-view"]')
    DATE_AND_TIME_SELECT_MONTH_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-option"]')
    DATE_AND_TIME_SELECT_YEAR_LIST = (By.CSS_SELECTOR, 'div[class^="react-datepicker__year-option"]')
    DATE_AND_TIME_SELECT_YEAR = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-read-view"]')
    DATE_AND_TIME_SELECT_TIME_LIST = (By.CSS_SELECTOR, 'li[class="react-datepicker__time-list-item "]')
    PREVIOUS_YEARS = (By.CSS_SELECTOR, 'a[class="react-datepicker__navigation react-datepicker__navigation--years react-datepicker__navigation--years-previous"]')
    UPCOMING_YEARS = (By.CSS_SELECTOR, 'a[class="react-datepicker__navigation react-datepicker__navigation--years react-datepicker__navigation--years-upcoming"]')


class SliderLocators:

    SLIDER_VALUE_INPUT = (By.CSS_SELECTOR, 'input[id="sliderValue"]')
    SLIDER_BAR_INPUT = (By.CSS_SELECTOR, 'input[class="range-slider range-slider--primary"]')


class ProgressBarLocators:

    PROGRESS_BAR_VALUE = (By.CSS_SELECTOR, 'div[class="progress-bar bg-info"]')
    START_STOP_BUTTON = (By.CSS_SELECTOR, 'button[id="startStopButton"]')


class TabsLocators:

    TAB_WHAT = (By.CSS_SELECTOR, 'a[id="demo-tab-what"]')
    TAB_WHAT_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-what"]')
    TAB_ORIGIN = (By.CSS_SELECTOR, 'a[id="demo-tab-origin"]')
    TAB_ORIGIN_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-origin"]')
    TAB_USE = (By.CSS_SELECTOR, 'a[id="demo-tab-use"]')
    TAB_USE_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-use"]')


class TooltipsLocators:

    BUTTON = (By.CSS_SELECTOR, 'button[id="toolTipButton"]')
    BUTTON_TOOLTIP = (By.CSS_SELECTOR, 'button[aria-describedby="buttonToolTip"]')
    FIELD = (By.CSS_SELECTOR, 'input[id="toolTipTextField"]')
    FIELD_TOOLTIP = (By.CSS_SELECTOR, 'input[aria-describedby="textFieldToolTip"]')
    WORD = (By.XPATH, '//*[.="Contrary"]')
    WORD_TOOLTIP = (By.CSS_SELECTOR, 'a[aria-describedby="contraryTexToolTip"]')
    NUMBER = (By.XPATH, '//*[.="1.10.32"]')
    NUMBER_TOOLTIP = (By.CSS_SELECTOR, 'a[aria-describedby="sectionToolTip"]')

    TOOLTIPS_TEXT = (By.CSS_SELECTOR, 'div[class="tooltip-inner"]')


class MenuLocators:

    MENU_ITEMS_LIST = (By.CSS_SELECTOR, 'ul[id="nav"] li a')
