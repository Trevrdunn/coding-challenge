from unittest import TestCase
from shapes_library.shapes_package.shapes_module import Circle
from shapes_library.shapes_package.shapes_module import Rectangle


class CircleTests(TestCase):
    """
    Contains all unit tests for the shapes_module.Circle class
    """
    def test_circle_area_returns_correct_result_with_valid_radius(self):
        """
        Tests that a Circle object with a radius > 0 returns the correct area
        """
        mock_radius = 5.0
        expected_area = 78.54
        mock_circle = Circle(radius=mock_radius)
        self.assertEqual(mock_circle.area(), expected_area)

    def test_circle_area_raises_ValueError_with_negative_radius(self):
        """
        Test that a Cicle object with a negative radius raises a ValueError
        """
        with self.assertRaises(ValueError):
            mock_circle = Circle(radius=-1.0)


class RectangleTests(TestCase):
    """
    Contains all the unit tests for the shapes_module.Rectangle class
    """
    def test_rectangle_area_returns_correct_result_with_valid_height_and_width(self):
        """
        Tests that a Rectangle object with a height > 0 and a width > 0 returns the correct area
        """
        mock_height, mock_width = 10., 10.
        expected_area = 100.
        mock_rectangle = Rectangle(height=mock_height, width=mock_width)
        self.assertEqual(mock_rectangle.area(), expected_area)


