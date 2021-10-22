import sys
import csv
import time
from math import ceil

start_time = time.time()
# Initial max buying power
max_wallet = 500


# Calculation of the sum of actions prices in the list
def buying_price(lst):
    actions_sum = []
    for item in lst:
        actions_sum.append(item[1])
    return sum(actions_sum)


# Generate a K[actions][capacity] type matrix and find the best possible combination
def knapsack(lst):

    price = max_wallet*10

    matrix = [[0 for x in range(price + 1)] for x in range(len(lst) + 1)]

    for action in range(1, len(lst) + 1):
        for capacity in range(1, price + 1):
            if lst[action-1][1] <= capacity:
                matrix[action][capacity] = max(
                    lst[action-1][2] + matrix[action-1][capacity-lst[action-1][1]],
                    matrix[action-1][capacity]
                )
            else:
                matrix[action][capacity] = matrix[action-1][capacity]

    p = price
    n = len(lst)
    comb = []

    while p >= 0 and n >= 0:
        e = lst[n-1]
        if matrix[n][p] == matrix[n-1][p-e[1]] + e[2]:
            comb.append(e)
            p -= e[1]

        n -= 1

    print('Best combination found: ')
    for c in comb:
        print(c[0])
    print('Price to invest : ~', buying_price(comb)/10, '€ (Rounded up)')
    print('Generated profits: +', matrix[-1][-1], '€ at the end of year 2')
    print('Execution time: ', time.time() - start_time, "seconds")


# Open and process de csv file, converting it to exploitable list
try:
    with open(sys.argv[1], newline='') as csvfile:
        actions = csv.reader(csvfile, delimiter=',', quotechar='|')
        actions_lst = []
        for rows in actions:
            if float(rows[1]) <= 0:
                pass
            else:
                actions_lst.append(
                    [
                        rows[0],
                        int(ceil(float(rows[1])*10)),
                        float(float(rows[1]) * float(
                            rows[2].replace('%', '')) / 100),
                    ]
                )

        knapsack(actions_lst)

except FileNotFoundError:
    print("Selected file doesn't exist, please check the file's name.")
