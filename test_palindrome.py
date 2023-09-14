from unittest import TestCase, main

class TestCheckPalindrome(TestCase):

    def test_palindrome(self):
        self.assertTrue(check_palindrome('racecar'))
        self.assertTrue(check_palindrome('yobananaboy'))
        self.assertTrue(check_palindrome('poop'))
        self.assertTrue(check_palindrome('madamimadam'))

    def test_non_palindrome(self):
        self.assertFalse('matrix')
        self.assertFalse('helloworld')
        self.assertFalse('sean', False)

    def test_casing(self):
        self.assertTrue(check_palindrome('Tacocat'))
        self.assertTrue(check_palindrome('TacoCat'))
        self.assertTrue(check_palindrome('TACocat'))

    def test_uneven_amount(self):
        pass

if __name__ == '__main__':
    main()