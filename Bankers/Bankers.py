# Taking inputs for no. of resources and processes
def main():
    resources = int(input("\nEnter the no. of resources: "))
    processes = int(input("Enter the no. of processes: "))

    # Instances of Each Resources
    max_resources = [int(i) for i in input("\nEnter instances of each Resource: ").split()]

    print("\n-- Allocated Resources for each process --")
    allocated = [[int(i) for i in input(f"P{j + 1}: ").split()] for j in range(processes)]

    print("\n-- Maximum Resources for each process --")
    max = [[int(i) for i in input(f"P{j + 1}: ").split()] for j in range(processes)]

    # store the total amount of resources that have been allocated to each process
    alloc = [0] * resources

    for i in range(processes):
        for j in range(resources):
            alloc[j] += allocated[i][j]
    print(f"\nTotal Allocated Resources: {alloc}")

    # Displaying the availabe resources
    available = [max_resources[i] - alloc[i] for i in range(resources)]
    print(f"\nTotal Available Resources: {available}\n")

    # calculate the need matrix
    need = []
    for i in range(processes):
        row = []
        for j in range(resources):
            row.append(max[i][j] - allocated[i][j])
        need.append(row)

    # print the need matrix
    print("\n-- Need matrix --")
    for i in range(processes):
        print(need[i])
    print()

    running = [True] * processes
    count = processes
    sequence = []

    while count != 0:

        safe = False
        for i in range(processes):
            if running[i]:
                executing = True

                for j in range(resources):
                    if need[i][j] > available[j]:
                        executing = False
                        break

                if executing:
                    print(f"Process {i+1} is executing")
                    sequence.append(i+1)
                    running[i] = False
                    count -= 1
                    safe = True

                    for j in range(resources):
                        available[j] += allocated[i][j]
                    break
        if not safe:
            print("The processes are in an unsafe state")
            break

        print(f"The process is in a safe state. \nAvailable Resouces: {available}\n")

        # Printing the execution sequence

        if(len(sequence) == processes):
            print("Execution sequence: ", sequence)
        else:
            print("Execution sequence not found")

if __name__ == '__main__':
    main()
