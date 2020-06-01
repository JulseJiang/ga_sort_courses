# encoding: utf-8
"""
@author: julse@qq.com
@time: 2020/6/1 0:11
@desc:
https://scikit-opt.github.io/scikit-opt/#/en/README?id=_2-genetic-algorithm
"""

import numpy as np

fout = r'file/course_group2_3_cosin_similarity_matric.npy'
fout_importantlist = r'file/course_group2_4_elementary_list.npy'
fout_elementary_list = r'file/course_group2_5_elementary_list.npy'

# important_matric = np.load(fout_importantlist)
# elementary_matric = np.load(fout_elementary_list)
# cosine_similarity_matric = np.load(fout)
count = 1

def my_schaffer(p):
    return [x for x in p]

# def obj_func(p):
#     x1, x2, x3 = p
#     return -x1 - x2 - x3


constraint_eq = [
    lambda x: 0 if x[0] == x[1] else 1
]
# %%
from sko.GA import GA

'''
https://scikit-opt.github.io/scikit-opt/#/en/more_ga
if precision is an integer, and the number of all possible value is $2^n$, the performance is best
if precision is an integer, and the number of all possible value is not $2^n$, GA do these:
Modify ub bigger, making the number of all possible value to be $2^n$
Add an unequal constraint, and use penalty function to deal with it
If your equal constraint constraint_eq 和 unequal constraint constraint_ueq is too much, the performance is not too good. you may want to manually deal with it.
If precision is not an integer, but you still want this mode, manually deal with it. For example, your original precision=0.5, just make a new variable, multiplied by 2
'''

ga = GA(func=my_schaffer, n_dim=82, size_pop=41, max_iter=800, lb=[0]*82, ub=[82]*82, precision=[1]*82,prob_mut=0.1,constraint_eq=constraint_eq)
best_x, best_y = ga.run()
print('best_x:', best_x, '\n', 'best_y:', best_y)
# demo_func = lambda x: (x[0] - 1) ** 2 + (x[1] - 0.05) ** 2 + x[2] ** 2
# ga = GA(func=demo_func, n_dim=3, max_iter=500, lb=[-1, -1, -1], ub=[5, 1, 1], precision=[2, 1, 1])
# best_x, best_y = ga.run()
# print('best_x:', best_x, '\n', 'best_y:', best_y)