def mergesort(list):
    #Dividing list
    if len(list)>1:
        mid = len(list)//2
        leftlist = list[:mid]
        rightlist = list[mid:]
        mergesort(leftlist)
        mergesort(rightlist)
        #Merge list
        i,j,k=0,0,0
        while i < len(leftlist) and j< len(rightlist):
            if leftlist[i]<rightlist[j]:
                list[k]= leftlist[i]
                i+=1
                k+=1
            else:
                list[k]=rightlist[j]
                j +=1
                k +=1
                
        # To check any value is left in left and right list
        while i < len(leftlist):
            list[k]=leftlist[i]
            i+=1
            k+=1
        while j < len(rightlist):
            list[k]=rightlist[j]
            j+=1
            k+=1
          
import random
list =[]
for i in range(10):
    a =random.randint(0,20)
    list.append(a) 
print("unsorted list : ", list, end=" ")
print()
mergesort(list)
print("After mergesort : ", list , end = ' '))
            
        
    
        
    
