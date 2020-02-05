# -*- coding: utf-8 -*-
"""
Updated Feb 4, 2020
The primary goal of this file is to demonstrate a simple unittest implementation

@author: rzhong2
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
		
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(3,3,1),'Isoceles','3,3,1 should be isoceles')

    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(5,6,7),'Scalene','5,6,7 should be scalene')

    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(200,201,201),'InvalidInput','200,201,201 should be InvalidInput')		
		
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(-1,1,1),'InvalidInput','-1,1,1 should be InvalidInput')

    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,2,100),'NotATriangle','1,2,100 should be NotATriangle')
		
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

