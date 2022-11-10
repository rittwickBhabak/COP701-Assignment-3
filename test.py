import unittest 
from tkinter.graphplotter import  *


class TestPoint(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass 


    
    @classmethod
    def tearDownClass(cls):
        pass 
    
    def setUp(self):
        def temp(x):
            return x*x

        self.height = 100
        self.width = 200
        self.eval = temp 
        self.domain = [-10, 10] 

        self.point = Point(100, 200, temp, [-10, 10]) 
    
    def tearDown(self):
        pass 

    def test_constructor(self):

        self.assertEqual(self.point.height, 100)
        self.assertEqual(self.point.width, 200)
        self.assertEqual(self.point.domain, [-10, 10])


    def test_set_points(self):
        domain = [5, 6, 7, 8]
        co_domain = [10, 9, 15, 12]
        expected = [(x, self.height-y) for x, y in zip(domain, co_domain)]
        self.point.set_points(domain, co_domain)
        self.assertEqual(self.point.points, expected)




if __name__=='__main__':
    unittest.main()
