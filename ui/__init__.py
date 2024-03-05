from .base_ui import Ui_MainWindow
from .box import Box
from .lcd import Lcd

import os
import json
from constants import *

class Ui:
    def __init__(self, MainWindow):
        self.MainWindow = MainWindow

        with open(os.path.join(APP_DIR, 'ui.json'), 'r') as f:
            self.config = json.loads(f.read())

        for element in self.config:
            self.processElement(element, self.MainWindow.centralwidget, self.MainWindow.gridLayout_2)

    def processElement(self, properties, parent, parent_grid):
        element_classes = {
            'box': Box,
            'lcd': Lcd
        }
        element = element_classes[properties['type']](self.MainWindow, parent, parent_grid, properties)

        if 'content' in properties:
            for sub_element in properties['content']:
                self.processElement(sub_element, element.element, element.grid)

