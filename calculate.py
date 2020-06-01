# encoding: utf-8
"""
@author: julse@qq.com
@time: 2020/5/31 23:01
@desc:
"""
import numpy as np
import random

def random_init(course_size,fout):
    # course_size = 82
    L1 = random.sample(range(1, course_size + 1), course_size)
    data = np.array(L1)
    random_list = data / (course_size * 1.3)
    np.save(fout,random_list)
    return list(random_list)

def compareTwo(random_list,x,y):
    if random_list[x]>random_list[y]:
        return 1
    return 0
def cosine_similarity(x,y):
    num = x.dot(y.T)
    denom = np.linalg.norm(x) * np.linalg.norm(y)
    return num / denom

def calculate_matrics():
    '''
    :return:
    fout = r'file/course_group2_3_cosin_similarity_matric.npy'
    data = np.load(fout)
    print(data)
    '''
    fin = r'file/course_group2_2.txt'
    fout_importantlist = r'file/course_group2_3_important_list.npy'
    fout_elementary_list = r'file/course_group2_4_elementary_list.npy'

    fout_important_matric = r'file/course_group2_5_important_matric.npy'
    fout_elementary_matric = r'file/course_group2_6_elementary_matric.npy'
    fout_cosin_similarity_matric = r'file/course_group2_7_cosin_similarity_matric.npy'

    data = np.loadtxt(fin,delimiter=',')
    course_size = data.shape[0]
    important_list = random_init(course_size, fout_importantlist)
    elementary_list = random_init(course_size,fout_elementary_list)

    important_matric = np.zeros((course_size,course_size))
    elementary_matric = np.zeros((course_size,course_size))
    cosine_similarity_matric = np.zeros((course_size,course_size))

    for i in range(course_size):
        for j in range(course_size):
            if i == j:continue
            important_matric[i,j] = compareTwo(important_list,i,j)
            elementary_matric[i,j] = compareTwo(elementary_list,i,j)
            cosine_similarity_matric[i,j] = cosine_similarity(data[i],data[j])
    np.save(fout_important_matric,important_matric)
    np.save(fout_elementary_matric,elementary_matric)
    np.save(fout_cosin_similarity_matric,cosine_similarity_matric)
if __name__ == '__main__':
    # calculate_matrics()
    # fout_importantlist = r'file/course_group2_3_important_list.npy'
    # fout_elementary_list = r'file/course_group2_4_elementary_list.npy'
    # fout_importantlist = np.load(fout_importantlist)
    # fout_elementary_list = np.load(fout_elementary_list)
    print()
