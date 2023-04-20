# Load Balancing

def print_load(load):

    print()
    print("****** Current Load of System ******")
    for i in range(len(load)):
        print(f'Server {i+1} load: {load[i]} processes')
    print()


def balance(s,p):

    load = [0] * s
    for i in range(p):
        load[i % len(load)] += 1
    return load


# Taking inputs and providing options to user

s = int(input("\nEnter no. of servers: "))
p = int(input("Enter no. of processes: "))

while True:

    load = balance(s,p)

    print_load(load)
    print('1. Add Servers')
    print('2. Remove Servers')
    print('3. Add Processes')
    print('4. Add Processes')
    print('5. Exit')

    option = int(input('\nSelect an option: '))

    if option == 1:
        change = int(input('Enter the no. of servers to add: '))
        s += change

    if option == 2:
        change = int(input('Enter the no. of servers to remove: '))
        s -= change

    if option == 3:
        change = int(input('Enter the no. of processes to add: '))
        p += change

    if option == 4:
        change = int(input('Enter the no. of processes to remove: '))
        p -= change

    if option == 5:
        break