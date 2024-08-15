import allure
import pytest

from pages_actions.interactions_page import SortablePage, SelectablePage, ResizeablePage, DroppablePage, DraggablePage


@allure.suite('Interactions')
class TestInteractions:

    @allure.feature('Sortable elements')
    class TestSortable:

        @allure.title('Change and check elements order')
        @pytest.mark.parametrize('tab', [
            'list',
            'grid'
        ])
        def test_sortable_elements(self, driver, tab):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            sortable_page.remove_footer()
            order_of_elements_before, order_of_elements_after, start_position, final_position = (
                sortable_page.change_order_of_elements(tab))

            assert final_position != start_position, 'Chosen element has not been moved'
            assert order_of_elements_after != order_of_elements_before, 'Order of elements has not changed'

    @allure.feature('Selectable elements')
    class TestSelectable:

        @allure.title('Select and check selected elements')
        @pytest.mark.parametrize('tab', [
            'list',
            'grid'
        ])
        def test_selectable_elements(self, driver, tab):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            selectable_page.remove_footer()
            (amount_of_selected_elements,
             selected_elements, active_elements) = selectable_page.select_and_check_elements(tab)

            assert len(active_elements) == amount_of_selected_elements, \
                'Another amount of selected elements is expected'
            assert len(selected_elements) == amount_of_selected_elements, \
                'Another amount of active elements is expected'
            assert set(active_elements) == set(selected_elements), \
                'Selected and active elements lists contain different elements'

    @allure.feature('Resizeable elements')
    class TestResizeable:

        @allure.title('Resize elements and check their sizes')
        @pytest.mark.parametrize('resizable_element, max_x, max_y, min_x, min_y', [
            ('resizable_box', 100, 100, -50, -50),
            ('resizable', 10, 10, -50, -50)
        ])
        def test_resizeable_elements(self, driver, resizable_element, max_x, max_y, min_x, min_y):
            resizeable_page = ResizeablePage(driver, 'https://demoqa.com/resizable')
            resizeable_page.open()
            resizeable_page.remove_footer()
            initial_size, max_size, min_size = resizeable_page.change_resizeable_box(
                resizable_element, max_x, max_y, min_x, min_y)

            assert max_size != min_size, 'Sizes of element have not been changed'
            assert initial_size != max_size, 'Element could not change sizes to larger ones'
            assert initial_size != min_size, 'Element could not change sizes to smaller ones'

    @allure.feature('Droppable elements')
    class TestDroppable:

        @allure.title('Drop simple element')
        def test_simple_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            droppable_page.remove_footer()
            text = droppable_page.drop_simple_element()

            assert text == 'Dropped!', 'Drag me element has not been dropped'

        @allure.title('Check acceptability of element')
        @pytest.mark.parametrize('element, expected_drop_box_text', [
            ('acceptable', 'Dropped!'),
            ('not_acceptable', 'Drop here')
        ])
        def test_drag_acceptable_element(self, driver, element, expected_drop_box_text):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            droppable_page.remove_footer()
            drop_box_text = droppable_page.drop_element(element)

            assert drop_box_text == expected_drop_box_text, 'Another drop box text is expected'

        @allure.title('Check prevent propagation properties of element')
        def test_prevent_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            droppable_page.remove_footer()
            (text_not_greedy_box, text_not_greedy_inner_box,
             text_greedy_box, text_greedy_inner_box) = droppable_page.drop_prevent_element()

            assert text_not_greedy_box == text_not_greedy_inner_box, 'Not greedy boxes have different texts'
            assert text_greedy_box != text_greedy_inner_box, 'Greedy boxes do not have different texts'

        @allure.title('Check revert properties of will-revert-element')
        def test_will_revert_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            droppable_page.remove_footer()
            position_before_action, position_after_action = droppable_page.drop_will_revert_element('will_revert')

            assert position_after_action == 'position: relative; left: 0px; top: 0px;', 'Element has not been reverted'

        @allure.title('Check revert properties of will-not-revert-element')
        def test_will_not_revert_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            droppable_page.remove_footer()
            position_before_action, position_after_action = droppable_page.drop_will_revert_element('will_not_revert')

            assert position_after_action != position_before_action, 'Element has been reverted'

    @allure.feature('Draggable elements')
    class TestDraggable:

        @allure.title('Drag simple element')
        def test_drag_simple_element(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            draggable_page.remove_footer()
            position_before, position_after = draggable_page.drag_simple_element()

            assert position_after != position_before, 'Element has not moved.'

        @allure.title('Drag x restricted element')
        def test_drag_x_restricted_element(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            draggable_page.remove_footer()
            top_x, left_x = draggable_page.drag_restricted_x_element('x')

            assert top_x[0] == top_x[1], 'Element has moved on axis Y.'
            assert left_x[1] != left_x[0], 'Element has not moved on axis X.'

        @allure.title('Drag y restricted element')
        def test_drag_y_restricted_element(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            draggable_page.remove_footer()
            top_x, left_x = draggable_page.drag_restricted_x_element('y')

            assert left_x[0] == left_x[1], 'Element has moved on axis X.'
            assert top_x[1] != top_x[0], 'Element has not moved on axis Y.'
