'''
DSAPY is a module which will help you in any competition and your dsa journey
Please share this with your friend too.
Creater - Rudransh
'''

import math as mt

print("Hello! from team dsapy (Rudransh) \n \n")


# def SieveOfEratosthenes(num):
#     prime = [True for i in range(num+1)]
#     p = 2
#     while (p * p <= num):
#         if (prime[p] == True):
#             for i in range(p * p, num+1, p):
#                 prime[i] = False
#         p += 1
#     for p in range(2, num+1):
#         if prime[p]:
#             return prime

# def check_user_input(input):
#     try:
#         val = int(input)
#         Exception("It's a int")
#         return val
#     except ValueError:
#         try:
#             val = float(input)
#             Exception("Input is a float")
#         except ValueError:
#             Exception("It's a string")
class string:
    @staticmethod
    def replaceallwith(string, old, key):
        return string.replace(old, key)

    @staticmethod
    def evalcal(str):
        return eval(str)



class array:

    class matrix:
        @staticmethod
        def transpose(X):
            result = X
            for i in range(len(X)):
                for j in range(len(X[0])):
                    result[j][i] = X[i][j]
            return result


    def __init__(self):
        self.fallatujf = 1
        self.matrix = self.matrix()

    @staticmethod
    def reversearray(arr):
        return arr[::-1]

    @staticmethod
    def addtoall(arr, num):
        for i in range(len(arr)):
            arr[i] += num
        return arr

    @staticmethod
    def frequency(arr, k):
        ct = 0
        for i in arr:
            if (k == arr[i]):
                ct += 1
        return ct

    @staticmethod
    def removeduplicates(arr):
        res = []
        [res.append(x) for x in arr if x not in res]
        return res

    # @staticmethod
    # def toString(List):
    #     return ''.join(List)

    @staticmethod
    def powerset(s):
        x = len(s)
        arr = []
        for i in range(1 << x):
            arr.append([s[j] for j in range(x) if (i & (1 << j))])
        return arr

    @staticmethod  # susssssy line
    def maxSum(arr, k):
        n = len(arr)
        if n < k:
            print("Invalid")
            return -1
        window_sum = sum(arr[:k])
        max_sum = window_sum
        for i in range(n - k):
            window_sum = window_sum - arr[i] + arr[i + k]
            max_sum = max(window_sum, max_sum)

        return max_sum

    @staticmethod
    def Kadane(a):
        size = len(a)
        max_so_far = -100000000000000000000000000000000000000000000000000000000000000000000000000000000000 - 1
        max_ending_here = 0
        for i in range(0, size):
            max_ending_here = max_ending_here + a[i]
            if (max_so_far < max_ending_here):
                max_so_far = max_ending_here
            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far


class number:
    class bit:
        @staticmethod
        def isSet(n, k):
            if n & (1 << (k - 1)):
                return True
            else:
                return False

        @staticmethod
        def setbit(num, k):
            return (1 << k) or num

        @staticmethod
        def countsetbit(num):
            count = 0
            while (num):
                count += num & 1
                num >>= 1
            return count

        @staticmethod
        def flip(num1, num2):
            return number.bit.countsetbit(num1 ^ num2)

    @staticmethod
    def power(x, y):

        if y == 0:
            return 1
        if y % 2 == 0:
            return number.power(x, y // 2) * number.power(x, y // 2)

        return x * number.power(x, y // 2) * number.power(x, y // 2)

    @staticmethod
    def order(x):
        n = 0
        while (x != 0):
            n = n + 1
            x = x // 10
        return n

    @staticmethod
    def nthFibonacci(num):
        if num <= 2:
            return num - 1
        else:
            return number.nthFibonacci(num - 1) + number.nthFibonacci(num - 2)

    @staticmethod
    def factorial(num):
        fact = 1
        if (num < 1):
            fact = None
        elif (num == 1 or num == 0):
            fact = 1
        else:
            for i in range(1, num+1):
                fact = fact * i
        return fact

    @staticmethod
    def gcd(x, y):
        while (y):
            x, y = y, x % y
        return x

    @staticmethod
    def lcm(x, y):
        if x > y:
            greater = x
        else:
            greater = y
        while (True):
            if ((greater % x == 0) and (greater % y == 0)):
                lcm = greater
                break
            greater += 1
        return lcm

    @staticmethod
    def nCr(n, r):
        return (number.factorial(n))/((number.factorial(r))*number.factorial(n-r))

    @staticmethod
    def nPr(n, r):
        return (number.factorial(n))/(number.factorial(n-r))

    @staticmethod
    def isArmstrong(x):
        n = number.order(x)
        temp = x
        sum1 = 0
        while (temp != 0):
            r = temp % 10
            sum1 = sum1 + number.power(r, n)
            temp = temp // 10
        return (sum1 == x)

    @staticmethod
    def isprime(n):
        prime_flag = 0
        if (n > 1):
            for i in range(2, int(mt.sqrt(n)) + 1):
                if (n % i == 0):
                    prime_flag = 1
                    break
            if (prime_flag == 0):
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def eulertotient(n):
        result = 1
        for i in range(2, n):
            if (number.gcd(i, n) == 1):
                result += 1
        return result

    @staticmethod
    def primearray(upper):
        result = []
        for cp in range(2, upper + 1):
            for i in range(2, cp):
                if (cp % i == 0):
                    break
            else:
                result.append(cp)
        return result

    @staticmethod
    def sumtilln(num):
        return num*(num+1)/2


class dsa:
    @staticmethod
    def checkSort(arr):
        flag = 0
        if (arr == sorted(arr)):
            flag = 1
        if (flag):
            return True
        else:
            return False

    @staticmethod
    def binarysearch(arr, low, high, key):
        if dsa.checkSort(arr):
            if high >= low:
                mid = (high + low) // 2
                if arr[mid] == key:
                    return mid
                elif arr[mid] > key:
                    return dsa.binarysearch(arr, low, mid - 1, key)
                else:
                    return dsa.binarysearch(arr, mid + 1, high, key)
            else:
                return -1
        else:
            return -1

    @staticmethod
    def bubbleSort(arr):
        n = len(arr)
        swapped = False
        for i in range(n-1):
            for j in range(0, n-i-1):
                if arr[j] > arr[j + 1]:
                    swapped = True
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            if not swapped:
                return

    @staticmethod
    def rotateArray(arr, n, d):
        temp = []
        i = 0
        while (i < d):
            temp.append(arr[i])
            i = i + 1
        i = 0
        while (d < n):
            arr[i] = arr[d]
            i = i + 1
            d = d + 1
        arr[:] = arr[: i] + temp
        return arr

    # NOTE - This function does not return a sorted array , to get a sorted array use dsa.insertionSort() function to do so.
    @staticmethod
    def insertion(arr, k, element):
        newarr = arr.insert(k, element)
        return newarr

    @staticmethod
    def insertionSort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    @staticmethod
    # NOTE-this function have arguments array (arr) and index(key) , there is a inbuilt function too which has arguments array and element , please dont confuse between them
    def deletion(arr, key):
        ele = arr[key]
        arr.remove(ele)
        return arr

    @staticmethod
    def mergeSort(arr1, arr2):
        n1, n2 = len(arr1), len(arr2)
        arr3 = [None] * (n1 + n2)
        i = 0
        j = 0
        k = 0
        while i < n1 and j < n2:
            if arr1[i] < arr2[j]:
                arr3[k] = arr1[i]
                k = k + 1
                i = i + 1
            else:
                arr3[k] = arr2[j]
                k = k + 1
                j = j + 1
        while i < n1:
            arr3[k] = arr1[i]
            k = k + 1
            i = i + 1
        while j < n2:
            arr3[k] = arr2[j]
            k = k + 1
            j = j + 1
        return arr3


class problem:
    @staticmethod
    def josephus(n, k):
        k -= 1
        arr = [0]*n
        for i in range(n):
            arr[i] = 1
        cnt = 0
        cut = 0
        num = 1
        while (cnt < (n - 1)):
            while (num <= k):
                cut += 1
                cut = cut % n
                if (arr[cut] == 1):
                    num += 1
            num = 1
            arr[cut] = 0
            cnt += 1
            cut += 1
            cut = cut % n
            while (arr[cut] == 0):
                cut += 1
                cut = cut % n
        return cut + 1

    @staticmethod
    def DutchNationalFlag(a, arr_size):
        lo = 0
        hi = arr_size - 1
        mid = 0
        # Iterate till all the elements
        # are sorted
        while mid <= hi:
            # If the element is 0
            if a[mid] == 0:
                a[lo], a[mid] = a[mid], a[lo]
                lo = lo + 1
                mid = mid + 1
            # If the element is 1
            elif a[mid] == 1:
                mid = mid + 1
            # If the element is 2
            else:
                a[mid], a[hi] = a[hi], a[mid]
                hi = hi - 1
        return a

    @staticmethod
    def trappedRainWater(arr, n):
        res = 0
        # For every element of the array
        for i in range(1, n - 1):
            # Find the maximum element on its left
            left = arr[i]
            for j in range(i):
                left = max(left, arr[j])
            # Find the maximum element on its right
            right = arr[i]
            for j in range(i + 1, n):
                right = max(right, arr[j])
            # Update the maximum water
            res = res + (min(left, right) - arr[i])
        return res

    @staticmethod
    def ChocolateDistrubution(arr, n, m):
        # if there are no chocolates or number
        # of students is 0
        if (m == 0 or n == 0):
            return 0
        # Sort the given packets
        arr.sort()
        # Number of students cannot be more than
        # number of packets
        if (n < m):
            return -1
        # Largest number of chocolates
        min_diff = arr[n-1] - arr[0]
        # Find the subarray of size m such that
        # difference between last (maximum in case
        # of sorted) and first (minimum in case of
        # sorted) elements of subarray is minimum.
        for i in range(len(arr) - m + 1):
            min_diff = min(min_diff,  arr[i + m - 1] - arr[i])
        return min_diff


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push_front(self, item):
        self.items.append(item)

    def push_back(self, item):
        self.items.insert(0,item)

    def pop_front(self):
        return self.items.pop()

    def pop_back(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

class stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + ""
            cur = cur.next
        return out[:-3]

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value