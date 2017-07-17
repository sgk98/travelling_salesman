import pickle
import math
'''
Parses the data and creates an adjacency matrix
'''

def parse():

    fo=open("./data/a281.tsp")
    data=fo.readlines()
    ndata=[]
    for i in data:
        temp=i.split()
        tup=(float(temp[1]),float(temp[2]))
        ndata.append(tup)
    fo.close()
    return ndata


def dist(tup1,tup2):
    return math.sqrt((tup1[0]-tup2[0])**2 + (tup1[1]-tup2[1])**2)

def gen_matrix():

    data=parse()
    print(len(data))
    adj_mat=[[0 for i in range(len(data))] for j in range(len(data))]

    for i in range(len(data)):
        for j in range(len(data)):

            if i!=j:
                adj_mat[i][j]=dist(data[i],data[j])
    fo=open("adj_mat","wb")
    pickle.dump(adj_mat,fo)
    fo.close()

if __name__=="__main__":
    gen_matrix()



