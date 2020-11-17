'''
Created on Nov 16, 2020

@author: houstonwalley
'''
import unittest
import Game.GameClass as GameClass


class Test(unittest.TestCase):
        
    def test100_010_Vertical(self):
        board = [0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,0,0,1,0,0,0, \
                 0,0,0,1,0,0,0, \
                 0,0,0,1,0,0,0, \
                 0,0,0,1,0,0,0]
        turnNum = 1
        x = 3
        expectedResult = True
        actualResult = GameClass.WillItWin(board, turnNum, x)
        self.assertEqual(expectedResult, actualResult)
           
    def test200_010_Vertical(self):
        board = [0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,0,0,1,0,0,0, \
                 0,0,0,1,0,0,0, \
                 0,0,0,1,0,0,0, \
                 0,0,0,1,0,0,0]
        turnNum = 2
        x = 3
        expectedResult = False
        actualResult = GameClass.WillItWin(board, turnNum, x)
        self.assertEqual(expectedResult, actualResult)
        
    def test100_010_Horizontal(self):
        board = [0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 1,1,1,0,0,0,0]
        turnNum = 1
        x = 3
        expectedResult = True
        actualResult = GameClass.WillItWin(board, turnNum, x)
        self.assertEqual(expectedResult, actualResult)
        
    def test100_020_Horizontal(self):
        board = [0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,1,1,0,1,0,0]
        turnNum = 1
        x = 3
        expectedResult = True
        actualResult = GameClass.WillItWin(board, turnNum, x)
        self.assertEqual(expectedResult, actualResult)
        
    def test100_030_Horizontal(self):
        board = [0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,0,1,0,1,1,0]
        turnNum = 1
        x = 3
        expectedResult = True
        actualResult = GameClass.WillItWin(board, turnNum, x)
        self.assertEqual(expectedResult, actualResult)
        
    def test100_040_Horizontal(self):
        board = [0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,0,0,0,1,1,1]
        turnNum = 1
        x = 3
        expectedResult = True
        actualResult = GameClass.WillItWin(board, turnNum, x)
        self.assertEqual(expectedResult, actualResult)
           
    def test200_010_Horizontal(self):
        board = [0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 1,1,1,0,0,0,0]
        turnNum = 2
        x = 3
        expectedResult = False
        actualResult = GameClass.WillItWin(board, turnNum, x)
        self.assertEqual(expectedResult, actualResult)
           
    def test200_020_Horizontal(self):
        board = [0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,1,1,0,1,0,0]
        turnNum = 1
        x = 3
        expectedResult = True
        actualResult = GameClass.WillItWin(board, turnNum, x)
        self.assertEqual(expectedResult, actualResult)
        
    def test200_030_Horizontal(self):
        board = [0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,0,1,0,1,1,0]
        turnNum = 2
        x = 3
        expectedResult = False
        actualResult = GameClass.WillItWin(board, turnNum, x)
        self.assertEqual(expectedResult, actualResult)
        
    def test200_040_Horizontal(self):
        board = [0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,0,0,0,1,1,1]
        turnNum = 2
        x = 3
        expectedResult = False
        actualResult = GameClass.WillItWin(board, turnNum, x)
        self.assertEqual(expectedResult, actualResult)
    
    def test100_010_Diagonal(self):
        board = [0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,0,0,1,0,0,0, \
                 0,0,1,0,0,0,0, \
                 0,1,0,0,0,0,0, \
                 0,0,0,0,0,0,0]
        turnNum = 1
        x = 0
        expectedResult = True
        actualResult = GameClass.WillItWin(board, turnNum, x)
        self.assertEqual(expectedResult, actualResult)
        
    def test100_020_Diagonal(self):
        board = [0,0,0,0,0,0,0, \
                 0,0,0,0,1,0,0, \
                 0,0,0,1,0,0,0, \
                 0,0,1,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,1,0,0,0,0,0]
        turnNum = 1
        x = 1
        expectedResult = True
        actualResult = GameClass.WillItWin(board, turnNum, x)
        self.assertEqual(expectedResult, actualResult)
        
    def test100_030_Diagonal(self):
        board = [0,0,0,0,0,1,0, \
                 0,0,0,0,1,0,0, \
                 0,0,0,1,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,0,1,0,0,0,0, \
                 0,0,1,0,0,0,0]
        turnNum = 1
        x = 2
        expectedResult = True
        actualResult = GameClass.WillItWin(board, turnNum, x)
        self.assertEqual(expectedResult, actualResult)
           
    def test200_010_Diagonal(self):
        board = [0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,0,0,1,0,0,0, \
                 0,0,1,0,0,0,0, \
                 0,1,0,0,0,0,0, \
                 0,0,0,0,0,0,0]
        turnNum = 2
        x = 0
        expectedResult = False
        actualResult = GameClass.WillItWin(board, turnNum, x)
        self.assertEqual(expectedResult, actualResult)
        
    def test300_010_Diagonal(self):
        board = [0,0,0,0,0,0,0, \
                 0,0,0,0,0,0,0, \
                 0,0,0,1,0,0,0, \
                 0,0,0,0,1,0,0, \
                 0,0,0,0,0,1,0, \
                 0,0,0,0,0,0,0]
        turnNum = 1
        x = 6
        expectedResult = True
        actualResult = GameClass.WillItWin(board, turnNum, x)
        self.assertEqual(expectedResult, actualResult)
    