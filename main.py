from Heap import Heap
def getnumber(filename):
    number= []
    with open(filename)as file:
        for line in file:
            values = line.split(",")
            for i in range(len(values)):
                number.append(values[i])
    return number

def sort(NumberOfList):
    Newheap = Heap()
    sortlist = []
    for i in range(len(NumberOfList)):
        Newheap.insert(int(NumberOfList[i]))
    while Newheap.is_empty() == False:
        sortlist.append(Newheap.extract_min())
    return sortlist

def main ():
    list = getnumber("numbers.txt") 
    list =  sort(list)  
    for i in range(len(list)):
        print(list[i])
main()