import unittest

def get_name(first_name, last_name):
    return f'{last_name}, {first_name}'

def get_name_with_default_args(first_name = 'Alexander', last_name = 'Dorogensky'):
    return get_name(first_name, last_name)

def get_toppings_with_arbitrary_positional_args(*toppings):
    return ', '.join(toppings)

def build_user_with_arbitrary_keyword_args(**props):
    return props

get_name_lambda = lambda first_name, last_name: f'{last_name}, {first_name}'

class PyFunctionTests(unittest.TestCase):
    def test_function(self):
        self.assertEqual('Dorogensky, Alexander', get_name('Alexander', 'Dorogensky'))
        self.assertEqual(
            'Dorogensky, Alexander',
            get_name(
                last_name='Dorogensky',
                first_name='Alexander'
            )
        )
    def test_function_with_default_args(self):
        self.assertEqual('Dorogensky, Alexander', get_name_with_default_args())
        self.assertEqual('Smith, Alexander', get_name_with_default_args(last_name = 'Smith'))
        self.assertEqual('Dorogensky, Eugene', get_name_with_default_args(first_name = 'Eugene'))
    def test_function_with_arbitrary_positional_args(self):
        self.assertEqual(
            'cheese, pepperoni, pineapple',
            get_toppings_with_arbitrary_positional_args('cheese', 'pepperoni', 'pineapple')
        )
    def test_function_with_arbitrary_keyword_args(self):
        self.assertEqual(
            {'first_name': 'Alexander', 'last_name': 'Dorogensky'},
            build_user_with_arbitrary_keyword_args(
                first_name='Alexander',
                last_name='Dorogensky'
            )
        )
    def test_function_lambda(self):
        self.assertEqual('Dorogensky, Alexander', get_name_lambda('Alexander', 'Dorogensky'))

if __name__ == '__main__':
    unittest.main()

