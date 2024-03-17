n_of_processes = int(input("Enter no. of processes : "))
n_of_resources = int(input("Enter no. of resources : "))
allocation = []
max = []
available = []
need = []
for i in range(n_of_processes):
    allocation.append(list(map(int, input("Enter the allocation for P{} : ".format(i)).split())))
    max.append(list(map(int, input("Enter the max for P{} : ".format(i)).split())))
    n = []
    for j in range(n_of_resources):
        n.append(max[i][j]-allocation[i][j])
    need.append(list(n))
available = list(map(int, input("Enter the available resources : ").split()))
safe_seq = []
while len(safe_seq)<n_of_processes:
    flag = 0
    for i in range(n_of_processes):
        if i in safe_seq:
            continue
        for j in range(n_of_resources):
            if need[i][j]>available[j]:
                break
        else:
            flag = 1
            safe_seq.append(i)
            for j in range(n_of_resources):
                available[j] += allocation[i][j]
    if flag==0:
        print("No safe sequence exists...")
        break
else:
    print("Safe Sequence :", safe_seq)