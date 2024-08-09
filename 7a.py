class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print(f"Stack: {self.stack}")

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print(f"Queue: {self.queue}")

# Function to handle stack operations with user input
def handle_stack_operations():
    stack = Stack()
    while True:
        print("\nStack Operations:")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            item = input("Enter item to push: ")
            stack.push(item)
        elif choice == '2':
            print(stack.pop())
        elif choice == '3':
            stack.display()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

# Function to handle queue operations with user input
def handle_queue_operations():
    queue = Queue()
    while True:
        print("\nQueue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            item = input("Enter item to enqueue: ")
            queue.enqueue(item)
        elif choice == '2':
            print(queue.dequeue())
        elif choice == '3':
            queue.display()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

# Main function to choose between stack and queue operations
def main():
    while True:
        print("\nMain Menu:")
        print("1. Stack Operations")
        print("2. Queue Operations")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            handle_stack_operations()
        elif choice == '2':
            handle_queue_operations()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
