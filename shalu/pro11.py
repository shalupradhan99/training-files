import pandas as pd
import numpy as np

#Reading and Printing Data-set
data = pd.read_csv("find_s.csv")
print(data)


#Defining Concepts (features)
concept=np.array(data)[:,:-1]
print(concept)
#defining target basically our positive and negative examples
target=np.array(data)[:,-1]
print(target)


#Defining Model (S-find algorithm concepts)
def func(concept,target):
    for i , val in enumerate(target):
        if val=="Yes":
            specific_hypothesis=concept[i].copy()
            print(specific_hypothesis)
            break
    count=0
    for i, val in enumerate(concept):
        count=count+1
        print("concept=",concept[i])
        print("count=",count)
        if target[i]=="Yes":
            print("target[i]=",target[i])
            for x in range (len(specific_hypothesis)):
                print("x=",x)
                if val[x]!= specific_hypothesis[x]:
                    specific_hypothesis[x]='?'
                    print("specific_hypothesis[x]=",specific_hypothesis)
                else:
                    pass
    print(specific_hypothesis)
return specific_hypothesis

print("Final Specific Hypothesis ", func(concept,target))

