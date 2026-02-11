if __name__ == "__main__":

    temperatures = [15.5, 17.2, 14.8, 16.0, 18.3, 20.1, 19.5]

    print(f"Wednesday: {temperatures[2]}")
    print(f"Max: {max(temperatures)}")
    print(f"Min: {min(temperatures)}")

    avg = sum(temperatures) / len(temperatures)
    print(f"Average: {round(avg, 1)}")

    count = 0
    for temp in temperatures:
        if temp > 17:
            count += 1
    print(f"Days above 17: {count}")

    print(f"Sorted: {sorted(temperatures)}")
