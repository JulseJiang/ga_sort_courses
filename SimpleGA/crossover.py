# 0.0 coding:utf-8 0.0
# 交配

import random

def crossover(pop, pc):
    pop_len = len(pop)
    for i in range(pop_len - 1):
        if(random.random() < pc):
            cpoint = random.randint(0,len(pop[0]))
            temp1 = []
            temp2 = []
            temp1.extend(pop[i][0:cpoint])
            temp1.extend(pop[i+1][cpoint:len(pop[i])])
            temp2.extend(pop[i+1][0:cpoint])
            temp2.extend(pop[i][cpoint:len(pop[i])])
            pop[i] = temp1
            pop[i+1] = temp2

def my_crossover(pop, pc):
    pop_len = len(pop)
    for i in range(pop_len - 1):
        if(random.random() < pc):
            cpoint = random.randint(0,len(pop[0])-1)
            temp1 = []
            temp2 = []
            temp1.extend(pop[i][0][0:cpoint])
            temp1.extend(pop[i+1][0][cpoint:len(pop[i][0])])
            temp2.extend(pop[i+1][0][0:cpoint])
            temp2.extend(pop[i][0][cpoint:len(pop[i][0])])

            try:
                if len(temp1) != len(set(temp1)):
                    for j in range(len(temp1)):
                        if temp1.count(temp1[j]) == 2:
                            print('temp1.count(temp1[j]) and cpoint', temp1.count(temp1[j],cpoint))
                            print(temp1[j], temp1, '+++++++++++++++++++++++')
                            index_0 = temp1.index(temp1[j])
                            index_1 = temp1[index_0 + 1:].index(temp1[j]) + index_0 + 1
                            temp1[index_1] = pop[i][0][index_1]
                            temp2[index_1] = pop[i + 1][0][index_1]
                            print(pop[i][0], '------------------------')
                            print(temp1[j], temp1, '+++++++++++++++++++++++')
            except:
                assert 'crossover wrong'
            if len(temp1) != len(set(temp1)):assert 'crossover wrong len(temp1) != len(set(temp1))'
            pop[i][0] = temp1
            pop[i+1][0] = temp2

if __name__ == '__main__':
    pass
