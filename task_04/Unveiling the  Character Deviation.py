
def count_differing_indices(s):
    reference = "amfoss"
    count = 0
    for i in range(10):
        if s[i] != reference[i]:
            count += 1
    return count


def main():
    t = int(input())  
    for _ in range(t):
        s = input() 
        result = count_differing_indices(s)
        print(result)

if __name__ == "__main__":
    main()
