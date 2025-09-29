import unittest

from idrobo_lab.basic_image_processing import Processing
from nionswift_plugin.basic_image_processing_ui import MenuItem

from nion.swift import Facade


class TestLibrary(unittest.TestCase):

    def setUp(self) -> None:
        """Common code for all tests can go here."""
        pass

    def tearDown(self) -> None:
        """Common code for all tests can go here."""
        pass

    def test_menu_item_name(self) -> None:
        api = Facade.get_api("~1.0", "~1.0")
        self.assertEqual("cookiecutter_menu", MenuItem.MenuItemDelegate(api).menu_id)
