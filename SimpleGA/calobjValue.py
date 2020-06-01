# 0.0 coding:utf-8 0.0
# 解码并计算值

import math
import numpy as np
print('load matric')
fout_important_matric = r'../file/course_group2_5_important_matric.npy'
fout_elementary_matric = r'../file/course_group2_6_elementary_matric.npy'
fout_cosin_similarity_matric = r'../file/course_group2_7_cosin_similarity_matric.npy'

important_matric = np.load(fout_important_matric)
elementary_matric = np.load(fout_elementary_matric)
cosine_similarity_matric = np.load(fout_cosin_similarity_matric)
def decodechrom(pop, chrom_length):
    temp = []
    for i in range(len(pop)):
        t = 0
        for j in range(chrom_length):
            t += pop[i][j] * (math.pow(2, j))
        temp.append(t)
    return temp


def calobjValue(pop, chrom_length, max_value):
    return myb2d(pop)
    # temp1 = []
    # obj_value = []
    # temp1 = decodechrom(pop, chrom_length)
    # for i in range(len(temp1)):
    #     x = temp1[i] * max_value / (math.pow(2, chrom_length) - 1)
    #     obj_value.append(10 * math.sin(5 * x) + 7 * math.cos(4 * x))
    # return obj_value


def calculateF(n, i, j, k):
    w1 = 1
    w2 = 1
    w3 = 1
    if n * (n - 1) / 2 == 0 or (n - 1) == 0: return 1e-07
    t = round(w1 * i / (n * (n - 1) / 2) + w2 * j / (n * (n - 1) / 2) + w3 * k / (n - 1), 2)
    # print(t)
    return t


def myb2d(pop):
    obj_value = []
    for k in range(len(pop)):
        important_sum = 0
        elementary_sum = 0
        cosine_similarity_sum = 0
        b = pop[k][0]
        if b==1:
            print(b)
        if len(set(b)) != len(b):
            f=1e-07
            print('*********************** a != b **************************')
        else:
            for i in range(len(b)):
                for j in range(len(b)):
                    if i > j:
                        important_sum = important_sum + important_matric[b[i], b[j]]
                        elementary_sum = elementary_sum + elementary_matric[b[i], b[j]]
                if i+1 < len(b):
                    cosine_similarity_sum = cosine_similarity_sum + cosine_similarity_matric[b[i], b[i+1]]
            f = calculateF(len(b), important_sum, elementary_sum, cosine_similarity_sum)
        obj_value.append(f)
        # print(f,b)
    return obj_value

if __name__ == '__main__':
    pass
