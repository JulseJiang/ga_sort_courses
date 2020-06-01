# encoding: utf-8
"""
@author: julse@qq.com
@time: 2020/6/1 0:11
@desc:
https://scikit-opt.github.io/scikit-opt/#/en/README?id=_2-genetic-algorithm
"""

import numpy as np

# fout = r'file/course_group2_3_cosin_similarity_matric.npy'
# fout_importantlist = r'file/course_group2_4_elementary_list.npy'
# fout_elementary_list = r'file/course_group2_5_elementary_list.npy'
#
# important_matric = np.load(fout_importantlist)
# elementary_matric = np.load(fout_elementary_list)
# cosine_similarity_matric = np.load(fout)

def schaffer(p):
    '''
    This function has plenty of local minimum, with strong shocks
    global minimum at (0,0) with value 0
    '''
    x1, x2 = p
    x = np.square(x1) + np.square(x2)
    return 0.5 + (np.sin(x) - 0.5) / np.square(1 + 0.001 * x)

def my_schaffer(p):
    # x1, x2 = p
    print(p)



# %%
from sko.GA import GA

# ga = GA(func=schaffer, n_dim=2, size_pop=50, max_iter=800, lb=[-1, -1], ub=[1, 1], precision=1e-7)
ga = GA(func=schaffer, n_dim=2, size_pop=50, max_iter=800, lb=[-1, -1], ub=[1, 1], precision=1e-7)
best_x, best_y = ga.run()
print('best_x:', best_x, '\n', 'best_y:', best_y)

# %% Plot the result
import pandas as pd
import matplotlib.pyplot as plt

Y_history = pd.DataFrame(ga.all_history_Y)
fig, ax = plt.subplots(2, 1)
ax[0].plot(Y_history.index, Y_history.values, '.', color='red')
Y_history.min(axis=1).cummin().plot(kind='line')
plt.show()