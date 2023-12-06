import unittest
from user import User


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Start test')

    @classmethod
    def tearDownClass(cls):
        print('Ending the test')

    def setUp(self):
        print('Starting test')
        self.user1 = User('Abay', 'Kunanbay', 'Abay_K')
        self.user2 = User('Mukhtar', 'Auez', 'Mukhtar_A')

    def tearDown(self):
        print('qwerty')

    def test_data(self):
        self.assertEqual(self.user1.get_info(), 'Abay Kunanbay : Abay.Kunanbay@gmail.com ; Abay_K')
        self.assertEqual(self.user2.get_info(), 'Mukhtar Auez : Mukhtar.Auez@gmail.com ; Mukhtar_A')

    def change_name(self):
        self.user1.name = 'Ali'
        self.assertEqual(self.user1.get_info(), 'Ali Kunanbay : Ali.Kunanbay@gmail.com ; Abay_K')


if __name__ == '__main__':
    unittest.main()