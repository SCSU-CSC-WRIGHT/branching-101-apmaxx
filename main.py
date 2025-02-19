"""There are 3 errors in this code. Please use your own ability to find them all. Consider this a Python refresher."""

def calculate_running_total(n):

    total = 0 
    for i in range(n):
        number = int(input("Enter a number: "))
        total += number

    print("The running total is: ",  total)
    return total

def main():
    num_inputs = 5
    calculate_running_total(num_inputs)

if __name__ == "__main__":
    main()