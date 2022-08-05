class Friend_Circle:
    def __init__(self):
        self.friends_list = {} #containing entries for students with list for each student has his/her friends listed.
        self.considered = [False] #list to help perform DFS to see indirect friends.
        
    # Function to add frinedship between students (adding edge between given nodes in a graph)
    def friends(self, student1, student2):
        #look for nodes in graph if not present add them before adding edge.
        if student1 not in self.friends_list:
            self.friends_list[student1] = []
            self.considered.insert(student1, False)

        if student2 not in self.friends_list:            
            self.friends_list[student2] = []
            self.considered.insert(student2, False)
            
        #adding the students to friendlist of each other    
        self.friends_list[student1].append(student2)
        self.friends_list[student2].append(student1)

    #Function to break up the friendship between students
    def breakUp(self, student1, student2):
        #Check if students exists
        if student1 in self.friends_list and student2 in self.friends_list:
            #check if students are friends with each other
            if student2 in self.friends_list[student1] and student1 in self.friends_list[student2]:
                self.friends_list[student1].remove(student2)
                self.friends_list[student2].remove(student1)
            else:
                print("Error:trying breakup students who are not friends", student1, student2)
        else:
            print("Error:trying to breakup students who are not registered!", student1, student2)
    
    # Funtion performing DFS to search the friends.
    def findNumberOfFriends(self, student):
        number_of_friends = 0
        self.considered[student] = True
        for itr in self.friends_list[student]:
            if self.considered[itr] == True:
                continue
            number_of_friends += 1 # to consider current student
            self.considered[itr] = True 
            number_of_friends += self.findNumberOfFriends(itr) # traverse through current student's friends using recursion.
        return number_of_friends

    #Function to find total number of students student0 can talk to and writing the result to output file.                 
    def total(self):
        result = self.findNumberOfFriends(0)
        try:
            outputFile = open("outputPS14.txt", "a+")
        except Exception:
            print("Output file could not be opened!")
        
        outputFile.write(str(result))
        outputFile.write("\n")
        outputFile.close()
        self.considered = [False] * len(self.considered) #reset the considered values for all students to False

    # function to print friends list of all students. 
    def printFriends(self):
        for itr in self.friends_list:
            print(f"Friends of student{itr}:", self.friends_list[itr])
        print(self.friends_list)

            

if __name__ == '__main__':

    FC = Friend_Circle()
    #Flush the previous contents of output.txt file
    try:
        open("outputPS14.txt", "w").close()
    except Exception:
        print("Output File Could not be opened!")

    try:
        inputFile = open("inputPS14.txt", "r")
    except Exception as E:
        print(type(E))
        print("Input File Could not be opened")
    
    input_line = inputFile.readline()
    #looping through the entire input file
    while input_line:
        input_command = input_line.split()
        if input_command[0] == "friends":
            FC.friends(int(input_command[1]), int(input_command[2]))
        elif input_command[0] == "total":
            FC.total()
        elif input_command[0] == "breakUp":
            FC.breakUp(int(input_command[1]), int(input_command[2]))
        else:
            print("UnExpected input received!")
        input_line = inputFile.readline()
        #FC.printFriends()       
    inputFile.close()
    
    
