import pickle
import math

'''
Implementation of nearest neighbour algorithm for Travelling Salesman
'''

def nn():

    fo=open("adj_mat","rb")
    adj_mat=pickle.load(fo)
    fo.close()

    visited=[False for i in range(len(adj_mat))]
    path=[0]
    visited[0]=True
    cost=0
    while len(path)<len(adj_mat)+1:
        
        cur=path[-1]
        visited[cur]=True
        found = False
        cur_min=100000000000000
        for i in range(len(adj_mat[cur])):
            
            if visited[i]==False and adj_mat[cur][i]<cur_min and i!=cur:
                cur_min=adj_mat[cur][i]
                cur_ind=i
                found=True
                
        if found==False:
            path.append(0)
            cost+=adj_mat[cur][0]
            break
        cost+=adj_mat[cur][cur_ind]
        path.append(cur_ind)
    print(cost)
    return path

if __name__=="__main__":
    nn()
    


