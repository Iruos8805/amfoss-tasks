
def find_town_to_journey(n, times):
    min_time = min(times)
    
    if times.count(min_time) == 1:
        return times.index(min_time) + 1
    else:
        return "Still Aetheria"

def main():
    n = int(input())
    times = list(map(int, input().split()))
    
    result = find_town_to_journey(n, times)
    print(result)

if __name__ == "__main__":
    main()
