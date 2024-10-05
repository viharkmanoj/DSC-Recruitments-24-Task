user_stack = []
again = 'y'

def push(x):
    user_stack.append(x)

def pop():
    if user_stack == []:
        print("no value is in the stack to pop")
    else:
        last_item = user_stack.pop()
        return last_item

def peek():
    if user_stack == []:
        print("No value is in the stach to peek")
    else:
        val = len(user_stack)-1
        return user_stack[val]

def againloop():
    global again
    again = input("Do you want to add another value(y/n): ")
    if again in 'yY':
        again = 'y'
    elif again in 'nN':
        menu()
    else:
        print("Enter valid option..............")
        againloop()


def menu():
    print("\n1.Push\n2.Pop\n3.Peek\n4.Show stack\n5.Exit\n")
    selection = int(input("Choose an option : "))
    if selection == 1:
        while again == 'y':
            to_push = eval(input("Enter the value which has to be pushed : "))
            push(to_push)
            againloop()

    elif selection == 2:
        popped_val = pop()
        print("\nThe popped value is ---->",popped_val)
        print("Executed.......")
        menu()

    elif selection == 3:
        peek_val = peek()
        print("\nThe value at the top ---->",peek_val)
        print("Executed.......")
        menu()

    elif selection == 4:
        print("\nThe stack is ----> ",user_stack)
        print("Executed.......")
        menu()

    elif selection == 5:
        print("Exiting program...")
        return
print("\n--------Design your own stack!--------")   
menu()