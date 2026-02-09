# Name: Muhammad Hanan
# Student Number: 501243664
# CPS109 Assignment 
'''
Often when at the gym one has the difficulty of knowing the desired workweight to be put on the barbell, but not
knowing how with the plates provided. The calculator below solves this problem, taking into consideration the weight
of the barbell and different possible plates to output the most efficient way to load plates on the barbell. It is
important to warmup before exercising, and so I have created a warmup calculator, taking workweight and a barbell
weight from the user and outputting warmup sets. I hope you enjoy.
'''
'''
The below function is the barbell weight calculator, it takes an input of desired workweight
and outputs the plates needed.
'''
def read_input_file(f):
    with open(f, 'r') as file:
        
        lines = file.readlines()
    weights = []
    for i in lines:
        weights.append(float(i.strip())) 
        return

def write_output_file(f, output):
    with open(f, "w") as file:
        file.write(output)

def weightcalculator():
    # This allows the user to input custom plates if their gym has them(e.g. 35lbs)
    userChoice = input('Would you like to use custom plates or default plates for calculations?(custom/default) ').lower()
   
    # Making sure that the user chooses a valid option
    while userChoice != 'default' and userChoice != 'custom':
        print('Choose a valid mode')
        userChoice = input('Custom plates or default plates? ')
    
    # If the user chooses the default plate setting, the weights are defined in the list below
    if userChoice == 'default':
        weights = read_input_file("weights.txt") # It reads the input for a text file 
    
    # If the user chooses a custom weight setting, the user populates the list below
    elif userChoice == 'custom':
        weights = []
        numberofplates = int(input('How many different denominations of plates do you have at your gym? Max 6: '))
        while numberofplates > 6 or numberofplates == False or numberofplates < 0:
            numberofplates = int(input('Maximum of 6 plates! Please select a valid number: '))
        while len(weights) < numberofplates:
            weights.append(float(input('Input the plates at your gym from greatest to least (one at a time): ')))

    # User input for calculations:
    workWeight = int(input('Input a work weight in pounds: '))
    desiredWeight = workWeight
    barbellWeight = int(input('How heavy is your barbell? '))
    
    # Subtract the weight of the barbell from the workweight and divide by two in order to consider
    # only the weight of one side of the barbell
    workWeight -= barbellWeight
    workWeight /= 2
    
    # Plates list to be populated by executing the logic below, this is printed at the end of the function
    plates = []

    # Main work loop, each index of the list is checked, if it is less than the workWeight, it is subtracted by the
    # index and the index is appended to the list plates. The loop then restarts. This logic is executed until the
    # weight is lower than 2.5(the lowest increment plate)
    while workWeight >= 2.5:
        if weights[0] <= workWeight:
            workWeight -= weights[0]
            plates.append(weights[0])
            continue
        elif weights[1] <= workWeight:
            workWeight -= weights[1]
            plates.append(weights[1])
            continue
        elif weights[2] <= workWeight:
            workWeight -= weights[2]
            plates.append(weights[2])
            continue
        elif weights[3] <= workWeight:
            workWeight -= weights[3]
            plates.append(weights[3])
            continue
        elif weights[4] <= workWeight:
            workWeight -= weights[4]
            plates.append(weights[4])
            continue
        elif weights[5] <= workWeight:
            workWeight -= weights[5]
            plates.append(weights[5])
            continue

    # Check if there is still weight remaining to be put on the barbell. This is unachievable with the given plates.
    # The print statement states this and provides the next best thing(the list of plates)
    if workWeight > 0:
        print('It is impossible to get to a weight of', desiredWeight,
              'lbs with the plates and barbell provided, the closest next thing would be the following plates on '
              'each side: ')
        print(plates)
   
    # The list of plates is printed
    else:
        print('These are the plates that must be put on each side with the plates and barbell provided: ')
        print(plates)


# The function below is for the warmup sets for a given workweight and barbell weight given by the user.
def warmupsets():
    
    # User inputs are collected for calculations
    workWeight = int(input('What is your desired work weight?(lbs) '))
    barbellWeight = int(input('How heavy is your barbell?(lbs) '))
    
    # warmupWeight initialized to 0, it will gradually go up with each set, until equalling the workweight
    # Counter used to make sure that there is only three repetitions and differentiate between sets
    # warmup# variables created to store the values for each warmup set
    warmupWeight = 0
    counter = 0
    warmup1 = 0
    warmup2 = 0
    warmup3 = 0
    
    # The while loop will keep going until the user will have reached their desired workweight
    while warmupWeight != workWeight:
        counter += 1
        if counter == 1:
    
            # This assigns warmup1 to barbell weight, the first set is a warmup with the barbell
            warmupWeight = barbellWeight
            warmup1 = warmupWeight
        elif counter == 2:
            
            # Assigns warmup2 to half of workweight
            warmupWeight = workWeight * 0.5
            
            # The calculation done below is to ensure that the weight value is reachable
            # given the usual plates in the gym
            warmup2 = (warmupWeight // 5) * 5
        elif counter == 3:
            
            # Warmup with 3/4 times workweight
            warmupWeight = workWeight*0.75
            
            # Ensure that weight is achievable given the usual plates at the gym
            warmup3 = (warmupWeight // 5) * 5
            
            # Assign warmupWeight to workWeight in order to break the while loop and proceed to print statements
            warmupWeight = workWeight
    
    # Print statements with the given warmup sets
    first = ('Your first set of warmups is with the bar: ' + str(warmup1) +  ' lbs')
    second = ('Your second set of warmups is 8 reps of ' + str(warmup2) +  ' lbs')
    third = ('Your third set of warmups is 8 reps of ' + str(warmup3) +  ' lbs')
    
    print (first)
    print (second)
    print (third)
    output = first + "\n" + second + "\n" + third
    write_output_file("weightoutput.txt", output)

weightcalculator()
warmupsets()
