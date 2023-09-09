import unittest

class Car():
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def description(self):
        return f'{self.make} {self.model}'
    def __eq__(self, other):
        if isinstance(other, Car):
            return self.make == other.make and self.model == other.model
        return False

class Truck(Car):
    def __init__(self, make, model):
        super().__init__(make, model)
    def description(self):
        return f'{super().description()} (truck)'

class PyClassTests(unittest.TestCase):
    def test_class(self):
        car = Car(make = 'Ford', model = 'F150')
        self.assertEqual('Ford', car.make)
        self.assertEqual('F150', car.model)
        self.assertEqual('Ford F150', car.description())
        car.model = 'F250'
        self.assertEqual('F250', car.model)
        self.assertEqual('Ford F250', car.description())
        car.__secret__ = 'secret'
        self.assertEqual(car.__secret__, 'secret')
    def test_class_inheritance(self):
        truck = Truck(make = 'Ford', model = 'F550')
        self.assertEqual('Ford', truck.make)
        self.assertEqual('F550', truck.model)
        self.assertEqual('Ford F550 (truck)', truck.description())
    def test_class_equal(self):
        car1 = Car('Ford', 'F150')
        car2 = Car('Ford', 'F150')
        self.assertFalse(car1 is car2)
        self.assertEqual(car1, car2)

if __name__ == '__main__':
    unittest.main()
