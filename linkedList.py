# Defining a class for linked list nodes
class node:
    
    # Constructor for the node class
    # Initializes value to None to account for the default constructor
    def __init__(self, valueParam = None):

        # Data member to store the value of the the current node
        # Initialized to be the value specified when the node is initialized        
        self.value = valueParam

        # Pointer to the next node
        # Initialized as null pointer
        self.nextNode = None

# Defining a class for the entire linked list
class linked_list:

    # Constructor for the linked_list class
    def __init__(self):

        # Sets the head of the linked list to be a default node
        self.head = node()

    # Function to add a node to the end of the linked list
    def appendToList(self, valueParam):

        # Creates a new node with the specified value
        newNode = node(valueParam)

        # Pointer to store the node being currently evaluated
        currNode = self.head

        # While loop to continue until next node is a null pointer
        while currNode.nextNode != None:

            # Iterates to the next node of the linked list
            currNode = currNode.nextNode

        # At this point, we're at the end of the list
        # Set the next node of the last element to be the new node
        currNode.nextNode = newNode

    # Function to find the length of our linked list
    def findLength(self):

        # Initializing our list iterator to be the head of the list
        currNode = self.head

        # Variable to store the total number of nodes
        numNodes = 0

        # While loop to continue until the next node is a null pointer
        while currNode.nextNode != None:

            # Increment the total # of nodes that have been encountered
            numNodes += 1

            # Moves to the next node of the list
            currNode = currNode.nextNode
        
        # Returns the total # of nodes found
        return numNodes

    # Function to print out the linked list
    def printList(self):

        # List to store the list of elements that have been encountered
        listOfElements = []

        # Initializing our iterator to be the head of the linked list
        currNode = self.head

        # While loop to iterate to the end of the list
        # Stops when the next node is a null pointer
        while currNode.nextNode != None:

            # Iterates to the next node in the list
            currNode = currNode.nextNode 

            # Adds the value of the current node to the list of elements
            listOfElements.append(currNode.value)

        # Outputs the list of elements
        print(listOfElements)

    # Function to return the value stored at the specified index
    def findValueAtSpecifiedIndex(self, indexParam):

        # Checks if the selected index is greater than the length of the list
        if indexParam >= self.findLength():

            # Outputs an error message
            print("ERROR:  Selected index is out of range!")

            # Return statement to end the function
            return None

        # Variable to store the index of the current node
        currIndex = 0

        # Initializing our list iterator to be the head of the list
        currNode = self.head

        # While loop to continue indefinitely
        while True:

            # Moving to the next node in the list
            currNode = currNode.nextNode

            # Checks if the index of the iterator is the specified index
            if currIndex == indexParam:

                # Returns the value of the node at the specified index
                return currNode.value

            # Increments the index of the iterator
            currIndex += 1

    # Function to remove the node at the given index
    def removeNodeAtIndex(self, indexParam):

        # Checks if the specified index is greater than the length of the linked list
        if indexParam >= self.findLength():

            # Displays an error message
            print("ERROR:  Selected index is out of range!")

            # Return statement to end the function
            return

        # Variable to store the index of the iterator
        currIndex = 0

        # Initializing the iterator to be the head of the linked list
        currNode = self.head

        # While loop to continue indefinitely
        while True:

            # Sets the previous node to be the node being evaluated
            prevNode = currNode

            # Moves to the next node in the list
            currNode = currNode.nextNode

            # Checks to see if the index of the current node is the specified index
            if currIndex == indexParam:

                # Changes the pointers to skip over the specified index
                # Sets the successor of the previous node to be the successor of the current node
                prevNode.nextNode = currNode.nextNode

                # Return statement to end the function
                return

            # Increments the index of the iterator
            currIndex += 1

# Testing
myList = linked_list()

myList.appendToList(0)
myList.appendToList(1)
myList.appendToList(2)
myList.appendToList(3)
myList.appendToList(4)

print("Here's the original list:")
myList.printList()

print("\nThe element at index 3 is: " + str(myList.findValueAtSpecifiedIndex(3)))

myList.removeNodeAtIndex(2)

print("\nAfter Removal:")

myList.printList()
