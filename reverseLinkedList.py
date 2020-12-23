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

        # Checks if the list is empty
        if self.head.value == None:

            # Sets the head's value to be the specified value
            self.head.value = valueParam

        # If the list is not empty
        else:

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
        while currNode != None:

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
        while currNode != None:

            # Iterates to the next node in the list
            #currNode = currNode.nextNode 

            # Adds the value of the current node to the list of elements
            listOfElements.append(currNode.value)

            # Iterates to the next node in the list
            currNode = currNode.nextNode

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
            
            # Checks if the index of the iterator is the specified index
            if currIndex == indexParam:

                # Returns the value of the node at the specified index
                return currNode.value

            # Moving to the next node in the list
            currNode = currNode.nextNode
            
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

        # Checks to see if the user wanted to remove the first element
        if indexParam == 0:

            # Sets the head of the list to be the 2nd node in the list
            self.head = self.head.nextNode
        
        # If the user wanted to remove an different element
        else:

            # Variable to store the index of the iterator
            # Starts at index 1 (as opposed to 0)
            currIndex = 1

            # Initializing the iterator to be the 2nd node of the linked list
            currNode = self.head.nextNode

            # Initializes the previous node to be the head of the linked list
            prevNode = self.head

            # While loop to continue indefinitely
            while True:

                # Checks to see if the index of the current node is the specified index
                if currIndex == indexParam:

                    # Changes the pointers to skip over the specified index
                    # Sets the successor of the previous node to be the successor of the current node
                    prevNode.nextNode = currNode.nextNode

                    # Return statement to end the function
                    return

                # Moves to the current node to the next node in the list
                currNode = currNode.nextNode

                # Moves the previous node to the next node in the list
                prevNode = prevNode.nextNode

                # Increments the index of the iterator
                currIndex += 1

    # Function to reverse the linked list specified by the given head node
    def reverseList(self):
            
        # Initializing the previous node as being a null pointer
        prevNode = None

        # While loop to continue while head doesn't refer to a null pointer
        while self.head != None:
    
            # Temporary node variable is set to be the current head node
            tempNode = self.head

            # The current head is moved to the next node in the linked list
            self.head = self.head.nextNode

            # The temporary current node is set to point to the previous node
            tempNode.nextNode = prevNode

            # Sets the new previous node to be the temporary node
            prevNode = tempNode

        # Returns the current previous node 
        # Accounts for the case that the list is empty
        self.head = prevNode

# Initializes the linked list
myList = linked_list()

# Populates the linked list
myList.appendToList(0)
myList.appendToList(1)
myList.appendToList(2)
myList.appendToList(3)
myList.appendToList(4)

# Displays the original linked list
print("\nHere's the original list:")
myList.printList()

# Reverses the linked list
myList.reverseList()

# Displays the reversed linked list
print("\nHere's the reversed list:")
myList.printList()

# Stores the length of the linked list
size = myList.findLength()

# Outputs the size of the linked list
print("\nThe size of the linked list is: " + str(size))

# Stores the value stored at index 3
valueAtIndex3 = myList.findValueAtSpecifiedIndex(3)

# Outputs the value stored at index 3
print("\nThe value at index #3 is: " + str(valueAtIndex3))

# Removes the value stored at index #0 of the linked list
myList.removeNodeAtIndex(0)

# Displays the linked list after removing the value at index 0
print("\nHere's the reversed list after removing the first element:")
myList.printList()

