from selenium.webdriver.common.by import By


class BrowserWindowsLocators:

    NEW_TAB = (By.CSS_SELECTOR, 'button[id="tabButton"]')
    NEW_TAB_CONTENT = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')
    NEW_WINDOW = (By.CSS_SELECTOR, 'button[id="windowButton"]')


class AlertsLocators:

    SIMPLE_ALERT = (By.CSS_SELECTOR, 'button[id="alertButton"]')
    TIME_ALERT = (By.CSS_SELECTOR, 'button[id="timerAlertButton"]')
    CONFIRM_ALERT = (By.CSS_SELECTOR, 'button[id="confirmButton"]')
    CONFIRM_MESSAGE = (By.CSS_SELECTOR, 'span[id="confirmResult"]')
    PROMPT_ALERT = (By.CSS_SELECTOR, 'button[id="promtButton"]')
    PROMPT_MESSAGE = (By.CSS_SELECTOR, 'span[id="promptResult"]')


class FramesLocators:

    LARGE_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    SMALL_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame2"]')
    FRAME_TITLE = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')


class NestedFramesLocators:

    PARENT_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    PARENT_FRAME_TEXT = (By.CSS_SELECTOR, 'body')
    CHILD_FRAME = (By.CSS_SELECTOR, 'iframe[srcdoc="<p>Child Iframe</p>"]')
    CHILD_FRAME_TEXT = (By.CSS_SELECTOR, 'p')


class ModalDialogsLocators:

    SMALL_MODAL = (By.CSS_SELECTOR, 'button[id="showSmallModal"]')
    SMALL_MODAL_TITLE = (By.CSS_SELECTOR, 'div[id="example-modal-sizes-title-sm"]')
    SMALL_MODAL_TEXT = (By.CSS_SELECTOR, 'div[class="modal-body"]')
    SMALL_MODAL_CLOSE = (By.CSS_SELECTOR, 'button[id="closeSmallModal"]')
    LARGE_MODAL = (By.CSS_SELECTOR, 'button[id="showLargeModal"]')
    LARGE_MODAL_TITLE = (By.CSS_SELECTOR, 'div[id="example-modal-sizes-title-lg"]')
    LARGE_MODAL_TEXT = (By.CSS_SELECTOR, 'div[class="modal-body"] p')
    LARGE_MODAL_CLOSE = (By.CSS_SELECTOR, 'button[id="closeLargeModal"]')

