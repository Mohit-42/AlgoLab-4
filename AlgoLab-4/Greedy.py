
    
def fractional_greedy_knapsack(values,weights,capacity):
    n = len(values)
    items = [(values[i], weights[i]) for i in range(n)]
    ratios = [(items[i][0] / items[i][1], items[i][0], items[i][1]) for i in range(n)]
    sorted_items = sorted(ratios, key=lambda x: x[0] / x[1], reverse=True)

    max_value = 0 
    knapsack = []  

    for ratios, value, weight in sorted_items:
        if capacity >= weight:
            knapsack.append((value,weight))
            max_value += value
            capacity -= weight
        else:
            fraction = capacity / weight
            partial_value = fraction * value
            knapsack.append((partial_value, weight))
            max_value += partial_value
            break

    return max_value, knapsack
