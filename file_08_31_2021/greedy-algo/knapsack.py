'''
problem:
objects = [5,1,2,4,6,7]
profits =[18,7,8,13,6,14]
weights =[6,4,2,8,1,5]
2.Knapsack Problem explained(in this problem values acan be divisable):
        1. we have a objects, it's profit and weight.
        2. here the constraint or the condition is, the knapsack can be filled with <= 15 kgs
        3. if you satisfy the condition then it is a feasible solution
        4. if you maximize profit of given condition then it becomes maxiimization problem (which
            is  optimization problem)
        5. if the solution is feasible and gets maxiimum profit then it is an optimal solution

'''
objects = [5,1,2,4,5,3]
profits =[18,7,8,13,6,14]
weights =[6,4,2,8,1,5]
conditon_weight = 15
profit_weight = [round(profits[x]/weights[y],2) for x in range(len(profits)) for y in range(len(weights)) if x ==y]
#print(profit_weight) # [3.0, 1.75, 4.0, 1.62, 6.0, 2.8]
profit_weight2 =profit_weight.copy()

def findMax():
    maxi_profit =max(profit_weight2)
    if maxi_profit >0:
        for i in range(len(profit_weight2)):
            if profit_weight[i]< maxi_profit:
                profit_weight2[i] =profit_weight[i]

            else:
                profit_weight2[i] =0

    return maxi_profit
def knapsack():
    y =conditon_weight
    k_sack =[]
    while(y>0):
        x =profit_weight.index(findMax())
        if(y <=conditon_weight):
            x_weight =weights[x]
            if(y <x_weight):
                new_weight = y
                weights[x]= weights[x] -y
                x_profit =new_weight*profit_weight[x]
                k_sack.append((new_weight,x_profit))
                y=0
            else:
                x_profit =profit_weight[x]
                weights[x]= 0
                k_sack.append((x_weight,x_profit*x_weight))
                y-=x_weight
    return k_sack





k_sack =knapsack()
total_profit = [k_sack[x][1] for x in range(len(k_sack))]
total_weight = [k_sack[x][0] for x in range(len(k_sack))]

print(f"Sum of Total profit is: {sum(total_profit)} \n"
      f"Total weight is:{sum(total_weight)}")
print("Balance weights remain: ",weights)
