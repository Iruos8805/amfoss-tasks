
def say_hello(s):
    word = "hello"
    i = 0  
    
    for char in s:
        if char == word[i]:
            i += 1
            if i == len(word):
                return "YES"
    
    return "NO"


def main():
    s = input().strip()
    result = say_hello(s)
    print(result)

if __name__ == "__main__":
    main()
