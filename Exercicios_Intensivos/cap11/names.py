from name_function import get_formatted_name

print("Enter 'q' ant any time do quit. ")
while True:
    first= input("\nPlease give me a fisrt name: ")
    if first == 'q':
        break
    last = input("\nPlease give me a last name: ")
    if last == 'q':
        break

    formatted_name=get_formatted_name(first,last)
    print(f'\tNeatly formatted name: {formatted_name}')