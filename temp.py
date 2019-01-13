# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
trial=[(0,1,1,1,0)
transfering=(0,1,0,0;0.4,0,0.6,0;0,0.4,0,0.6;0,0,0.5,0.5)
print(transfering)
3+2
'''
    
import numpy as np
def CRP(alpha,users):
    n=[]#table
    u=[z for z in range(users)]#people
#    alpha=3
    loc=[0 for m in range(len(u))] #where the people sitting
    for i in range (len(u)):
       tmp =np.random.random()
       p=alpha/(alpha+i)
       if tmp<p:
           n.append(1)
           loc[i]=len(n)-1
       else:
           l=np.random.choice(u[:i], 1)
           loc[i]=loc[l[0]]
           n[loc[l[0]]]=n[loc[l[0]]]+1
    return n

users=int(input('number of users'))
T=int(input('number of time intervals'))
alpha=int(input('alpha in CRP'))

crp=CRP(alpha,users)

d2 = [c/(users+alpha) for c in crp]
initial_pro=np.append(d2,alpha/(users+alpha))

a=sum(initial_pro)
print(a)



'''number_of_iterations=input('number_of_iterations')
b=list()
for iteration in range (1,number_of_iterations+1):
    for i in range(1,U+1):
        mf=list()
        mc=list(1)
        t=T
        while t>=0:
            f(t,i)=f(t+1)
            mf.append()
            
            '''
            
            