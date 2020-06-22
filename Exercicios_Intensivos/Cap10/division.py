print("Give me two numbers, and I'll divid them.")
print('Enter "q" to quit. ')

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        awser = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero! ")
    else:
        print(awser)

