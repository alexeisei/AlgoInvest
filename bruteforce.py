from itertools import combinations
import csv
import time

start_time = time.time()
# Initial max buying power
max_wallet = 500


# Calculation of profits from an actions list
def profit_calculation(lst):
    profits = []
    for action in lst:
        profits.append(action[1] * action[2] / 100)
    return sum(profits)


# Calculation of the sum of actions prices in the list
def buying_price(lst):
    actions_sum = []
    for item in lst:
        actions_sum.append(item[1])
    return sum(actions_sum)


# Creation and iteration through every possible combination to find the most optimal one
def find_combination(lst):

    actions_list = lst
    profit = 0

    for i in range(len(actions_list)):

        combis = combinations(actions_list, i + 1)
        for combi in combis:
            total_sum = buying_price(combi)
            if total_sum <= max_wallet:
                total_profit = profit_calculation(combi)

                if total_profit > profit:
                    profit = total_profit
                    best_combination = combi

    print('Best possible combination: ')
    for comb in best_combination:
        print(comb)
    print('Total buying price: ', buying_price(best_combination), '€')
    print('Profits from this combination: +', profit, '€ at the end of year 2')
    print('Execution time of algorithm: ', time.time() - start_time, "seconds")


# Open and process de csv file, converting it to exploitable list
try:
    with open(f'data_set/actions.csv', newline='') as csvfile:
        actions = csv.reader(csvfile, delimiter=',', quotechar='|')
        actions_lst = []
        for rows in actions:
            actions_lst.append(
                [
                    rows[0],
                    float(rows[1]),
                    float(rows[2].replace('%', ''))
                ]
            )

        find_combination(actions_lst)

except FileNotFoundError:
    print("Selected file doesn't exist, please check the file's name.")
