Request Management System using BST and Max Heap

This project is a simple request management system implemented using a priority queue that combines a Binary Search Tree (BST) and a Max Heap. Each request includes a name, ID, and priority. The system allows users to insert, search, delete, and process requests using these two fundamental data structures.

📂 Project Structure

BST.py – Implements a Binary Search Tree for storing requests and performing operations based on Name and ID.
MaxHeap.py – Implements a Max Heap for managing requests based on their Priority and ID.
Main.py – Contains a CLI interface that displays a menu, allowing users to interact with the system.

🚀 Features

The following operations are available via the menu:

Insertion: Register requests with ID, name, and priority in both the BST and Max Heap.
Search: Search for requests based on their ID.
Delete: Delete requests using their ID.
Display BST: Show pre-order traversal of the BST.
Display Max Heap: Show level-order traversal of the Max Heap.
Process a Request: Process and remove the highest-priority request from both the BST and Max Heap.
Increase Priority: Increase the priority of a specific request.
🛠️ How to Run

To run the program:

```bash
python Menu.py
```
📦 Requirements

Python 3.x
No external libraries required

🧪 Example Use Cases

Demonstrates how pre-order traversal changes when a request is deleted:

Add new requests with different priority levels
Display pre-order traversal
Delete a request based on its ID
Display updated pre-order traversal

📌 Notes

Ensure each task has a unique ID.
Requests are stored in both structures for greater flexibility.

🧑‍💻 Author

This project was created to gain a deeper understanding of data structure concepts, particularly BSTs and Max Heaps.
