from ProcessData import ProcessDataset
# from scripts import txt2img
#
# # test ProcessData
p = ProcessDataset()
# Virtualize the dataset - BTF
fileName='/Users/chenlianghong/PycharmProjects/DiffusionModel/matched_volumn/TCGA-AO-A0JI_1.3.6.1.4.1.14519.5.2.1.9203.4002.115495544730113615407489736518.npy'
img = p.loadImg(fileName)
# print(img)
# exit(0)
# txt2img.numpy_to_pil(img)
# p.virtualizeMatrix()
# exit(0)
# p.getMatchedImg()
# Virtualize the dataset - BTF
p.virtualizeImg(fileName)



#
# r5 = '013800150738'
# r0 = 0  # pointer
# r1 = 0  # sum1
# # r2 = 0  # sum2
# while r0 < 11:
#     r1 = r1 + int(r5[r0]) * 3
#     r0 = r0 + 1
#     r1 = r1 + int(r5[r0])
#     r0 = r0 + 1
# # r4 = r1*3+r2
# print(r1)
# while r1 > 0:
#     r1 = r1 -10
# if r1 == 0:
#     print('1')
# else: print('2')


