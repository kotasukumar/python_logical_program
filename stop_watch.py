def elapsed_time(start, end):
    return start - end


if __name__ == "__main__":
    start = float(input("Enter the start time: "))
    end = float(input("Enter the end time: "))
    time = elapsed_time(start, end)
    print("Elapsed time is: ", time)
