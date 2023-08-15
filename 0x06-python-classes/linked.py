class Node:

    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SlinkedList:

    def __init__(self):
        self.headval = None


    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
        
list1 = SlinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

#lint 1st Node to 2nd node
list1.headval.nextval = e2

#link 2nd Node to 3rd node
e2.nextval = e3

list1.listprint()
