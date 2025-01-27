import unittest
import numpy as np
from CART import loadDataSet, binSplitDataSet, createTree, chooseBestSplit, regErr, regLeaf


class TestTreeFunctions(unittest.TestCase):

    def setUp(self):
        # small dataset for testing
        self.data = np.array([
            [1.0, 2.1, 1.0],
            [1.3, 3.4, 1.0],
            [1.1, 1.2, 0.0],
            [1.2, 1.4, 0.0]
        ])

    def test_loadDataSet(self):
        # Test loading a dataset from a file
        fileName = 'test_data.txt'
        with open(fileName, 'w') as f:
            f.write("1.0,2.1,1.0\n")
            f.write("1.3,3.4,1.0\n")
            f.write("1.1,1.2,0.0\n")
            f.write("1.2,1.4,0.0\n")
        loaded_data = loadDataSet(fileName)
        np.testing.assert_array_equal(loaded_data, self.data)

    def test_binSplitDataSet(self):
        # Test splitting the dataset
        mat0, mat1 = binSplitDataSet(self.data, feature=0, value=1.2)
        np.testing.assert_array_equal(mat0, np.array([[1.3, 3.4, 1.0]]))
        np.testing.assert_array_equal(mat1, np.array([
            [1.0, 2.1, 1.0],
            [1.1, 1.2, 0.0],
            [1.2, 1.4, 0.0]
        ]))

    def test_createTree(self):
        # Test creating a tree
        tree = createTree(self.data, leafType=regLeaf, errType=regErr, ops=(1, 2))
        self.assertIsInstance(tree, dict)
        self.assertIn('spInd', tree)
        self.assertIn('spVal', tree)
        self.assertIn('left', tree)
        self.assertIn('right', tree)

    def test_chooseBestSplit(self):
        # Test choosing the best split
        bestIndex, bestValue = chooseBestSplit(self.data, leafType=regLeaf, errType=regErr, ops=(1, 2))
        self.assertEqual(bestIndex, 1)
        self.assertAlmostEqual(bestValue, 1.4)


if __name__ == '__main__':
    unittest.main()
