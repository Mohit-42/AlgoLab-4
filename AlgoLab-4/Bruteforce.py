def knapsack_brute_force(values, weights, capacity):
    n = len(values)
    max_value = 0
    inclusion=[0]*n
    
    for i in range(2**n):
       
        binary = [int(x) for x in bin(i)[2:].zfill(n)]
        total_value = sum([values[j]*binary[j] for j in range(n)])
        total_weight = sum([weights[j]*binary[j] for j in range(n)])
        if total_weight <= capacity and total_value > max_value:
            max_value = total_value
            inclusion=binary
            

    return max_value, inclusion

def fractional_bruteforce(values, weights, capacity):
    n = len(values)
    bit_strings = [bin(x)[2:].rjust(n,'0') for x in range(2**n)]

    max_profit = 0
    

    for s in bit_strings:
       
        profit = 0
        weight = 0

        for i in range(n):
            if s[i] == '1':
                # Add the entire item if weight allows
                if weights[i] <= capacity - weight:
                    profit += values[i]
                    weight += weights[i]
                else:
                    # Add a fraction of the item to fill the remaining capacity
                    fraction = (capacity - weight) / weights[i]
                    profit += fraction * values[i]
                    weight = capacity
                    break

        if profit > max_profit:
            max_profit = profit
           
    return max_profit




