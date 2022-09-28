class selectivesort:
    def descendingorder(list):
        for i in range(len(list)):
            maxvalue = max(list[i:])
            maxindex = list.index(maxvalue)
            list[i],list[maxindex]=list[maxindex],list[i]
        print("Descending Order: ",list)
    def ascendingorder(list):
        for i in range(len(list)):
            minvalue = min(list[i:])
            minindex = list.index(minvalue)
            list[i],list[minindex]=list[minindex],list[i]
        print("Ascending Order : ", list)
   
a = selectivesort
list = [34,12,40,25,17]
a.ascendingorder(list)
a.descendingorder(list)