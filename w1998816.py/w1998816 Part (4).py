# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 

# Student ID: 20220227 / w1998816 
 
# Date: 17/04/2023


#determining if the credit range is between 0 and 20, 40 to 60, 80 to 100, and 120
def r_Chek(z):
    validdigits = [0,20,40,60,80,100,120]
    if z in validdigits:
        return True
    else:
        print("Out of range") #displaying an out-of-range error
        print('') #To get space
        return False


# Setting up separate variables for progress  
Progress = 0
trailer = 0
retriever = 0
Exclude = 0
total = 0
outcomes = 0
results = {}
t_results = []
student_IDs = []


#To determine the progression outcome, function is used.
def p_Out_Come(P_Mark, D_Mark, F_Mark, T_Mark):
    if P_Mark == 120:
        print("Progress")
        global Progress
        Progress += 1
    elif (P_Mark == 100):
        print("Progress(module trailer))")
        global trailer
        trailer += 1
    elif (P_Mark < 100) and (P_Mark+D_Mark)>=60:
        print("Do not progress - module retriever")
        global retriever
        retriever += 1
    elif ((P_Mark <= 40) and (F_Mark >= 80)):
        print("Exclude")
        global Exclude
        Exclude += 1


#Validating the ID to be unique
def validID(S_ID):
    global student_IDs
    for i in range(0, len(student_IDs)):
        if S_ID == student_IDs[i]:
            return True
        else:
            return False


#adjusting the loop's execution based on the user's answer to accommodate various inputs
print('')#To get space
print("Part 1")
print('')#To get space
response = 'y'



while response == 'y':
    while True:
        S_ID = input('Enter Student ID : ')
        print("")#To get space
        if validID(S_ID):
            print('The ID you entered already exists') #To check whether the ID already exists
            continue
        else:
            student_IDs.append(S_ID)
        try:
          P_Mark = int(input('Please enter your credits at pass: '))#Enter your credit mark
          r_Chek(P_Mark)
          D_Mark = int(input('Please enter your credits at defer: '))#Enter your defer mark
          r_Chek(D_Mark)
          F_Mark = int(input('Please enter your credits at fail: '))#Enter your faill mark
          r_Chek(F_Mark)
        except ValueError:
          print('Integer Required')
          print('') #To get space
          continue

        
        T_Mark = P_Mark+D_Mark+F_Mark
        if T_Mark != 120:
            print('Total incorrect') #display error for total incorrect
            print('')
            break


        #With the input data, determine the result
        p_Out_Come(P_Mark, D_Mark, F_Mark, total)
        t_results.append(f"{outcomes} - {P_Mark}, {D_Mark}, {F_Mark}")

        
        #Feeding the dictionary with deleted list data
        for i in range(0,len(t_results)):
            results.update({S_ID:t_results[i]})
        outcomes += 1
        break


    
    print('') #To get space



    question = input('''
Would you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view results: ''')

    if question == 'y':# If user willing to enter another data set, then count and total_marks variables will be assigned to zero and programme loops.
            print("")#To get space
            continue

    elif question == 'q': # This condition will break the loop and display the histogram , if user willing to exit.
        decision = False
        print("")#To get space
               

        #searching the dictionary repeatedly to print the desired result
        for z in results:
            print(z,results[z])

        break
