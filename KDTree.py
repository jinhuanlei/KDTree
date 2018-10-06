import sys
import os

minSize = 0
dimensionType = 0


def getInputs():
    global minSize, dimensionType
    # sys.argv.append("/2d_small.txt")             # necessary command for debug
    # sys.argv.append("2")
    arguments = sys.argv
    if len(arguments) != 3:
        print("Please Enter Correct Inputs !")
        return
    fileName = sys.argv[1]
    minSize = int(sys.argv[2])
    # print(os.path.exists(module_path+"2d_large.txt"))
    # print(module_path+"/"+fileName)
    module_path = os.path.dirname(__file__)
    dataFile = module_path + "/" + fileName  # pycharm can ignore this / , but in terminal cannot
    if not os.path.exists(dataFile):
        print("Please Enter Correct File name !")
        return
    inputData = []
    with open(dataFile, "r") as f:
        # data=f.readlines()
        for line in f.readlines():
            line = line.strip()
            inputData.append(list(map(float, line.split(" "))))
    dimensionType = int(inputData[0][0])
    dataSet = inputData[1:]
    # print(dimensionType)
    root = BuildTree(dataSet, 0)
    traverseTree(root)


def printNode(root):
    print('items:', ', '.join(['%s:%s' % item for item in root.__dict__.items()]))


def traverseTree(root):  # preOrder
    # self.printNode(root)
    printNode(root)


def traversalTree(root):
    # calculate Bounding value
    dataSets = root.nodes
    minBounding = []
    maxBounding = []
    for d in range(dimensionType):
        minBounding.append(findMin(dataSets, d))
        maxBounding.append(findMax(dataSets, d))
    print("Bounding Box : ", minBounding + " , ", maxBounding)


def findMin(dataSet, dimension):
    min = 1.0
    for s in dataSet:
        if s[dimension] < min:
            min = s[dimension]
    return min


def findMax(dataSet, dimension):
    max = 0.0
    for s in dataSet:
        if s[dimension] > max:
            max = s[dimension]
    return max


def BuildTree(dataSet, depth):
    if len(dataSet) <= minSize:
        return TreeNode(dataSet)
    else:
        split = depth % dimensionType  # +1 and -1 so I simply ignored it
        dataSet.sort(key=lambda x: x[split])
        left = 0
        right = len(dataSet) - 1
        median = int(left + (right - left) / 2)
        parent = TreeNode([dataSet[median]])
        parent.left = BuildTree(dataSet[0:median - 1], depth + 1)
        parent.right = BuildTree(dataSet[median + 1:right], depth + 1)
        return parent


class TreeNode:
    def __init__(self, nodes=None, left=None, right=None):
        self.nodes = nodes
        # self.split = split
        self.left = left
        self.right = right


if __name__ == "__main__":
    getInputs()
