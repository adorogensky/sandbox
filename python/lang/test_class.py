#!/usr/bin/python3
import unittest

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def __eq__(self, other):
        if isinstance(other, Car):
            return self.make == other.make and self.model == other.model
        return False
    def __str__(self):
        return f'{self.make} {self.model}'

class Truck(Car):
    def __init__(self, make, model):
        super().__init__(make, model)
    def __str__(self):
        return f'{super().__str__()} (truck)'

car1 = Car(make = 'Ford', model = 'F150')
car2 = Car('Ford', 'F150')
truck = Truck(make = 'Ford', model = 'F550')

class PyClassTests(unittest.TestCase):
    def test_attributes_api(self):
        self.assertEqual(car1.make, 'Ford')
        self.assertEqual(car1.model, 'F150')
    def test_attributes_impl(self):
        car1.__secret__ = 'secret'
        self.assertEqual(car1.__secret__, 'secret')
    def test_equal(self):
        self.assertEqual(car1, car2)
    def test_is_same_object(self):
        self.assertTrue(car1 is car1)
    def test_is_different_object(self):
        self.assertFalse(car1 is car2)
    def test___str___(self):
        self.assertEqual(f'{car1}', 'Ford F150')
    def test___str___override(self):
        self.assertEqual(f'{truck}', 'Ford F550 (truck)')

if __name__ == '__main__':
    unittest.main()
