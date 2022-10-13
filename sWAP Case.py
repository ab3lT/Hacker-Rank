def swap_case(s):
    n = list(s)
    temp = ""
    for i in n:
        if i == i.upper():
            temp += i.lower()
            
        elif i == i.lower():
            temp += i.upper()
            
    return temp


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)