import random
import time
import re

from locators.interactions_page_locators import SortableLocators, SelectableLocators, ResizeableLocators, \
    DroppableLocators, DraggableLocators
from pages_actions.base_page import BasePage


class SortablePage(BasePage):

    locators = SortableLocators()

    def get_order_of_elements(self, elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    def change_order_of_elements(self, tab):

        tabs = {
            'list': {
                    'tab_name': self.locators.LIST_TAB,
                    'tab_elements': self.locators.LIST_ELEMENTS
                },
            'grid': {
                    'tab_name': self.locators.GRID_TAB,
                    'tab_elements': self.locators.GRID_ELEMENTS
                }
        }

        tab_name = tabs[tab]['tab_name']
        tab_elements = tabs[tab]['tab_elements']

        self.element_is_visible(tab_name).click()
        order_of_elements_before = self.get_order_of_elements(tab_elements)
        positions_list = random.sample(self.elements_are_visible(tab_elements), k = 2)
        start_position = positions_list[0]
        final_position = positions_list[1]
        self.action_drag_and_drop_to_element(start_position, final_position)
        order_of_elements_after = self.get_order_of_elements(tab_elements)
        return order_of_elements_before, order_of_elements_after, start_position, final_position


class SelectablePage(BasePage):

    locators = SelectableLocators()

    def select_active_elements(self, elements):
        elements_list = self.elements_are_visible(elements)
        random_number_of_elements = random.randint(1, len(elements_list))
        random_elements = random.sample(elements_list, random_number_of_elements)
        selected_elements = []
        for element in random_elements:
            element.click()
            selected_elements.append(element.text)
        return random_number_of_elements, selected_elements

    def select_and_check_elements(self, tab):

        elements_tabs = {
            'list': {
                    'tab_name': self.locators.LIST_TAB,
                    'tab_elements': self.locators.LIST_ELEMENT,
                    'tab_selected_elements': self.locators.LIST_SELECTED_ELEMENT
                },
            'grid': {
                    'tab_name': self.locators.GRID_TAB,
                    'tab_elements': self.locators.GRID_ELEMENT,
                    'tab_selected_elements': self.locators.GRID_SELECTED_ELEMENT
                }
        }

        self.element_is_visible(elements_tabs[tab]['tab_name']).click()
        amount_of_selected_elements, selected_elements = self.select_active_elements(elements_tabs[tab]['tab_elements'])
        clicked_elements = self.elements_are_visible(elements_tabs[tab]['tab_selected_elements'])
        active_elements = []
        for element in clicked_elements:
            active_elements.append(element.text)
        return amount_of_selected_elements, selected_elements, active_elements


class ResizeablePage(BasePage):

    locators = ResizeableLocators()

    def get_width_height(self, value_of_size):
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    def get_max_min_size(self, element):
        size = self.element_is_present(element)
        size_value = size.get_attribute('style')
        return size_value

    def change_resizeable_box(self, resizeable_element, max_x_coord, max_y_coord, min_x_coord, min_y_coord):

        resizeable_elements = {
            'resizable_box': {
                    'element': self.locators.RESIZEABLE_BOX,
                    'handle': self.locators.RESIZEABLE_BOX_HANDLE
                },
            'resizable': {
                    'element': self.locators.RESIZEABLE,
                    'handle': self.locators.RESIZEABLE_HANDLE
                }
        }

        initial_size = self.get_width_height(self.get_max_min_size(resizeable_elements[resizeable_element]['element']))
        self.action_drag_and_drop_by_offset(self.element_is_present(
            resizeable_elements[resizeable_element]['handle']), max_x_coord, max_y_coord)
        max_size = self.get_width_height(self.get_max_min_size(resizeable_elements[resizeable_element]['element']))
        self.action_drag_and_drop_by_offset(self.element_is_present(
            resizeable_elements[resizeable_element]['handle']), min_x_coord, min_y_coord)
        min_size = self.get_width_height(self.get_max_min_size(resizeable_elements[resizeable_element]['element']))
        return initial_size, max_size, min_size


class DroppablePage(BasePage):

    locators = DroppableLocators()

    def drop_simple_element(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_div = self.element_is_visible(self.locators.SIMPLE_DRAG_ME_ELEMENT)
        drop_div = self.element_is_visible(self.locators.SIMPLE_DRAG_ME_BOX)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        return drop_div.text

    def drop_element(self, element):

        elements = {
            'acceptable': self.locators.ACCEPTABLE_DRAG_ELEMENT,
            'not_acceptable': self.locators.NOT_ACCEPTABLE_DRAG_ELEMENT,
        }

        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        drag_element = self.element_is_visible(elements[element])
        drop_div = self.element_is_visible(self.locators.ACCEPT_DRAG_BOX)
        self.action_drag_and_drop_to_element(drag_element, drop_div)
        drop_box_text = drop_div.text
        return drop_box_text

    def drop_prevent_element(self):
        self.element_is_visible(self.locators.PREVENT_TAB).click()
        drag_div = self.element_is_visible(self.locators.PREVENT_DRAG_ELEMENT)
        not_greedy_inner_box = self.element_is_visible(self.locators.NOT_GREEDY_INNER_BOX)
        greedy_inner_box = self.element_is_visible(self.locators.GREEDY_INNER_BOX)
        self.action_drag_and_drop_to_element(drag_div, not_greedy_inner_box)
        text_not_greedy_box = self.element_is_visible(self.locators.NOT_GREEDY_DROP_BOX_TEXT).text
        text_not_greedy_inner_box = not_greedy_inner_box.text
        self.action_drag_and_drop_to_element(drag_div, greedy_inner_box)
        text_greedy_box = self.element_is_visible(self.locators.GREEDY_DROP_BOX_TEXT).text
        text_greedy_inner_box = greedy_inner_box.text
        return text_not_greedy_box, text_not_greedy_inner_box, text_greedy_box, text_greedy_inner_box

    def drop_will_revert_element(self, element):

        elements = {
            'will_revert': self.locators.WILL_REVERT_DRAG_ELEMENT,
            'will_not_revert': self.locators.NOT_REVERT_DRAG_ELEMENT
        }

        self.element_is_visible(self.locators.REVERT_TAB).click()
        element = self.element_is_visible(elements[element])
        drop_div = self.element_is_visible(self.locators.REVERT_DRAG_BOX)
        position_before_action = element.get_attribute('style')
        self.action_drag_and_drop_to_element(element, drop_div)
        time.sleep(1)
        position_after_action = element.get_attribute('style')
        return position_before_action, position_after_action


class DraggablePage(BasePage):

    locators = DraggableLocators()

    def drag_element_and_get_position(self, drag_element, x_coords, y_coords):
        self.action_drag_and_drop_by_offset(drag_element, x_coords, y_coords)
        time.sleep(2)
        position = drag_element.get_attribute('style')
        return position

    def get_drag_element_position(self, drag_element, x_coords, y_coords):
        position_before = self.drag_element_and_get_position(drag_element, x_coords, y_coords)
        position_after = self.drag_element_and_get_position(drag_element, x_coords, y_coords)
        return position_before, position_after

    def drag_simple_element(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_div = self.element_is_visible(self.locators.SIMPLE_DRAG_ME_ELEMENT)
        position_before, position_after = self.get_drag_element_position(drag_div,
                                                                         random.randint(0, 300), random.randint(0, 300))
        return position_before, position_after

    def get_top_position(self, positions):
        return re.findall(r'\d[0-9]|\d', positions.split(';')[2])

    def get_left_position(self, positions):
        return re.findall(r'\d[0-9]|\d', positions.split(';')[1])

    def drag_restricted_x_element(self, element):

        elements = {
            'x': self.locators.ONLY_X_ELEMENT,
            'y': self.locators.ONLY_Y_ELEMENT
        }

        self.element_is_visible(self.locators.AXIS_RESTRICTED_TAB).click()
        drag_div = self.element_is_visible(elements[element])
        position_before, position_after = self.get_drag_element_position(drag_div,
                                                                         random.randint(0, 99), random.randint(0, 99))
        top_x_before = self.get_top_position(position_before)
        top_x_after = self.get_top_position(position_after)
        left_x_before = self.get_left_position(position_before)
        left_x_after = self.get_left_position(position_after)
        return [top_x_before, top_x_after], [left_x_before, left_x_after]
