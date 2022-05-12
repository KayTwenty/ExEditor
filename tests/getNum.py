def getNum():
    num = input("Enter a number (<Enter> to quit): ")
    sum = 0
    count = 0
    
    while num !="":
        x = eval(num)
        sum = sum + x
        count = count + 1
        result = sum / count 
        num = input("Enter a number (<Enter> to quit): ")
    print("The average of the numbers is {0}".format(result))
        

def main():
    print("This program calculates the average of a undetermined number of inputs")
    getNum()
    input("Press Enter to Quit")

main()

