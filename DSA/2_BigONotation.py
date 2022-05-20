"""
Measuring Running Time Growth - Time Complexity
################################################################################################################
Big O Notation is used to measure how running time or space requirements for your program grows as input
size grows.
1. O(n)
def foo(arr):
    pass

size(arr) -> 100  -> 0.22 milliseconds
size(arr) -> 1000 -> 2.30 milliseconds

Time represented in the below formula:
    time = a * n + b (a cross n plus b)

Rules:
    1. Keep the fastest growing term
        time = a * n # Here we are running 1 for loop
    2. Drop Constants
        time = O(n) # Order Of n or Big O Notation

Examples:
    def getSquaredNos(numbers):
    SquaredNos = []
    for n in numbers:
        SquaredNos.append(n*n)
    return SquaredNos

    numbers = [2,3,4]
    print(getSquaredNos(numbers))

    For this example the time complexity is Order of N -> Bog O(n)
    -> Here the program time increases bases on the input

################################################################################################################
2. O(1)
def foo(arr):
    pass

size(arr) -> 100  -> 0.22 milliseconds
size(arr) -> 1000 -> 0.23 milliseconds # Here even for the bigger size the time is not growing much

Time represented in the below formula:
    time = a # Here we are not running any for loop.
Rules:
    1. Keep the fastest growing term
    2. Drop Constants
        time = O(1) # Order Of 1 or Big O(1)

Examples:
      def find_first_pe(prices,eps,index):
        pe = prices[index]/eps[index]
        return pe


################################################################################################################
3. O(n)
def foo(arr):
    pass

size(arr) -> 100  -> 0.22 milliseconds
size(arr) -> 1000 -> 0.23 milliseconds # Here even for the bigger size the time is not growing much

Examples:
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] == numbers[j]:
                print(numbers[i] +" is  a duplicate")
                break

    -> IN this example for loop runs 2 times so O(n square)

time = a * n square + b (a cross n plus b)

Rules:
    1. Keep the fastest growing term
        time = a * n square # Here we are running 2 for loops
    2. Drop Constants
        time = O(n square) # Order Of n or Big O Notation

################################################################################################################
Measuring Space Growth - Space Complexity
Binary Search :

list1 = [4,9,15,21,34,57,68,91] -> Search for 68

We can identify the value in 3 iterations using binary search

k = O(log n) -> log2 8 > log2 2to3 ->3 * log 2 to 2 -> 3 iterations




"""

