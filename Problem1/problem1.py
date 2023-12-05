
if __name__ == '__main__':

    #read the input file into list
    input = open('input', "r")
    input = input.readlines()

    #strip newline symbols
    for i in range(len(input)):
        input[i] = input[i].rstrip()


    #empty key list to store first and last values
    key_list = []

    for i in range(len(input)):

        #store single line from input to line variable
        line = input[i]

        line_list = []
        #for each element in the string, store it the the 'line_list' if it is a digit
        for element in line:
            if element.isdigit():
                line_list.append(element)

        #append the keylist to include a string combination of the first and last digits
        key_list.append(line_list[0]+line_list[-1])

    #convert key_list into numbers
    numbers = [int(x) for x in key_list]

    print(sum(numbers))
