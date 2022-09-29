# Its a simmple sorting algortinm that builds the final sorted list one item at a time
def insertionsort(list):
    for i in range(1,len(list)):
        ce = list[i]
        sorted = i
        while ce < list[sorted-1] and sorted >0:
             list[sorted]= list[sorted-1]
             sorted = sorted -1 
             list[sorted]  = ce 
    print(list)        
        
            

list = [9,4,2,1,6,12]
insertionsort(list)