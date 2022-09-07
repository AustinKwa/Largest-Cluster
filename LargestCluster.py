#  File: LargestCluster.py

#  Description: Determine the largest cluster found in each journey through space.

#  Student Name: Austin Kwa

#  Student UT EID: ak38754

#  Course Name: CS 313E

#  Unique Number: 51125

import sys

# Input: s is a string representing your journey through the galaxy
# Output: return an integer representing the largest cluster encountered
def largest_cluster(s):
    clusters = []
    count = 1
    for i in range(len(s) - 1):
        if (s[i] == s[i + 1]) and (i + 1 == len(s) - 1):
            clusters.append(count + 1)
            count = 1

        elif (s[i] != s[i + 1]):
            clusters.append(count)
            count = 1
            
        elif s[i] == s[i + 1]:
            count += 1
    
    max = clusters[0]
    max_i = 0
    for i in range(len(clusters)):
        if clusters[i] > max:
            max = clusters[i]
            max_i = i
    
    return clusters[max_i]

# IMPORTANT: You should not have to modify anything below this line
def main():
    # read in the number of test cases
    test_cases = int(sys.stdin.readline().strip())

    for i in range(test_cases):
        test_case = sys.stdin.readline().strip()
        max_cluster = largest_cluster(test_case)
        print("The largest cluster of journey", i, "is", max_cluster)

if __name__ == "__main__":
    main()