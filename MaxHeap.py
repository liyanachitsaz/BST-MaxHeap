class HeapNode:
    def __init__(self,ID,priority):
        self.ID = ID
        self.priority = priority


class MaxHeap:
    def __init__(self):
        self.heapArray = [] 

    def isEmptyHeap(self):
        return len(self.heapArray) == 0

    def sizeMaxHeap(self):
        return len(self.heapArray)

    def maxHeapify(self,index):
        left = 2 * index + 1
        right = 2 * index + 2

        if left < self.sizeMaxHeap() and self.heapArray[left].priority > self.heapArray[index].priority:
            largest = left

        else:
            largest = index

        if right < self.sizeMaxHeap() and self.heapArray[right].priority > self.heapArray[largest].priority:
            largest = right
        
        if largest != index:
            self.heapArray[largest], self.heapArray[index] = self.heapArray[index], self.heapArray[largest]

            self.maxHeapify(largest)

    def searchHeap(self,ID):
        i = 0
        while i != self.sizeMaxHeap():
            if self.heapArray[i].ID == ID:
                return i
            i+=1
        
    def increasePriority(self,ID, newPriority):
        findID = self.searchHeap(ID)

        if findID is None:
            print("ID not found.\n")
            return False
        if newPriority < self.heapArray[findID].priority:
            print("new priority is smaller than current priority.\n")
            return False

        self.heapArray[findID].priority = newPriority

        parent = (findID-1)//2

        while findID > 0 and self.heapArray[parent].priority < self.heapArray[findID].priority:

            self.heapArray[parent], self.heapArray[findID] = self.heapArray[findID], self.heapArray[parent]
            findID = parent
            parent = (findID-1)//2
        return True

    def insertHeap(self,ID,priority):
        newNode = HeapNode(ID,-1000)
        self.heapArray.append(newNode)
        self.increasePriority(ID,priority)

    def deleteMaxHeap(self):
        if not self.sizeMaxHeap():
            print("No request exists\n")
            return 
        deleteNode = self.heapArray[0]
        self.heapArray[0] = self.heapArray[self.sizeMaxHeap()-1]
        self.heapArray.pop()
        self.maxHeapify(0)
        return deleteNode

    def processHighestPriorityRequest(self,BST):
        request = self.deleteMaxHeap()
        if request is not None:
            BST.deleteRequest(request.ID)
        return False

    def printMaxHeap(self):
        if self.isEmptyHeap():
            print("Max heap is empty\n")

        else :
            index = 0
            level = 0
            size = self.sizeMaxHeap()
            while index < size:
                count = 2 ** level  
                print(f"Level {level}:", end=" ")

                for i in range(count):
                    if index >= size:
                        break
                    print(f"[ID={self.heapArray[index].ID}, P={self.heapArray[index].priority}]", end=" ")
                    index += 1

                print()  
                level += 1

    def DeleteNode(self, ID):
        index = self.searchHeap(ID)

        if index is None:
            print(f"ID {ID} not found in MaxHeap.")
            return False

        last = self.sizeMaxHeap() - 1

        if index != last:
            self.heapArray[index] = self.heapArray[last]

        self.heapArray.pop()

        if index < self.sizeMaxHeap():
            self.maxHeapify(index)
            parent = (index - 1) // 2
            while index > 0 and self.heapArray[parent].priority < self.heapArray[index].priority:
                self.heapArray[parent], self.heapArray[index] = self.heapArray[index], self.heapArray[parent]
                index = parent
                parent = (index - 1) // 2

        return True
        