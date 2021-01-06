from dataclasses import dataclass

@dataclass
class Coins:
    value : int
    deno : []

def minCoins(currency):
    num = len(currency.deno)
    changeOfValue = []

    #Traversing through all deno
    i = num-1
    while(i>=0):
        while(currency.value >= currency.deno[i]):
            currency.value -= currency.deno[i]
            changeOfValue.append(currency.deno[i])
        i -=1

    return changeOfValue 

def main():
    denom = [1,2,5,10,20,100,500,2000]
    money = Coins(2345,denom)
    print("Change Needed = ", money.value)
    change = minCoins(money)
    print("Change Given = ", change)


if __name__ == "__main__":
    main()
