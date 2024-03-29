import unittest

# Import student code. Replace 'asgn9_1' with name of student script.
from shapes import Shape, Ellipse, Circle, Rectangle, Square

class TestExamples(unittest.TestCase):

    # Shape - Example
    def test_shape_example(self):
        # Create Shape
        test_shape = Shape("test_id")
        actual = isinstance(test_shape, Shape)
        expected = True
        self.assertEqual(actual, expected, \
            f"example/Shape: Shape class or constructor method did not work properly.")
    
    def test_shape_get_id_example(self):
        test_shape = Shape("test_id")
        actual = test_shape.get_id()
        expected = "test_id"
        self.assertEqual(actual, expected, \
            f"example/Shape/get_id: Method did not work. Expected '{expected}', but found '{actual}'.")

    def test_ellipse_example(self):
        test_ellipse = Ellipse("test_id_e", 5, 4)
        actual = isinstance(test_ellipse, Ellipse) and isinstance(test_ellipse, Shape)
        expected = True
        self.assertEqual(actual, expected, \
            f"example/Ellipse: Ellipse class or constructor method did not work properly, \
                or did not derive from Shape as required.")

    def test_ellipse_get_area_example(self):
        test_ellipse = Ellipse("test_id_e", 5, 4)
        actual = test_ellipse.get_area()
        expected = 62.83185307179586
        self.assertAlmostEqual(actual, expected, 0, \
            f"example/Ellipse/get_area: Method did not work. Expected {expected}, but found {actual}.")

    def test_ellipse_get_perimeter_example(self):
        test_ellipse = Ellipse("test_id_e", 5, 4)
        actual = test_ellipse.get_perimeter()
        expected = None
        self.assertAlmostEqual(actual, expected, \
            f"example/Ellipse/get_perimeter: Method did not work. Expected {expected}, but found {actual}.")

    def test_circle_example(self):
        test_circle = Circle("test_id_c", 4)
        actual = isinstance(test_circle, Circle) and isinstance(test_circle, Ellipse) \
            and isinstance(test_circle, Shape)
        expected = True
        self.assertEqual(actual, expected, \
            f"example/Circle: Circle class or constructor method did not work properly, \
                or did not derive from Ellipse as required.")

    def test_circle_get_area_example(self):
        test_circle = Circle("test_id_c", 4)
        actual = test_circle.get_area()
        expected = 50.26548245743669
        self.assertAlmostEqual(actual, expected, 0, \
            f"example/Circle/get_area: Method did not work. Expected {expected}, but found {actual}.")
    
    def test_circle_get_perimeter_example(self):
        test_circle = Circle("test_id_c", 4)
        actual = test_circle.get_perimeter()
        expected = 25.132741228718345
        self.assertAlmostEqual(actual, expected, 0, \
            f"example/Circle/get_perimeter: Method did not work. Expected {expected}, but found {actual}.")

    def test_rectangle_example(self):
        test_rect = Rectangle("test_id_r", 4, 5)
        actual = isinstance(test_rect, Rectangle) and isinstance(test_rect, Shape)
        expected = True
        self.assertEqual(actual, expected, \
            f"example/Rectangle: Rectangle class or constructor method did not work properly, \
                or did not derive from Shape as required.")

    def test_rectangle_get_area_example(self):
        test_rect = Rectangle("test_id_r", 5, 4)
        actual = test_rect.get_area()
        expected = 20
        self.assertEqual(actual, expected, \
            f"example/Rectangle/get_area: Method did not work. Expected {expected}, but found {actual}.")

    def test_rectangle_get_perimeter_example(self):
        test_rect = Rectangle("test_id_r", 5, 4)
        actual = test_rect.get_perimeter()
        expected = 18
        self.assertEqual(actual, expected, \
            f"example/Rectangle/get_perimeter: Method did not work. Expected {expected}, but found {actual}.")

    def test_square_example(self):
        test_square = Square("test_id_s", 4)
        actual = isinstance(test_square, Square) and isinstance(test_square, Rectangle)\
             and isinstance(test_square, Shape)
        expected = True
        self.assertEqual(actual, expected, \
            f"example/Square: Square class or constructor method did not work properly, \
                or did not derive from Rectangle as required.")

    def test_square_get_area_example(self):
        test_square = Square("test_id_s", 4)
        actual = test_square.get_area()
        expected = 16
        self.assertEqual(actual, expected, \
            f"example/Square/get_area: Method did not work. Expected {expected}, but found {actual}.")

    def test_square_get_perimeter_example(self):
        test_square = Square("test_id_s", 4)
        actual = test_square.get_perimeter()
        expected = 16
        self.assertEqual(actual, expected, \
            f"example/Square/get_perimeter: Method did not work. Expected {expected}, but found {actual}.")
    
if __name__ == "__main__":
    unittest.main()