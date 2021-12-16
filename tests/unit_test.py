import unittest
import unit2


class Test(unittest.TestCase):
    def test_cancer1(self):
        res=unit2.classifier_naive.predict([[1,3,4,6,2,4,5,7,2]])
        self.assertEqual(res,4)
        
    def test_cancer2(self):
        res=unit2.classifier_naive.predict([[3,1,2,1,2,1,2,1,1]])
        self.assertEqual(res,2)
        
    def test_cancer3(self):
        res=unit2.classifier_naive.predict([[0,0,0,0,0,0,0,0,0]])
        self.assertEqual(res,2)
       
    def test_cancer4(self):
        res=unit2.classifier_naive.predict([[10,10,10,8,6,1,8,9,1]])
        self.assertEqual(res,4)
        
if __name__ == '__main__':
    unittest.main()