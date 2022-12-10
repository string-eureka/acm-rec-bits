from time import perf_counter, sleep
def main():
    a = int(input(""))
    n = list(map(int,input("").strip().split()))[:a]
    x = [i for i in range(1, n[-1]+1) if i not in n]
    print(x[0])
start_time = perf_counter()

main() 

passed_time = perf_counter() - start_time

print(f"It took {passed_time}") # It took 5.007398507999824