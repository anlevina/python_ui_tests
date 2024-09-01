import allure
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    @allure.step('Remove browser page footer')
    def remove_footer(self):
        self.driver.execute_script('document.getElementsByTagName("footer")[0].remove();')
        self.driver.execute_script('document.getElementById("fixedban").style.display="none";')

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @allure.step('Open an url')
    def open(self):
        self.driver.get(self.url)

    @allure.step('Check that element is visible')
    def element_is_visible(self, locator, timeout=6):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Check that elements are visible')
    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    @allure.step('Check that element is present')
    def element_is_present(self, locator, timeout=6):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Check that elements are present')
    def elements_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    @allure.step('Check that element is not visible')
    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element(locator))

    @allure.step('Check that element is clickable')
    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step('Go to element on a page')
    def go_to_element(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Perform double click')
    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    @allure.step('Perform right click')
    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    @allure.step('Switch to a tab')
    def switch_to_tab(self, driver):
        self.driver.switch_to.window(self.driver.window_handles[1])
        url = self.driver.current_url
        return url

    @allure.step('Switch to a window')
    def switch_to_window(self, driver):
        self.driver.switch_to.window(self.driver.window_handles[1])
        url = self.driver.current_url
        return url

    @allure.step('Switch to alert')
    def switch_to_alert(self, driver):
        alert = self.driver.switch_to.alert
        return alert.text

    @allure.step('Accept alert')
    def accept_alert(self, driver):
        alert = self.driver.switch_to.alert
        alert.accept()

    @allure.step('Send a value to an alert')
    def send_keys_to_alert(self, driver, keys):
        alert = self.driver.switch_to.alert
        alert.send_keys(keys)

    @allure.step('Dismiss alert')
    def dismiss_alert(self, driver):
        alert = self.driver.switch_to.alert
        alert.dismiss()

    @allure.step('Drag and drop an element to given coordinates')
    def action_drag_and_drop_by_offset(self, element, x_coords, y_coords):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coords, y_coords)
        action.perform()

    @allure.step('Move to an element')
    def action_move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    @allure.step('Drag and drop an element to a different element')
    def action_drag_and_drop_to_element(self, from_item, to_item):
        action = ActionChains(self.driver)
        action.drag_and_drop(from_item, to_item)
        action.perform()