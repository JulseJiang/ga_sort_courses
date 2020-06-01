# 0.0 coding:utf-8 0.0

import matplotlib.pyplot as plt
import math

from calobjValue import calobjValue
from calfitValue import calfitValue
from selection import selection
from crossover import crossover, my_crossover
from mutation import mutation, my_mutation
from best import best
from geneEncoding import geneEncoding, myEncoding

# print('y = 10 * math.sin(5 * x) + 7 * math.cos(4 * x)')
import numpy as np

fout_important_matric = r'../file/course_group2_5_important_matric.npy'
fout_elementary_matric = r'../file/course_group2_6_elementary_matric.npy'
fout_cosin_similarity_matric = r'../file/course_group2_7_cosin_similarity_matric.npy'

important_matric = np.load(fout_important_matric)
elementary_matric = np.load(fout_elementary_matric)
cosine_similarity_matric = np.load(fout_cosin_similarity_matric)

pop_size = 15		# 种群数量
generation_times = 50
max_value = 10      # 基因中允许出现的最大值
chrom_length = 82		# 染色体长度
pc =0.4			# 交配概率
pm = 0.1           # 变异概率
results = [[]]		# 存储每一代的最优解，N个二元组S
fit_value = []		# 个体适应度
fit_mean = []		# 平均适应度

# pop = [[0, 1, 0, 1, 0, 1, 0, 1, 0, 1] for i in range(pop_size)]
print('----------------------------------init popularization----------------------')
pop = myEncoding(pop_size, chrom_length)
print('----------------------------------evolution--------------------------------')
for i in range(generation_times):
	obj_value = calobjValue(pop, chrom_length, max_value)        # 个体评价
	fit_value = calfitValue(obj_value)      # 淘汰
	best_individual, best_fit = best(pop, fit_value)		# 第一个存储最优的解, 第二个存储最优基因
	results.append([best_fit, best_individual])
	print('---------------------------------selection------------------------------')
	selection(pop, fit_value)		# 新种群复制
	print('---------------------------------crossover-----------------------------')
	# my_crossover(pop, pc)		# 交配
	print('---------------------------------mutation-------------------------------')
	# my_mutation(pop, pm)       # 变异
	print('end of evolution i,result',i,results[-1])

results = results[1:]
results.sort()
print(results[-1])
print('best_individual',str(best_individual))
print('best_fit',str(best_fit))
print('obj_value[1]',str(obj_value[1]))


print(results[-1])
# print("y = %f, x = %f" % (results[-1][0], results[-1][1]))

X = []
Y = []
for i in range(pop_size):
	X.append(i)
	t = results[i][0]
	Y.append(t)

plt.plot(X, Y)

plt.show()
