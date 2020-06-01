# 0.0 coding:utf-8 0.0
# 基因突变

import random


def mutation(pop, pm):
    px = len(pop)
    py = len(pop[0])
    
    for i in range(px):
        if(random.random() < pm):
            mpoint = random.randint(0, py-1)
            if(pop[i][mpoint] == 1):
                pop[i][mpoint] = 0
            else:
                pop[i][mpoint] = 1


def my_mutation(pop, pm):
    px = len(pop)
    py = len(pop[0][0])

    for i in range(px):
        if (random.random() < pm):

            mpoint = random.randint(0, py-1)
            pair = random.sample(range(0, py), 2)

            for mpoint in range(py):
                if (pop[i][0][mpoint] == pair[0]):
                    pop[i][0][mpoint] = pair[1]
                elif(pop[i][0][mpoint] == pair[1]):
                    pop[i][0][mpoint] = pair[0]
                else:
                    pass
        if len(pop[i][0]) != len(set(pop[i][0])):
            print('mutation error')

if __name__ == '__main__':
    pass
