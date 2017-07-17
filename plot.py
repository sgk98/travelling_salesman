import matplotlib.pyplot as plt
import nn

def plotTSP():

    fo=open("./data/a281.tsp","r")
    X,Y=[],[]
    paths=nn.nn()
    data=fo.readlines()
    for i in range(len(data)):
        X.append(float(data[i].split()[1]))
        Y.append(float(data[i].split()[2]))
    
    a_scale=float(max(X))/float(100.0)
    new_data=[]
    for i in range(len(paths)):
        new_data.append([X[paths[i]],Y[paths[i]]])
    print new_data[-1][0]
    print new_data[-1][1] 
    #print new_data[0][0]-new_data


    #plt.arrow(new_data[-1][0],new_data[-1][1], (new_data[0][0] - new_data[-1][0]), (new_data[0][1] - new_data[-1][1]), head_width = a_scale,color ='g', length_includes_head=True)

    for i in range(len(new_data)-1):

        plt.arrow(new_data[i][0], new_data[i][1], (new_data[i+1][0] - new_data[i][0]), (new_data[i+1][1] - new_data[i][1]),head_width = a_scale,color = 'g', length_includes_head = True)

    plt.xlim(min(X)*1.1, max(X)*1.1)
    plt.ylim(min(Y)*1.1, max(Y)*1.1)
    plt.show()

        
if __name__=="__main__":
    plotTSP()
