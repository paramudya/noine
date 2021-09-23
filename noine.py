def nine(nums):
    lst=[]
    for num in nums:
        satuan = num%10
        if satuan+int(num/10)<9:
            lst.append('impossible') 
            continue
        lst.append(10-satuan)
    return lst

if __name__ == '__main__':
    n = int(input("number of test cases: "))
    ints = list(map(int,input("insert {} integer{} each separated with space:\n".format(n,'' if n <= 1 else 's')).split()))

    try:
        for i in range(n):
            print(nine(ints[i]))
    except:
        print("number of integers you just put in is less than what you said earlier!")