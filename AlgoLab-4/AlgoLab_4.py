import unittest
from Bruteforce import knapsack_brute_force, fractional_bruteforce  
from Greedy import fractional_greedy_knapsack
from Dynamic import knapsack_0_1_dp


#(BF_max_value,BF_inclusion)=knapsack_brute_force(values, weights, 18)
#(G_max_value,G_inclusion)=fractional_greedy_knapsack(values, weights, 18)
#print("Brute-Force")
#print(BF_max_value)
#print(BF_inclusion)
#print("Greedy")
#print(G_max_value)
#print(G_inclusion)
class TestSum(unittest.TestCase):
 
    def test_01Bruteforce(self):
        values = [15, 10, 7, 25, 30]
        weights = [2, 5, 3, 10, 8]
        (BF_max_value,BF_inclusion)=knapsack_brute_force(values, weights, 19)
        
        self.assertEqual(BF_max_value,62)
    
    def test_F_Bruteforce(self):
        values = [15, 10, 7, 25, 30]
        weights = [2, 5, 3, 10, 8]
        FBF_max_value=fractional_bruteforce(values, weights, 19)
        
        self.assertEqual(FBF_max_value,66.25)

    def test_Greedy(self):
        values = [15, 10, 7, 25, 30]
        weights = [2, 5, 3, 10, 8]
        (G_max_value,G_inclusion)=fractional_greedy_knapsack(values, weights, 19)
        
        self.assertEqual(G_max_value,64.5)
    def test_dynamic(self):
        values = [15, 10, 7, 25, 30]
        weights = [2, 5, 3, 10, 8]
        (D_max_value,D_inclusion)=knapsack_0_1_dp(values, weights, 18)
        self.assertEqual(D_max_value,62)
 
if __name__ == '__main__':
    unittest.main()