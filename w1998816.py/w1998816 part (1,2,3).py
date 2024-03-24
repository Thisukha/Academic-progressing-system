# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: 20220227 / w1998816 
 
# Date: 17/04/2023


## Setting up separate variables for progress    
Progress = 0
trailer = 0
retriever = 0
Exclude = 0
count = 0
t_results = []
outcomes = 0
data = []
student_IDs = []
total_results = []
outcome = None



#creating the list for part 2
def list():
    print('')
    print("Part 2")
    print('')#To get space
    for l in data:
        print(l)


#creating html file
def file():
    print("part 03")
    print("")
    text_file = open ("Output.txt" , "w+")
    for l in data:
        text_file.write(l + '\n')
    text_file.close()

        #printing  out the text file
    output_text = open ("Output.txt" , "r")
    read = output_text.read()
    print (read)
    output_text.close()
        
   
#determining if the credit range is between 0 and 20, 40 to 60, 80 to 100, and 120
def r_Chek(z):
    Valid_digits = [0, 20, 40, 60, 80, 100, 120]
    if z in Valid_digits:
        return True
    else:
        print("out of range")  #displaying an out-of-range error
        return False


#To determine the progression outcome, function is used.
def p_Out_Come(P_Mark, D_Mark, F_Mark, T_Mark):
    if P_Mark == 120:
        print("Progress")
        outcome = "Progress"
        data.append(f"Progress - {P_Mark},{D_Mark},{F_Mark}")
        global Progress
        Progress += 1

    elif (P_Mark == 100):
        print("Progress(module trailer)")
        outcome = "trailer"
        data.append(f"Progress (module trailer) - {P_Mark},{D_Mark},{F_Mark}")
        global trailer
        trailer += 1

    elif((P_Mark < 100) and (P_Mark+D_Mark)>=60):
        print("Do not progress - module retriever")
        outcome = "retriever"
        data.append(f"Do not progress - {P_Mark},{D_Mark},{F_Mark}")
        global retriever
        retriever += 1

    elif(P_Mark <= 40) and (F_Mark >= 80):
        print("Exclude")
        outcome = "Exclude"
        data.append(f"Exclude - {P_Mark},{D_Mark},{F_Mark}")
        global Exclude
        Exclude += 1

        
#adjusting the loop's execution based on the user's answer to accommodate various inputs
print('')#To get space
print("Part 1")
print('')#To get space




while response == 'y':
        try:
            P_Mark = int(input("Please enter your credits at pass :"))#Enter your credit mark
            r_Chek(P_Mark)
            D_Mark = int(input("Please enter your credit at defer :"))#Enter your defer mark
            r_Chek(D_Mark)
            F_Mark = int(input("Please enter your credit at fail :"))#Enter your faill mark
            r_Chek(F_Mark)
        except ValueError:
            print('Integer Required')
            print('') #Get space within lines
            continue

        
        T_Mark = P_Mark + D_Mark + F_Mark
        if T_Mark != 120:
            print("Total wrong")#display error for total incorrect
            break
            print("")   #To get space


        #With the input data, determine the result
        p_Out_Come(P_Mark, D_Mark, F_Mark, T_Mark)
        t_results.append("{outcomes} - {P_Mark}, {D_Mark}, {F_Mark}")


        question = input('''
Would you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view results: ''')


        if question == 'y':# If user willing to enter another data set, then count and total_marks variables will be assigned to zero and programme loops.
            print("")#To get space
            continue

        elif question == 'q': # This condition will break the loop and display the histogram , if user willing to exit.
            decision = False
            
            
            list()
            print("")
            file()
            




            break

        

















        
