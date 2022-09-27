class Bubblesort:
    def ascending(list):
        for i in range(len(list)-1,0,-1):
            for j in range(i):
                if list[j]>list[j+1]:
                    list[j],list[j+1] = list[j+1],list[j]
        print(list)
    
    def descending(list):
        for i in range(len(list)-1,0,-1):
            for j in range (i):
                if list[j]<list[j+1]:
                    list[j],list[j+1] = list[j+1],list[j]
        print(list)
        

a = Bubblesort
list = [56,32,11,89,25,100,65,87]
a.ascending(list)
a.descending(list)
list = ['yak','apple','cat','bat','pineapple','zoo','hen']
Bubblesort.descending(list)
Bubblesort.ascending(list)
    