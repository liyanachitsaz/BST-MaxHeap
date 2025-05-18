class BSTNode:
    def __init__(self,name,ID):
        self.name = name
        self.ID = ID
        self.left = None
        self.right = None
        self.parent = None


class BST:
    def __init__(self):
        self.root = None

    def isEmptyBST(self):
        return self.root is None
    
    def nodeCounter(self, node):
        if node is None:
            return 0
        return 1 + self.nodeCounter(node.left) + self.nodeCounter(node.right)
    
    def sizeBST(self):
        return self.nodeCounter(self.root)
    
    def insertRequest(self, ID, name):

        newNode = BSTNode(name,ID)

        if self.root is None:
            self.root = newNode
            return

        current = self.root
        while True:
            if ID < current.ID:
                if current.left is None:
                    newNode.parent = current
                    current.left = newNode
                    return
                current = current.left
            elif ID > current.ID:
                if current.right is None:
                    newNode.parent = current
                    current.right = newNode
                    return
                current = current.right
            else:
                print(f"Request with ID {ID} already exists.")
                return

    def searchRequest(self, ID):
        current = self.root
        while current is not None:
            if ID == current.ID:
                return current
            
            elif ID < current.ID:
                current = current.left

            else:
                current = current.right

        return None               

    def preOrderTraversal(self, node):
            if node is not None:
                print(f"ID={node.ID}, Name={node.name}")
                self.preOrderTraversal(node.left)
                self.preOrderTraversal(node.right)
        
    def printBST(self):
            if self.root is None:
                print("BST is empty.\n")
            else:
                self.preOrderTraversal(self.root)

    def findMin(self,node):
        while node.left:
            node = node.left
        
        return node
    
    def transplant(self,u,v):
        if u.parent == None:
            self.root = v

        elif u == u.parent.left:
            u.parent.left = v

        else:
            u.parent.right = v
        
        if v != None:
            v.parent = u.parent

    def deleteRequest(self,ID):
        deleteNode = self.searchRequest(ID)

        if deleteNode is None:
            return False
        
        if deleteNode.left == None:
            self.transplant(deleteNode,deleteNode.right)
            return True
        
        elif deleteNode.right == None:
            self.transplant(deleteNode,deleteNode.left)
            return True

        else:
            y = self.findMin(deleteNode.right)

            if y.parent != deleteNode:
                self.transplant(y,y.right)
                y.right = deleteNode.right
                y.right.parent = y

            self.transplant(deleteNode,y)
            y.left = deleteNode.left
            y.left.parent = y
            return True

