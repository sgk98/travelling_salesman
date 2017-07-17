import random
import pickle
import math

import nn

def probability(old,new,T):

    if new<old:
        return 1.0
    else:
        #return 0.0
        return math.exp(- abs(old-new)/T)

def get_rand(n):

    init=[i for i in range(1,n)]
    random.shuffle(init)
    init=[0]+init+[0]
    return init

def get_state(oldstate):

    ind1=random.randint(1,len(oldstate)-2)
    ind2=random.randint(1,len(oldstate)-2)
    oldstate[ind1],oldstate[ind2]=oldstate[ind2],oldstate[ind1]
    return oldstate
    
def eval_state(state,adj_mat):
    
    cost=0
    for i in range(len(state)-1):
        cost+=adj_mat[state[i]][state[i+1]]
    return cost


def anneal():

    fo=open("adj_mat","rb")
    adj_mat=pickle.load(fo)
    init=nn.nn()
    cost=eval_state(init,adj_mat)
    T=50000
    alpha=0.99
    while T>0.00000000000000000000000000001:
        newstate=get_state(init)
        p=random.random()
        old=eval_state(init,adj_mat)
        new=eval_state(newstate,adj_mat)
        if p<probability(old,new,T):
            init=newstate
            cost=min(cost,new)
        T*=alpha
    print(cost)        

if __name__=="__main__":
    anneal()



