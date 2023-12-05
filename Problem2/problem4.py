
if __name__ == '__main__':

    # read the input file into list
    input = open('input', "r")
    input = input.readlines()

    # strip newline symbols
    for i in range(len(input)):
        input[i] = input[i].rstrip()

    split_list = []
    number_pool = []
    winning_numbers = []

    # split up and parse each input line to extract numbers

    for card in input:
        card_split = card.split('|')

        # numbers split and generate 2d list
        numbers = card_split[0].split(':')
        numbers = numbers[1].split()
        numbers = [int(x) for x in numbers]
        number_pool.append(set(numbers))

        # winning numbers splits and generate 2d list
        winners = card_split[1].split()
        winners = [int(x) for x in winners]
        winning_numbers.append(set(winners))

    # use set.intersection method to match numbers that are common between
    # the number pool and winning numbers

    score = []

    for i in range(len(number_pool)):
        # print(number_pool[i])
        # print(winning_numbers[i])
        z = number_pool[i].intersection(winning_numbers[i])

        # generate a score for the matches
        match = len(z)

        # if there is a match present, calculate the score and tally it
        if match >= 1:
            score.append(pow(2 ,match -1))

        # for x in range(len(z))

    print(sum(score))
