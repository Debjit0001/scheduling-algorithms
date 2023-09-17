import collections


class Process:
    def __init__(self, arrivalTime, execTime):
        self.arrivalTime = arrivalTime
        self.lastCPU = arrivalTime
        self.execTime = execTime
        self.waitingTime = 0
        self.turnAroundTime = 0


def rr(process, tq):
    # sorting the processes with respect to their arrival times
    process.sort(key=lambda x: x.arrivalTime)

    ready_queue = collections.deque()
    ready_queue.append(process[0])

    time_passed = process[0].arrivalTime
    pcount = 1

    while len(ready_queue) > 0:
        p = ready_queue.popleft()
        p.waitingTime += time_passed - p.lastCPU

        if p.execTime > tq:
            p.execTime -= tq
            time_passed += tq
            p.turnAroundTime += tq
        else:
            time_passed += p.execTime
            p.turnAroundTime += p.execTime + p.waitingTime
            p.execTime = 0

        p.lastCPU = time_passed

        while pcount < len(process) and process[pcount].arrivalTime <= time_passed:
            ready_queue.append(process[pcount])
            pcount += 1

        if p.execTime > 0:
            ready_queue.append(p)


def main():
    # inputting the arrival times and execution times of the processes:
    n = int(input("Enter number of processes : "))
    processes = []

    print("Enter arrival & burst time of the processes: ")
    for i in range(n):
        input_str = input(f"P{i + 1}: ")
        numbers_str = input_str.split()
        processes.append(Process(int(numbers_str[0]), int(numbers_str[1])))

    tq = int(input("Enter the time quanta: "))

    rr(processes, tq)
    total_wait = 0
    total_tat = 0

    # displaying waiting and turn around times:
    print("Process    Waiting time    Turn around time")
    for i, process in enumerate(processes, start=1):
        print(f"P{i} \t\t\t\t {process.waitingTime} \t\t\t\t {process.turnAroundTime}")
        total_wait += process.waitingTime
        total_tat += process.turnAroundTime

    print(f"Average: \t    {total_wait / n} \t\t\t {total_tat / n}")


if __name__ == "__main__":
    main()
