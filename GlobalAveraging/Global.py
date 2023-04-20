# creating a class for nodes

class Node:
    def __init__(self):
        self.hours = 0
        self.mins = 0
        self.name = ""
        self.node_time_diff_list = []
        self.avg_time_diff = 0

agreed_time_hr = int(input("\nEnter the agreed time in hours: "))
agreed_time_mins = int(input("Enter the agreed time in minutes: "))

initial_time_hr = int(input("\nEnter the initial time in hours: "))
initial_time_mins = int(input("Enter the initial time in minutes: "))

# Calculating time difference between agreed and initial time minutes

time_diff = (agreed_time_hr - initial_time_hr) + (agreed_time_mins - initial_time_mins)

# Creating nodes containing hours and minutes

n = int(input("\nEnter the number of nodes to synchronize their clock time: "))

# Creating n instances of the Node class and set their local clock times
nodes_li = []
for i in range(1,n+1):
    node = Node()
    node.name = f"Node '{chr(64+i)}'"
    node.hours = int(input(f"\nEnter the local clock time in hrs for {node.name}: "))
    node.mins = int(input(f"Enter the local clock time in minutes for {node.name}: "))
    nodes_li.append(node)


time_elapsed = 5
time_diff_li = []

# Calculating time difference for each node

iterations =  int(time_diff / time_elapsed) + 1

for i in range(iterations):

    diff_li = []
    print(f"\nStep {i+1} current time:")

    for node in nodes_li:

        print(f"{node.name} = {node.hours}:{node.mins}")
        curr_diff = (node.hours - agreed_time_hr) + (node.mins - agreed_time_mins)
        diff_li.append(curr_diff)
        node.node_time_diff_list.append(curr_diff)

        # updating the local time of all nodes after the time has elapsed
        if i != iterations:
            node.mins += time_elapsed

    print(f"Skeww after step {i+1}: {diff_li}")
    print("")
    time_diff_li.append(diff_li)

ctr = 1
no_of_nodes = len(nodes_li)

avg_li = []

for n in nodes_li:

    sum_diff = 0
    for diff in n.node_time_diff_list:
        sum_diff += diff

    avg_li.append((sum_diff/no_of_nodes))
    n.avg_time_diff = sum_diff/no_of_nodes

print(f"Average List: {avg_li}")

# Calculating the common time difference

common_time_diff = []
second_li = []

for i in range(no_of_nodes):

    res = 0
    min_part = int(avg_li[i]/1)
    sec_part = avg_li[i] % 1
    second_li.append(sec_part)

    if(avg_li[i] < 0):
        res = nodes_li[i].mins + abs(min_part)
    else:
        res = nodes_li[i].mins - min_part

    common_time_diff.append(res)

results = []

for i in range(no_of_nodes):

    n = nodes_li[i]
    if n.avg_time_diff % 1 >= 0.5:
        results.append(str(n.hours) + ":" + str(common_time_diff[i]) + ":" + str(30))
    else:
        results.append(str(n.hours) + ":" + str(common_time_diff[i]))

print(f"\nResults: {results}\n")