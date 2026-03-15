def invest(amount, rate, years):
    ans = ""

    for i in range(years):
        ans += f"year {i+1}: ${(amount + amount*rate):.2f}\n"
        amount = amount + amount*rate
    
    return ans

print(invest(100, .05, 4))