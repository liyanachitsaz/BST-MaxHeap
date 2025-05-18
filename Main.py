import BST
import MaxHeap

tree = BST()
heap = MaxHeap()

while True:
    print("Request managment system:")
    print("1. Add new request")
    print("2. Search request by ID")
    print("3. Delete request by ID")
    print("4. Display BST(pre-order)")
    print("5. Display Maxheap(level-order)")
    print("6. Process a request")
    print("7. Increase priority")
    print("8.Exit\n")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            name = input("Enter name: ")
            ID = int(input("Enter ID: "))
            priority = int(input("Enter priority: "))
            tree.insertRequest(ID, name)
            heap.insertHeap(ID,priority)
            print(" Node inserted in both BST and Max heap.\n")

        except ValueError:
            print(" Invalid type. Please enter an integer.\n")

    elif choice == "2":
        try:
            ID = int(input("Enter ID to search: "))
            result1 = tree.searchRequest(ID)
            if result1:
                print("Expected request found")
                print(f" Name: {result1.name} (ID = {result1.ID})\n")

            else:
                print(" Request not found.\n")

        except ValueError:
            print(" Invalid request.\n")

    elif choice == "3":
        try:
            ID = int(input("Enter request's ID to delete: "))
            result1 = tree.deleteRequest(ID)
            result2 = heap.DeleteNode(ID)

            if result1 and result2:
                print(f"Request with ID {ID} deleted from BST.")
                print(f"Request with ID {ID} deleted from MaxHeap.\n")
            
            else:
                print("request not found.\n")

        except ValueError:
            print("Invalid request.\n")

    elif choice == "4":
        print("Tree contents (Pre-order):")
        tree.printBST()
        print("\n")

    elif choice == "5":
        print("Maxheap contents (level-order):")
        heap.printMaxHeap()
        print("\n")

    elif choice == "6":
        answer = heap.processHighestPriorityRequest(tree)
        if answer:
            print("Highest request's priority deleted from both BST and Max heap")
        else: 
            print("Invalid ID.")

    elif choice == "7":

        try:
            ID = int(input("Enter ID which its priority is going to be changed : "))
            priority = int(input("Enter new priority : "))
            success = heap.increasePriority(ID,priority)

            if success:
                print(f"request's priority changed to {priority}.\n")
            
        except ValueError:
            print("Invalid request.\n")

    elif choice == "8":
       
        answer = input("Are you sure you want to exit the program(y/n)?")
    
        if answer == 'n':
            continue

        elif answer == 'y':
            print("Exiting the program...\n")
            break

        else:
            print("Invalid answer.\n")

    else:
        print("Invalid choice. Please try again.\n")
