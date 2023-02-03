def main():
    ##################################################
    # Comlete your code here
    val1 = int(input("Input your first number: "))
    val2 = int(input("Input your second number: "))
    val3 = int(input("Input your third number: "))
    sum = val1 + val2 + val3
    avg = sum / 3
    print("Values: " , val1 , val2 , val3) 
    print("Totoal: " , sum)
    print(f'Average \t {avg:.2f}')

    ##################################################

    pass


if __name__ == '__main__':
    main()
