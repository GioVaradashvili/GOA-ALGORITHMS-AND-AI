def hw1_try1(a,b,c,):
    return len([i for i in range(a,b)if i % c == 0])

def hw1_try2(a,b,c):
    return (b - a) // c if a % c != 0 or (a % c == 0 and b % c == 0) else (b - a) // c + 1

def hw1_try2_eazy_version(a,b,c):
    if a % c != 0 or (a % c == 0):
        return (b - a) // c
    else:
        return (b - a) // c + 1
    

# ----------------------------------------------------------------

print(hw1_try1(1,20,2))

print(hw1_try2(1,20,2))

print(hw1_try2_eazy_version(1,20,2))

print()

print(hw1_try1(12,19,3))

print(hw1_try2(12,19,3))

print(hw1_try2_eazy_version(12,19,3))

print()

print(hw1_try1(2,20,2))

print(hw1_try2(2,20,2))

print(hw1_try2_eazy_version(2,20,2))

print("/n")

# ----------------------------------------------------------------

def hw2_try1(num,b):
    num = str(num)
    nums1 = []
    nums2 = []
    if "." in num:
        num = num.split(".")
        part1 = num[0][::-1]
        part2 = num[1]

        for i in range(len(part1)):
            nums1.append(int(part1[i])) * (b ** i)

        for i in range(len(part2)):
            nums2.append(int(part2[i])) * (b ** (-(i + 1)))

        return sum(nums1) + sum(nums2)
    else:
        for i in range(len(num)):
            nums1.append(int(num[i])) * (b ** i)
        return sum(nums1)
    
# ----------------------------------------------------------------

print(hw2_try1(1001, 2))

print(hw2_try1(1001, 4))

print(hw2_try1(528.3, 10))

print(hw2_try1(1001, 16))

print(hw2_try1(528.3, 6))