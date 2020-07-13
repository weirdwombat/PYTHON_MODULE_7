import unittest
#do i need to import array here as well
import sort_and_search_array


class MyTestCase(unittest.TestCase):
    def test_sort_found(self):
        #need to be passing a list in
        self.assertEqual(list.index(0), [0],#list = [0, 3, 4, 0])
        #if i have [0, 3, 4, 0]
        #then my array.index[0] would give me [0]

    def test_sort_not_found(self):
        #if i have [0, 3, 4, 0]
        #then my expected output would be negative 1


if __name__ == '__main__':
    unittest.main()
