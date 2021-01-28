# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 20:33:30 2021

@author: soico
"""
import random 

def list2dict(li):#converting a list of lists to dict
    di = {}
    for keys in range(len(li)):
        di[keys] = li[keys]
    return di

def computeBFStree_random(AdjTable): 
    
    #check the type of the input, should be a dictionary or list of lists
    check = isinstance(AdjTable, (list, dict)) 
    if check == False:
        return 'AdjTable is invalid'
    
    if isinstance(AdjTable, list): #if it's a list, convert it to a dict
        AdjTable = list2dict(AdjTable)
    
     
    # define some variables etc.
    start = random.choice(list(AdjTable.keys()))
    visited= [] #return value, or can be thought of as visited 
    queue = [] #FIFO queue
    queue.append(start) 
    visited.append(start) 
    
    while queue: 
        v = queue.pop(0)
        
        for u in AdjTable.get(v):
            if u not in visited:
                visited.append(u)
                queue.append(u)
    return visited


def disconnected(G):
    
    if isinstance(G, list): #if it's a list, convert it to a dict
        G = list2dict(G)
        
    n = 1
    nodes =[]   
    V = computeBFStree_random(G)
    nodes.append(len(V)) 
    # compo = {1 : len(V)}
    if len(list(G.keys())) == len(V):
        
        return ['connected', n, nodes]
    
    
    
    while len(list(G.keys())) != len(V):
        n +=1
        G_sub = {}
        for node in list(G.keys()):
            if node not in V:
                G_sub[node] = G[node]
        
        V_sub = computeBFStree_random(G_sub)
        
        nodes.append( len(V_sub))
        V.extend(V_sub)
        print('end')
    return ['disconnected',n, nodes]
        
        
        
        
        
        
if __name__ == '__main__':
    """ 
    This is the place where you can test your function. 
    You can define variables, feed them into your function and check the output   
    """
    
    # defined as a dictionary 
    k = [[1],[0,2], [1], [4], [3], [], []]
    # AdjTable={ 'Tom' : ['Lee', 'Sam', 'Ben'],   
    #           'Lee' : ['Tom'],             
    #           'Sam' : ['Tom', 'Ben'],        
    #           'Ben' : ['Tom','Sam']}
    # print(computeBFStree(AdjTable))
    # AdjTable={ 'Tom' : ['Lee', 'Sam', 'Ben'], 
    #             'Lee' : ['Tom','Kara'],
    #             'Sam' : ['Tom', 'Ben','Zyga','Zal'],
    #             'Ben' : ['Tom','Sam', 'Kha'],
    #             'Kha' : ['Ben', 'Zal'],
    #             'Zal' : ['Kha', 'Sam', 'Zyga'],
    #             'Zyga' : ['Zal', 'Sam', 'Kara'],
    #             'Kara': ['Lee', 'Zyga'],
    #             'Not': []}
    [a,b,c] = disconnected(k)
    print(a,b,c)
    
    