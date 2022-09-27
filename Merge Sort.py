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
          
list = [22,97,121,54,12,76,32]
mergesort(list)
print("Sorted List is ", list)
            
        
    
        
    