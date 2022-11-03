import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
from Config import Config


class ProcessDataset(object):

    def __init__(self):
        self.btf = Config.BTF_features
        self.matchedImg = Config.mathched_volumn

    def getBTF(self) -> pd.DataFrame:
        return pd.read_csv(self.btf,
                names=['ID','V1','V2','V3','V4','V5','V6','V7','V8','V9','V10','V11','V12','V13','V14','V15','V16','V17'])

    def getMatchedImg(self) -> list:
        result = []
        for dirpath, dirnames, filenames in os.walk(self.matchedImg):
            for filepath in filenames:
                result.append(os.path.join(dirpath, filepath))
        return result

    def loadImg(self, fileName:str) -> list:
        # npy = np.load(fileName)
        # print(np.shape(npy))
        return np.load(fileName)

    def virtualizeMatrix(self):
        print(self.getBTF())

    def virtualizeImg(self, fileName:str):
        dic = self.getMatchedImg()
        for each in dic:
            depthmap = np.load(each)
            plt.imshow(depthmap[:,:,0], cmap='gray')
            plt.show()
        # npy = np.load(fileName)
        # fig = plt.figure()
        # ax = fig.add_subplot(111, projection='3d')
        # ax.plot(npy[:,0],npy[:,1],npy[:,2])
        # plt.show()
