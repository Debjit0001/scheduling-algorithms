class Process:
    def __init__(self, arrivalTime, execTime):
        self.arrivalTime = arrivalTime
        self.execTime = execTime
        self.waitingTime = 0
        self.turnAroundTime = self.arrivalTime + self.execTime


def fcfs(process):
    time_passed = 0

    for p in process:
        # If the process hasn't arrived yet, wait until it arrives
        if p.arrivalTime > time_passed:
            time_passed = p.arrivalTime

        p.waitingTime = time_passed - p.arrivalTime
        time_passed += p.execTime


def main():
    # inputting the arrival times and execution times of the processes:
    n = int(input("Enter number of processes : "))
    processes = []

    print("Enter arrival & burst time of the processes: ")
    for i in range(n):
        input_str = input(f"P{i + 1}: ")
        numbers_str = input_str.split()
        processes.append(Process(int(numbers_str[0]), int(numbers_str[1])))

    fcfs(processes)
    total_wait = 0
    total_tat = 0

    # displaying waiting and turn around times:
    print("Process    Waiting time    Turn around time")
    for i, process in enumerate(processes, start=1):
        print(f"P{i} \t\t\t\t {process.waitingTime} \t\t\t\t {process.turnAroundTime}")
        total_wait += process.waitingTime
        total_tat += process.turnAroundTime

    print(f"Average: \t    {total_wait/n} \t\t\t {total_tat/n}")


if __name__ == "__main__":
    main()
