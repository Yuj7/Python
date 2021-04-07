def changereturn(n):
    changedict ={"dollars":0,"quarters":0, "dimes":0,"nickels": 0, "pennies":0}    
    # if n >= 100:
    #     rem = n%100
    #     changedict["hundred"] = rem
    #     n = n-rem*100
    # if n >= 50:
    #     rem = n%50
    #     changedict["fifty"] = rem
    #     n = n-rem*50
    # if n >= 20:
    #     rem = n%20
    #     changedict["twenty"] = rem
    #     n = n-rem*20
    # if n >= 10:
    #     rem = n%10
    #     changedict["ten"] = rem
    #     n = n-rem*10
    # if n >= 5:
    #     rem = n%5
    #     changedict["five"] = rem
    #     n = n-rem*5

    if n >= 1:
        rem = n/1
        changedict["dollars"] = int(rem)
        n = n-int(rem)*1
    if 1 > n >= 0.25:
        rem = n/0.25
        changedict["quarters"] = int(rem)
        n = n-int(rem)*0.25
    if 0.25>n >= 0.1:
        rem = n/0.1
        changedict["dimes"] = int(rem)
        n = n-int(rem)*0.1
    if 0.1>n >= 0.05:
        rem = n/0.05
        changedict["nickels"] = int(rem)
        n = n-int(rem)*0.05
    if 0.05>n >= 0.01:
        rem = n/0.01
        changedict["pennies"] = int(rem)
        n = n-int(rem)*0.01
        
    print("You will have "+ str(changedict["dollars"])+ " dollars, "+ str(changedict["quarters"])+ " quarters, " + str(changedict["dimes"]) + " dimes, "+ str(changedict["nickels"])+" nickels and " + str(changedict["pennies"])+ " pennies.")


cost = float(input("Enter the cost: "))
amount = float(input("Enter the amount of money given: "))

change = amount - cost

if change ==0:
    print("You will have 0 dollar left.")
elif change < 0:
    print("Sorry, but you need more money.")
else:
    changereturn(change)