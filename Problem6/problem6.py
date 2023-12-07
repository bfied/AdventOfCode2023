
def problem6(filename):
    # read the input file into list
    input = open(filename, "r")
    input = input.readlines()

    # strip newline symbols
    for i in range(len(input)):
        input[i] = input[i].rstrip()




    times = input[0].split(':')
    times = times[1].split()
    times = [int(x) for x in times]


    distances = input[1].split(':')
    distances = distances[1].split()
    distances = [int(x) for x in distances]

    # iterate through each combination of times and distances
    winner_count = []
    for t,record in zip(times,distances):


        # for a given distance 't', iterate through each millisecond value to see if the resulting
        # velocity will beat the record
        winners = 0
        for i in range(t):
            # i is current millisecond value
            velocity = i
            time_remaining = t - i
            distance_traveled = velocity * time_remaining
            if distance_traveled > record:
                winners += 1


        winner_count.append(winners)

    # Multiply elements one by one
    result = 1
    for x in winner_count:
        result = result * x
    print(result)


    split_list = []
    number_pool = []
    winning_numbers = []


if __name__ == '__main__':
    problem6('input.txt')

    # import timeit
    # print(timeit.timeit("problem6('input.txt')", setup="from __main__ import problem4", number=100))
