# find intersection of two sorted arrays (equal length)

A = [13, 27, 35, 40, 49, 55, 59]
B = [17, 35, 39, 40, 55, 58, 60]

## Brute force
constructing all possible pairs, takes O(n)

## Binary search
check the element in the second arrya by binary search O(n * log(n))

## with hash table (search is O(1))
then we get O(n), can we drop the hash table?

## O(n) time and O(1) space solution

In fact, we don't need to do a binary search at all now. We can just do a linear search. As long as the linear
search in B is j ust picking up where the last one left off, we know that we're going to be operating in linear
time.
This algorithm is very similar to merging two sorted arrays. It operates in
O(N) time and O(1) space.
