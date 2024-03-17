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
t_completed = 0
curr_time = 0
available = []
while t_completed<n:
    available = list(filter(lambda p: p["at"]<=curr_time and p["left"]>0, processes))
    if available:
        available.sort(key=lambda p: p["left"])
        process = available[0]
    else:
        curr_time = sorted(list(filter(lambda p: p["at"]>curr_time, processes)), key=lambda p: p["at"])[0]["at"]
        continue
    if process["left"]==process["bt"]:
        process["rt"] = curr_time-process["at"]
    process["left"] -= 1
    curr_time += 1
    if process["left"]==0:
        process["ct"] = curr_time
        process["tat"] = process["ct"]-process["at"]
        process["wt"] = process["tat"]-process["bt"]
        t_completed += 1

#Display the results
print("--- SJF(Preemptive) CPU SCHEDULING ALGORITHM ---")      
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