#Course work Part 4

# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: [UOW : W1985534], [IIT : 20222070]
# Date: 18/4/2023

def validation (credit):    #Range and Integer Validation
    '''Validate whether the input credits at Pass, Defer and Fail are integer and in the range'''
    notValid = True
    while notValid:
        try:
            credit = int(credit)
            if credit == 120 or credit == 100 or credit == 80 or credit == 60 or credit == 40 or credit == 20 or credit == 0:
                notValid = False
                return credit      
            else:
                print('Out of Range')
                notValid = True
                credit = input('Please enter valid credit again : ')
        except ValueError:
            print ('Integer required')
            notValid = True
            credit = input('Please enter valid credit again : ')

def progressionOutcome():
    '''To check the relevant progression outcome for input credits'''
    if Pass == 120:
        outcome = 'Progress'
    elif Pass == 100:
        outcome = 'Progress (module trailer)'
    elif Fail == 80 or Fail == 100 or Fail == 120:
        outcome = 'Exclude'
    else:
        outcome = 'Do not Progress - module retriever'
    return(outcome)

def loop():
    '''To ask user whether the another set of data to be given and iterate accordingly'''
    while True:
        loopAgain = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
        loopAgain = loopAgain.lower()
        if loopAgain == 'y':
            return 1
        elif loopAgain == 'q':
            return 0
        else:
            print('Enter Valid Option')

while True:
    try:
        print('1. Student Version \n2. Staff Version \n3. Quit')
        option = int(input('Enter your option number : '))
    
    
        if option == 1:
            print('Student Version')
        
            Pass = input('Please enter your credits at pass : ')
            Pass = validation (Pass)
            Defer = input('Please enter your credits at defer: ')
            Defer = validation (Defer)
            Fail = input('Please enter your credits at fail : ')
            Fail = validation (Fail)
        
            if Pass + Defer + Fail == 120: # Total Validation
                print (progressionOutcome())
            else:
                print('Total Incorrect')
        
    
        elif option == 2:
            print('Staff version')

            progressionDict = {}

            looping = 1
            while looping == 1:
                print()
                studentID = input('Enter student ID: ')
                Pass = input('Enter your total PASS credits : ')
                Pass = validation (Pass)
                Defer = input('Enter your total DEFER credits: ')
                Defer = validation (Defer)
                Fail = input('Enter your total FAIL credits : ')
                Fail = validation (Fail)
            
                if Pass + Defer + Fail == 120: # Total Validation
                    print (progressionOutcome())
                                
                    if progressionOutcome() == 'Progress':
                        outcomeList = ['Progress - ',Pass, Defer, Fail]
                        progressionDict [studentID] = outcomeList
                    elif progressionOutcome() == 'Progress (module trailer)':
                        outcomeList = ['Progress (module trailer) - ',Pass, Defer, Fail]
                        progressionDict [studentID] = outcomeList
                    elif progressionOutcome() == 'Do not Progress - module retriever':
                        outcomeList = ['Module retriever - ',Pass, Defer, Fail]
                        progressionDict [studentID] = outcomeList
                    elif progressionOutcome() == 'Exclude':
                        outcomeList = ['Exclude - ',Pass, Defer, Fail]
                        progressionDict [studentID] = outcomeList
                
                    print()
                else:
                    print('Total Incorrect')
                    print()

                looping = loop()

            print('-'*63)
            print('Part 4:')
            for studentID in progressionDict.keys():
                print(studentID,': ',progressionDict[studentID][0],end = '')
                print(*progressionDict[studentID][1:],sep = ', ', end = ' ')
            print('\n','-'*63)
#Reference to print list without brackets and seperate with comma - https://www.javatpoint.com/how-to-print-a-list-without-brackets-in-python        
        
        elif option == 3:
            break
        else:
            print('Invalid option')

    except ValueError:
        print('Integer required')
