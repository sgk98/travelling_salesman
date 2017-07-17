import pickle
import math
import random

import nn

def eval_cost(path,adj_mat):
    cost=0
    for i in range(len(path)-1):
        cost+=adj_mat[path[i]][path[i+1]]
    return cost

def gen_rand():
    path=[i for i in range(1,280)]
    random.shuffle(path)
    path=[0]+path+[0]
    return path

def opt(iter=100000):
    fo=open("adj_mat","rb")
    adj_mat=pickle.load(fo)

    path=gen_rand()
    print(eval_cost(path,adj_mat))
    count=0
    for it in range(iter):

        r1=random.randint(1,len(path)-3)
        r2=random.randint(1,len(path)-3)
        o1=path[r1]
        o2=path[r1+1]
        o3=path[r2]
        o4=path[r2+1]
        o5=path[r1+2]
        o6=path[r2+2]
        if abs(r1-r2)!=1:
            oldcost=adj_mat[o1][o2]+adj_mat[o3][o4]+adj_mat[o2][o5]+adj_mat[o4][o6]
            newcost=adj_mat[o1][o4]+adj_mat[o3][o2]+adj_mat[o4][o5]+adj_mat[o2][o6]
            if oldcost>newcost:
                count+=1
                path[r1+1],path[r2+1]=path[r2+1],path[r1+1]
    print eval_cost(path,adj_mat)
    print(count)
if __name__=="__main__":
    opt()
