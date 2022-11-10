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

    def test_get_scaled_values(self):
        l = [10, 20 , 100, 50, 20, 80, 20, 90, 18]
        mx = max(l)
        self.point.get_scaled_values(l, mx)
        not_expected = [10, 20]
        self.assertNotEqual(self.point.get_scaled_values(l, mx), not_expected)
        expected = [0.0, 11.11111111111111, 100.0, 44.44444444444444, 11.11111111111111, 77.77777777777779, 11.11111111111111, 88.88888888888889, 8.88888888888889]
        self.assertEqual(self.point.get_scaled_values(l, mx), expected)

    
class TestPointFromList(unittest.TestCase):

    def setUp(self):
        self.height = 200
        self.width = 1000
        self.data = [
            (5, 10), (10, 5), (9, 12), (21, 22), (19, 100), (25, 100)
        ]

    def test_constructor(self):
        self.points = PointFromList(self.height, self.width, self.data)
        exptected = [(0.0, 189.47368421052633),(250.0, 200.0),(200.0, 185.26315789473685),(800.0, 164.21052631578948),(700.0, 0.0),(1000.0, 0.0)]
        self.assertEqual(self.points.points, exptected)

class TestPointFromFunction(unittest.TestCase):

    def setUp(self):
        self.height = 200
        self.width = 1000
        self.domain = [-10, 10]
        self.eval = lambda x: x*x + (1 / x)
        self.points = PointFromFunction(self.height, self.width, self.eval, self.domain)

    # def test_constructor(self):
    #     x = [] 
    #     low = self.domain[0]
    #     high = self.domain[1] 
    #     diff = 0.01
    #     while low<=high:
    #         x.append(low)
    #         low = low + diff 

    #     y = [self.eval(i) for i in x]
    #     self.domain = self.points.get_scaled_values(x, self.width)
    #     self.co_domain = self.points.get_scaled_values(y, self.height)
    #     expected = list(zip(self.domain, self.co_domain))
        
    #     self.assertEqual(self.points.points, expected)
        
    def test_get_y_values(self):
        expected = [self.eval(i) for i in self.domain]
        
        self.assertNotEqual(self.points.get_y_values(self.eval, self.domain), expected)

if __name__=='__main__':
    unittest.main()
