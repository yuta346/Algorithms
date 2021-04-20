#time complexity: O(vn)
def currency_combination(total, currency_denomination):
    if total<0:
        return False
    num_combinations = [[1]+[0]*total for _ in currency_denomination]

    for i in range(len(currency_denomination)):
        for j in range(1, total + 1):
            if(currency_denomination[i] > j): #if coin in currency_denomination is greater than j, place a value one cell above
                num_combinations[i][j] = num_combinations[i-1][j]
            else:
                exclude_this_coin = (num_combinations[i-1][j] if i >=1 else 0)      

                include_this_coin = (num_combinations[i][j-currency_denomination[i]] if j >= currency_denomination[i] else 0)

                num_combinations[i][j] = (exclude_this_coin + include_this_coin)
    print(num_combinations)
    return num_combinations[-1][-1]
    # if num_combinations[-1][-1] ==0:
    #     return False
    # else:return True
currency_list = [2,3,5,10]
#print(currency_combination(15, currency_list))
