import heapq


class Process:
    def __init__(self, arrivalTime, execTime, pid):
        self.pid = pid
        self.arrivalTime = arrivalTime
        self.execTime = execTime
        self.waitingTime = 0
        self.turnAroundTime = 0


def sjf(process):
    process.sort(key=lambda x: x.arrivalTime)
    time_passed = 0
    ready_queue = []
    heapq.heappush(ready_queue, (process[0].execTime, process[0]))

    pcount = 1
    while len(ready_queue) > 0:
        p = heapq.heappop(ready_queue)[1]
        if p.arrivalTime > time_passed:
            time_passed = p.arrivalTime

        # Calculate waiting and turn around time before pushing the next process
        p.waitingTime = time_passed - p.arrivalTime
        p.turnAroundTime = p.waitingTime + p.execTime

        # updating the total time passed
        time_passed += p.execTime

        while pcount < len(process) and process[pcount].arrivalTime <= time_passed:
            heapq.heappush(ready_queue, (process[pcount].execTime, process[pcount]))
            pcount += 1


def main():
    # inputting the arrival times and execution times of the processes:
    n = int(input("Enter number of processes : "))
    processes = []

    print("Enter arrival & burst time of the processes: ")
    for i in range(n):
        input_str = input(f"P{i + 1}: ")
        numbers_str = input_str.split()
        processes.append(Process(int(numbers_str[0]), int(numbers_str[1]), i+1))

    sjf(processes)
    total_wait = 0
    total_tat = 0

    # displaying waiting and turn around times:
    print("Process    Waiting time    Turn around time")
    for i, process in enumerate(processes, start=1):
        print(f"P{process.pid} \t\t\t\t {process.waitingTime} \t\t\t\t {process.turnAroundTime}")
        total_wait += process.waitingTime
        total_tat += process.turnAroundTime

    print(f"Average: \t    {total_wait / n} \t\t\t {total_tat/ n}")


if __name__ == "__main__":
    main()
