def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")
    
    dp = [float('inf')] * (target + 1)
    dp[0] = 0
    previous_coin = [0] * (target + 1)
    
    for i in range(1, target + 1):
        for coin in coins:
            if i - coin >= 0:
                candidate = dp[i - coin] + 1

                if candidate < dp[i]:
                    dp[i] = candidate
                    previous_coin[i] = coin

    if dp[target] == float('inf'):
        raise ValueError("can't make target with given coins")

    result = []
    while target > 0:
        coin = previous_coin[target]
        result.append(coin)
        target -= coin

    return result