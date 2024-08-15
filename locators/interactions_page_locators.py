from selenium.webdriver.common.by import By


class SortableLocators:

    LIST_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    LIST_ELEMENTS = (By.CSS_SELECTOR, 'div[class="vertical-list-container mt-4"] '
                                      'div[class="list-group-item list-group-item-action"]')

    GRID_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    GRID_ELEMENTS = (By.CSS_SELECTOR, 'div[class="grid-container mt-4"] '
                                      'div[class="list-group-item list-group-item-action"]')


class SelectableLocators:

    LIST_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    LIST_ELEMENT = (By.CSS_SELECTOR, 'li[class="mt-2 list-group-item list-group-item-action"]')
    LIST_SELECTED_ELEMENT = (By.CSS_SELECTOR, 'li[class="mt-2 list-group-item active list-group-item-action"]')

    GRID_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    GRID_ELEMENT = (By.CSS_SELECTOR, 'li[class="list-group-item list-group-item-action"]')
    GRID_SELECTED_ELEMENT = (By.CSS_SELECTOR, 'li[class="list-group-item active list-group-item-action"]')


class ResizeableLocators:

    RESIZEABLE_BOX_HANDLE = (By.CSS_SELECTOR, 'div[class="constraint-area"] '
                                              'span[class="react-resizable-handle react-resizable-handle-se"]')
    RESIZEABLE_BOX = (By.CSS_SELECTOR, 'div[id="resizableBoxWithRestriction"]')
    RESIZEABLE_HANDLE = (By.CSS_SELECTOR, 'div[id="resizable"] '
                                          'span[class="react-resizable-handle react-resizable-handle-se"]')
    RESIZEABLE = (By.CSS_SELECTOR, 'div[id="resizable"]')


class DroppableLocators:

    SIMPLE_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-simple"]')
    SIMPLE_DRAG_ME_ELEMENT = (By.CSS_SELECTOR, 'div[id="draggable"]')
    SIMPLE_DRAG_ME_BOX = (By.CSS_SELECTOR, '#simpleDropContainer #droppable')

    ACCEPT_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-accept"]')
    ACCEPTABLE_DRAG_ELEMENT = (By.CSS_SELECTOR, 'div[id="acceptable"]')
    NOT_ACCEPTABLE_DRAG_ELEMENT = (By.CSS_SELECTOR, 'div[id="notAcceptable"]')
    ACCEPT_DRAG_BOX = (By.CSS_SELECTOR, '#acceptDropContainer #droppable')

    PREVENT_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-preventPropogation"]')
    PREVENT_DRAG_ELEMENT = (By.CSS_SELECTOR, 'div[id="dragBox"]')
    NOT_GREEDY_DROP_BOX_TEXT = (By.CSS_SELECTOR, 'div[id="notGreedyDropBox"] p:nth-child(1)')
    NOT_GREEDY_INNER_BOX = (By.CSS_SELECTOR, 'div[id="notGreedyInnerDropBox"]')
    GREEDY_DROP_BOX_TEXT = (By.CSS_SELECTOR, 'div[id="greedyDropBox"] p:nth-child(1)')
    GREEDY_INNER_BOX = (By.CSS_SELECTOR, 'div[id="greedyDropBoxInner"]')

    REVERT_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-revertable"]')
    WILL_REVERT_DRAG_ELEMENT = (By.CSS_SELECTOR, 'div[id="revertable"]')
    NOT_REVERT_DRAG_ELEMENT = (By.CSS_SELECTOR, 'div[id="notRevertable"]')
    REVERT_DRAG_BOX = (By.CSS_SELECTOR, '#revertableDropContainer #droppable')


class DraggableLocators:

    SIMPLE_TAB = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-simple"]')
    SIMPLE_DRAG_ME_ELEMENT = (By.CSS_SELECTOR, 'div[id="dragBox"]')

    AXIS_RESTRICTED_TAB = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-axisRestriction"]')
    ONLY_X_ELEMENT = (By.CSS_SELECTOR, 'div[id="restrictedX"]')
    ONLY_Y_ELEMENT = (By.CSS_SELECTOR, 'div[id="restrictedY"]')

    CONTAINER_RESTRICTED_TAB = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-containerRestriction"]')
    CONTAINMENT_WRAPPER = (By.CSS_SELECTOR, 'div[id="containmentWrapper"]')
    WRAPPER_DRAG_ELEMENT = (By.CSS_SELECTOR,
                            'div[class="draggable ui-widget-content ui-draggable ui-draggable-handle"]')
    DRAGGABLE_WIDGET = (By.CSS_SELECTOR, 'div[class="draggable ui-widget-content m-3"]')
    WIDGET_DRAG_ELEMENT = (By.CSS_SELECTOR, 'span[class="ui-widget-header ui-draggable ui-draggable-handle"]')



