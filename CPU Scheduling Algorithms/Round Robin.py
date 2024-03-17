#Read the inputs from user
processes = []
n = int(input("Enter no. of processes : "))
for i in range(n):
    name = input("Enter process name : ")
    at = int(input("Enter process arrival time : "))
    bt = int(input("Enter process burst time : "))
    processes.append({"name":name, "at":at, "bt":bt})

#Apply the algorithm
processes = list(PROCESSES)
for process in processes:
    process["left"] = process["bt"]
    process["isEntered"] = False
t_completed = 0
curr_time = 0
available = []
TQ = 3
curr_process = {}
queue = []
while t_completed<n:
    new = []
    for p in processes:
        if p["at"]<=curr_time and p["left"]>0 and (not p["isEntered"]):
            new.append(p)
            p["isEntered"] = True
    new.sort(key=lambda p: p["at"])
    queue.extend(new)
    if curr_process in queue and curr_process["left"]>0:
        queue.remove(curr_process)
        queue.append(curr_process)
    if queue:
        process = queue[0]
    else:
        curr_time = sorted(list(filter(lambda p: p["at"]>curr_time, processes)), key=lambda p: p["at"])[0]["at"]
        continue
    if process["left"]==process["bt"]:
        process["rt"] = curr_time-process["at"]
    if process["left"] > TQ:
        process["left"] -= TQ
        curr_time += TQ
    else:
        curr_time += process["left"]
        process["left"]=0
    if process["left"]==0:
        queue.remove(process)
        process["ct"] = curr_time
        process["tat"] = process["ct"]-process["at"]
        process["wt"] = process["tat"]-process["bt"]
        t_completed += 1
    curr_process = process

#Display the results
print("--- ROUND ROBIN CPU SCHEDULING ALGORITHM ---")
print("\n--- PROCESS TABLE ---")
print("P", "AT", "BT", "CT", "TAT", "WT", "RT", sep="\t")
t_tat = t_wt = t_rt = 0
for p in processes:
    print(p["name"], p["at"], p["bt"], p["ct"], p["tat"], p["wt"], p["rt"], sep="\t")
    t_tat += p["tat"]
    t_wt += p["wt"]
    t_rt += p["rt"]
print("\n")
print("Average TAT =", round(t_tat/n,2))
print("Average WT =", round(t_wt/n,2))
print("Average RT =", round(t_rt/n,2))