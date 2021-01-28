#A15708577


## all the explanations for codes are on my pdf submission. page 4, 5, and 6

import numpy as np

def distance2points(x,y):
        answer = np.sqrt( (x[0]-y[0])**2 + (x[1]-y[1])**2)
        return answer 
    
##############################################################################
    
def computeLineThroughTwoPoints(p1,p2):
    
    if np.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)<=1e-8:
        #check for non-distinct points
        print('non-distinct points. please input distinct points')
       
    elif p1[0]==p2[0]: #check for vertical x=constant case
        answer = [1,0,-p1[0]]
        return answer
    
    else: #explanation in hw pdf
        m= (p2[1]-p1[1])/(p2[0]-p1[0])
        b1= p1[1]-m*p1[0]
        
        a=m/np.sqrt(m**2+1)
        b=-1/np.sqrt(m**2+1)
        c=b1/np.sqrt(m**2+1)
        answer = [a,b,c]
        return answer
     
def computeDistancePointToLine(q,p1,p2): #explanation in hw pdf
    a,b,c = computeLineThroughTwoPoints(p1,p2)
    distance = np.abs(a*q[0]+b*q[1]+c)/np.sqrt(a**2+b**2)
    return distance


def computeDistancePointToSegment(q,p1,p2):  #explanation in hw pdf
    a,b,c = computeLineThroughTwoPoints(p1,p2)
    
    #distance = 
    
    opx = (b*(b*q[0]-a*q[1])-a*c)/np.sqrt(a**2+b**2)
    opy = (a*(-b*q[0]+a*q[1])-b*c)/np.sqrt(a**2+b**2)
    op = [opx, opy]
    
         
    dopp1 = distance2points(op, p1)
    dopp2 = distance2points(op, p2)
    dp1p2 = distance2points(p2, p1)
    
    if dopp1 + dopp2 == dp1p2:
        w = 0
        distance = computeDistancePointToLine(q,p1,p2)
    else:
        if dopp1 < dopp2:
            w = 1
            distance = distance2points(q, p1)
        elif dopp2 < dopp1:
            w = 2
            distance = distance2points(q, p2)
    
    answer = [distance, w]
    return answer

##############################################################################

def isPointonSegment(q,p1,p2):  #explanation in hw pdf
    dqp1 = distance2points(q, p1)
    dqp2 = distance2points(q, p1)
    dp1p2 = distance2points(p2, p1)
    if dqp1 + dqp2 == dp1p2:
        return 1
    else:
        return 0

def theta2vectors(q,p1,p2):  #explanation in hw pdf
    q = np.array(q)
    p1 = np.array(p1)
    p2 = np.array(p2)
    
    v1 = p1-q
    v2 = p2-q
    
    theta = np.arccos( np.dot(v1,v2)/
                     (distance2points(q, p1)*distance2points(q, p2)))
    
    return theta


def computeDistancePointToPolygon(P,q):  #explanation in hw pdf
    P = np.array(P)
    vertex = len(P)
    if vertex < 3:
        print('Not enough points for a polygon. At least a 3x2 list')
    elif vertex == 3 and computeDistancePointToLine(P[0],P[1],P[2])==0:
        print('Please input an actual polygon. These P points form a line :<')
        
    else: 
            
        segment = np.empty([0])
        theta = np.array([])
        zal = 0
        for i in range(vertex): 
            
            if i == vertex-1:
                segment_temp = computeDistancePointToSegment(q,P[i],P[0])
                theta_temp = theta2vectors(q, P[i], P[0])
                print(segment_temp)
            else:
                segment_temp = computeDistancePointToSegment(q,P[i],P[i+1])
                theta_temp = theta2vectors(q, P[i], P[i+1])
                
            theta = np.append(theta, theta_temp)
            
            # print(segment_temp)
            if segment_temp[1] == 0:
                # print(zal)
                segment = np.append(segment,segment_temp[0])
                zal +=1
                print(segment)
       
        uron =1
        if sum(theta) == 2*np.pi:
            uron = 0
            for i in range(vertex):
                for j in range(vertex):
                    uron += isPointonSegment(q,P[i],P[j])
        if uron == 0:
            distance = 0
        else:
            distance = 1#min(segment)
            
        return distance
   
        
        


