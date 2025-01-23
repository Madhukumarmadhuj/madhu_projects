max_lines=3
max_bet=100
min_bet=1

def deposit():
    while True:
        amount=input("enter a amount")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("enter a greater than zero number")
        else:
            print("enter the value or digit not string")
    return amount

def lines_of_bet():
    while True:
        lines=input("enter the lines")
        if lines.isdigit():
            lines=int(lines)
            if 1<=lines<=max_lines:
                break
            else:
                print("enter a line number 1,2,3")
        else:
            print("enter a number")
    return lines
def get_bet():
    while True:
        bet_amount=input("enter the amount")
        if bet_amount.isdigit():
            bet_amount=int(bet_amount)
            if min_bet<=bet_amount<=max_bet:
                break
            else:
                print(f"enter the amount between {min_bet} and {max_bet} bet amount")
        else:
            print("enter the number")
    return bet_amount
def main():
    balance=deposit()
    lines=lines_of_bet()
    while True:
        bet=get_bet()
        totalbet=bet*lines
        if totalbet>balance:
            print(f"you have not enough money to bet{balance} and {totalbet}")
        else:
            break
    print(f"bet {bet} and {lines} and total bet equalls to{totalbet}")
main()
