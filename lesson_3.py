#1. **Count Occurrences**: Given a list and an element, find how many times the element appears in the list.
# element = input("Enter element: ")
# arr = input().split()

# print(arr.count(element))

#2. **Sum of Elements**: Given a list of numbers, calculate the total of all the elements.

# arr = [int(i) for i in input().split()]

# print("Sum of list is", sum(arr))

#3. **Max Element**: From a given list, determine the largest element.

# arr = [int(i) for i in input().split()]
# print("Max of the list is", max(arr))

#4. **Min Element**: From a given list, determine the smallest element.
# arr = [int(i) for i in input().split()]
# print("Min of the list is", min(arr))

#5. **Check Element**: Given a list and an element, check if the element is present in the list.

# element = input()
# arr = input().split()

# print("Element is in list:", element in arr)

#6. **First Element**: Access the first element of a list, considering what to return if the list is empty.

# def func(arr):
#     if arr:
#         return arr[0]
#     return
# arr = input().split()
# print(func(arr))


# 7. **Last Element**: Access the last element of a list, considering what to return if the list is empty.

# def func(arr):
#     if arr:
#         return arr[-1]
#     return
# arr = input().split()
# print(func(arr))

# 8. **Slice List**: Create a new list that contains only the first three elements of the original list.

# arr = input().split()
# new_arr = arr[:3]
# print(new_arr)

# 9. **Reverse List**: Create a new list that contains the elements of the original list in reverse order.

# arr = input().split()
# new_arr = arr[::-1]
# print(new_arr)

# 10. **Sort List**: Create a new list that contains the elements of the original list in sorted order.

# arr = [int(i) for i in input().split()]
# arr.sort()
# print(arr)

# 11. **Remove Duplicates**: Given a list, create a new list that contains only unique elements from the original list.

# arr = input().split()
# arr = list(set(arr))
# print(arr)

# 12. **Insert Element**: Given a list and an element, insert the element at a specified index.

# arr = input().split()
# element = input()
# arr.insert(1,element)
# print(arr)

# 13. **Index of Element**: Given a list and an element, find the index of the first occurrence of the element.

# arr = input().split()
# element = input()
# ans = arr.index(element)
# print(ans)

# 14. **Check for Empty List**: Determine if a list is empty and return a boolean.

# def func(arr):
#     return bool(arr)

# arr = input().split()
# print(func(arr))


# 15. **Count Even Numbers**: Given a list of integers, count how many of them are even.

# arr = [4124, 12, 124,325 ,125, 4127, 49, 1241, 214, 2135]
# ans = 0
# for i in arr:
#     if i % 2 == 0:
#         ans += 1
# print(ans) 


# 16. **Count Odd Numbers**: Given a list of integers, count how many of them are odd.

# arr = [4124, 12, 124,325 ,125, 4127, 49, 1241, 214, 2135]
# ans = 0
# for i in arr:
#     if i % 2 == 1:
#         ans += 1
# print(ans) 

# 17. **Concatenate Lists**: Given two lists, create a new list that combines both lists.

# arr = [4124, 12, 124,325 ,125, 4127, 49, 1241, 214, 2135]
# another_arr = [42, 1, 12,4, 214, 12, 421, 421, 4, 24, 45, 436, 6, 643, 634, 34]

# print(arr + another_arr) 

# 18. **Find Sublist**: Given a list and a sublist, check if the sublist exists within the list.

# arr = [4124, 12, 124,325 ,125, 4127, 49, 1241, 214, 2135]
# sub_arr = [125, 4127, 49, 1241]

# def func(arr,sub_arr):
#     for i in range(0,len(arr)):
#         if arr[i] == sub_arr[0]:
#             bl: bool = True
#             for j in range(len(sub_arr)):
#                 if arr[i+j] != sub_arr[j]:
#                     bl = False
#                     break

#             if bl:
#                 return True
#     return False

# print(func(arr, sub_arr))     



# 19. **Replace Element**: Given a list, replace the first occurrence of a specified element with another element.

# arr = [4124, 12, 124,325 ,125, 4127, 49, 1241, 214, 2135]
# element = 12
# another_element = 4444

# arr[arr.index(element)] = another_element

# print(arr)

# 20. **Find Second Largest**: From a given list, find the second largest element.

# arr = [4124, 12, 124,325 ,125, 4127, 49, 1241, 214, 2135]
# arr.sort()

# print(arr[-2])

# 21. **Find Second Smallest**: From a given list, find the second smallest element.

# arr = [4124, 12, 124,325 ,125, 4127, 49, 1241, 214, 2135]
# arr.sort()

# print(arr[1])

# 22. **Filter Even Numbers**: Given a list of integers, create a new list that contains only the even numbers.

# arr = [4124, 12, 124,325 ,125, 4127, 49, 1241, 214, 2135]

# ans = []
# for i in arr:
#     if i % 2 == 0:
#         ans.append(i)

# print(ans)


# 23. **Filter Odd Numbers**: Given a list of integers, create a new list that contains only the odd numbers.

# arr = [4124, 12, 124,325 ,125, 4127, 49, 1241, 214, 2135]

# ans = []
# for i in arr:
#     if i % 2 == 1:
#         ans.append(i)

# print(ans)

# 24. **List Length**: Determine the number of elements in the list.

# arr = input().split()

# print(len(arr))

# 25. **Create a Copy**: Create a new list that is a copy of the original list.

# arr = [4124, 12, 124,325 ,125, 4127, 49, 1241, 214, 2135]
# copy_arr = arr

# print(arr)
# print(copy_arr)

# 26. **Get Middle Element**: Given a list, find the middle element. If the list has an even number of elements, return the two middle elements.

# arr = input().split()
# ll = len(arr)
# if ll % 2 == 0:
#     print(arr[(ll//2) - 1:ll//2+1])

# else:
#     print(arr[ll//2])

# 27. **Find Maximum of Sublist**: Given a list, find the maximum element of a specified sublist.

# arr = input().split()
# start_inx = int(input())
# end_inx = int(input())

# print(max(arr[start_inx:end_inx]),"\n",arr[start_inx:end_inx] )

# 28. **Find Minimum of Sublist**: Given a list, find the minimum element of a specified sublist.

# arr = input().split()
# start_inx = int(input())
# end_inx = int(input())

# print(min(arr[start_inx:end_inx]),"\n",arr[start_inx:end_inx] )

# 29. **Remove Element by Index**: Given a list and an index, remove the element at that index if it exists.

# arr = [4124, 12, 124,325 ,125, 4127, 49, 1241, 214, 2135]
# inx = int(input())
# arr.pop(inx)
# print(arr)

# 30. **Check if List is Sorted**: Determine if the list is sorted in ascending order and return a boolean.

# def func(arr):
#     ans = arr[::]
#     ans.sort()
#     print(ans, arr)
#     for i in range(len(arr)):
#         if ans[i] != arr[i]:

#             return False
    
#     return True

# arr = [int(i) for i in input().split()]

# print("List is sorted:",func(arr))

# 31. **Repeat Elements**: Given a list and a number, create a new list where each element is repeated that number of times.

# arr = input().split()
# number = int(input())

# ans = []

# for i in arr:
#     for j in range(number):
#         ans.append(i)

# print(ans)

# 32. **Merge and Sort**: Given two lists, create a new sorted list that merges both lists.

# arr1 = input().split()
# arr2 = input().split()

# ans = arr1 + arr2
# ans.sort()
# print(ans)

# 33. **Find All Indices**: Given a list and an element, find all the indices of that element in the list.

# arr = input().split()
# element = input()
# ans = []
# for i in range(len(arr)):
#     if arr[i] == element:
#         ans.append(i)

# print(ans)

# 34. **Rotate List**: Given a list, create a new list that is a rotated version of the original list (shift elements to the right).

# arr = input().split()
# k = int(input())

# ans = arr[len(arr)-k:] + arr[:len(arr)-k]

# print(ans)

# 35. **Create Range List**: Create a list of numbers in a specified range (e.g., from 1 to 10).

# x, y = map(int, input().split())

# arr = [int(i) for i in range(x,y+1)]
# print(arr)

# 36. **Sum of Positive Numbers**: Given a list of numbers, calculate the sum of all positive numbers.

# arr = [int(i) for i in input().split()]

# ans = 0
# for i in arr:
#     if  i > 0:
#         ans += i

# print(ans)


# 37. **Sum of Negative Numbers**: Given a list of numbers, calculate the sum of all negative numbers.

# arr = [int(i) for i in input().split()]

# ans = 0
# for i in arr:
#     if  i < 0:
#         ans += i

# print(ans)

# 38. **Check Palindrome**: Given a list, check if the list is a palindrome (reads the same forwards and backwards).

# arr = input().split()

# ans = arr[::-1]

# print("list is a palindrome:", ans == arr)

# 39. **Create Nested List**: Create a new list that contains sublists, where each sublist contains a specified number of elements from the original list.

# arr = input().split()
# number = int(input())

# ans = []
# for i in range(0,len(arr) - number):
#     ans.append(arr[i:i+number])

# print(ans)
    

# 40. **Get Unique Elements in Order**: Given a list, create a new list that contains unique elements while maintaining the original order.

# arr = input().split()

# ans = []
# for i in arr:
#     if i not in ans:
#         ans.append(i)
# print(ans)




# ### Tuple Tasks




# 1. **Count Occurrences**: Given a tuple and an element, find how many times the element appears in the tuple.

# tpl = (321, 312,432, 4324, 432,424 ,423)
# element = 432

# print(tpl.count(element))

# 2. **Max Element**: From a given tuple, determine the largest element.

# tpl = (321, 312,432, 4324, 432,424 ,423)


# print(max(tpl))

# 3. **Min Element**: From a given tuple, determine the smallest element.

# tpl = (321, 312,432, 4324, 432,424 ,423)

# print(min(tpl))

# 4. **Check Element**: Given a tuple and an element, check if the element is present in the tuple.

# tpl = (321, 312,432, 4324, 432,424 ,423)
# element = 432

# print("element is present in the tuple:", element in tpl )

# 5. **First Element**: Access the first element of a tuple, considering what to return if the tuple is empty.

# def func(arr):
#     if arr:
#         return arr[0]
#     return
# arr = (321, 312,432, 4324, 432,424 ,423)
# print(func(arr))


# 6. **Last Element**: Access the last element of a tuple, considering what to return if the tuple is empty.

# def func(arr):
#     if arr:
#         return arr[-1]
#     return
# arr = (321, 312,432, 4324, 432,424 ,423)
# print(func(arr))

# 7. **Tuple Length**: Determine the number of elements in the tuple.

# arr = (321, 312,432, 4324, 432,424 ,423)
# print(len(arr))

# 8. **Slice Tuple**: Create a new tuple that contains only the first three elements of the original tuple.

# arr = (321, 312,432, 4324, 432,424 ,423)
# ans = arr[:3]
# print(ans)

# 9. **Concatenate Tuples**: Given two tuples, create a new tuple that combines both.

# arr1 = (321, 312,432, 4324, 432,424 ,423)
# arr2 = (547,654,754,756,876,342,435)

# ans = arr1 + arr2

# print(ans)

# 10. **Check if Tuple is Empty**: Determine if a tuple has any elements.

# arr = (321, 312,432, 4324, 432,424 ,423)
# print(bool(arr))

# 11. **Get All Indices of Element**: Given a tuple and an element, find all the indices of that element in the tuple.

# arr = (321, 312,432, 4324, 432,424 ,423)
# element = 432
# ans = []
# for i in range(len(arr)):
#     if arr[i] == element:
#         ans.append(i)

# print(ans)

# 12. **Find Second Largest**: From a given tuple, find the second largest element.

# arr = (321, 312,432, 4324, 432,424 ,423)

# ans = list(arr)
# ans.sort()
# print(ans[-2])

# 13. **Find Second Smallest**: From a given tuple, find the second smallest element.

# arr = (321, 312,432, 4324, 432,424 ,423)

# ans = list(arr)
# ans.sort()
# print(ans[1])

# 14. **Create a Single Element Tuple**: Create a tuple that contains a single specified element.

# arr= (1,)
# print(type(arr))

# 15. **Convert List to Tuple**: Given a list, create a tuple containing the same elements.

# arr = [4124, 12, 124,325 ,125, 4127, 49, 1241, 214, 2135]
# ans = tuple(arr)

# print(ans)
# print(type(ans))

# 16. **Check if Tuple is Sorted**: Determine if the tuple is sorted in ascending order and return a boolean.

# arr = (4124, 12, 124,325 ,125, 4127, 49, 1241, 214, 2135) # to check example
# arr = (1, 2 ,3 ,4)
# ans = list(arr[::])
# ans.sort()

# print(ans == list(arr))

# 17. **Find Maximum of Subtuple**: Given a tuple, find the maximum element of a specified subtuple.

# arr = (4124, 12, 124,325 ,125, 4121, 49, 1241, 214, 2135)

# start_with = 3
# end_with = 6

# print(max(arr[start_with:end_with]))



# 18. **Find Minimum of Subtuple**: Given a tuple, find the minimum element of a specified subtuple.

# arr = (4124, 12, 124,325 ,125, 4121, 49, 1241, 214, 2135)

# start_with = 3
# end_with = 6

# print(min(arr[start_with:end_with]))

# 19. **Remove Element by Value**: Given a tuple and an element, create a new tuple that removes the first occurrence of that element.'

# arr = (4124, 12, 124,325 ,125, 4121, 49, 1241, 214, 2135)

# element = 125
# arr = list(arr)
# arr.remove(125)
# print(tuple(arr))


# 20. **Create Nested Tuple**: Create a new tuple that contains subtuples, where each subtuple contains specified elements from the original tuple.

# arr = (4124, 12, 124,325 ,125, 4121, 49, 1241,124, 214, 2135)
# element = 124

# ans = []

# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         if element in arr[i:j]:
#             ans.append(tuple(arr[i:j]))

# print(tuple(ans))


# 21. **Repeat Elements**: Given a tuple and a number, create a new tuple where each element is repeated that number of times.

# arr = (4124, 12, 124,325 ,125, 4121, 49, 1241,124, 214, 2135)
# number = int(input())

# ans = []

# for i in arr:
#     for j in range(number):
#         ans.append(i)

# print(tuple(ans))

# 22. **Create Range Tuple**: Create a tuple of numbers in a specified range (e.g., from 1 to 10).

# x, y = map(int, input().split())

# arr = list(int(i) for i in range(x,y+1))
# print(tuple(arr))

# 23. **Reverse Tuple**: Create a new tuple that contains the elements of the original tuple in reverse order.

# arr = (4124, 12, 124,325 ,125, 4121, 49, 1241,124, 214, 2135)
# new_arr = arr[::-1]
# print(tuple(new_arr))

# 24. **Check Palindrome**: Given a tuple, check if the tuple is a palindrome (reads the same forwards and backwards).


# arr = (4124, 12, 124,325 ,125, 4121, 49, 1241,124, 214, 2135)
# ans = arr[::-1]

# print("list is a palindrome:", ans == arr)

# 25. **Get Unique Elements**: Given a tuple, create a new tuple that contains only the unique elements while maintaining the original order.


# arr = (4124, 12, 124,325 ,125, 4121, 49, 1241,124, 214, 2135)

# ans = []
# for i in arr:
#     if i not in ans:
#         ans.append(i)
# print(tuple(ans))


# ### Set Tasks

# 1. **Union of Sets**: Given two sets, create a new set that contains all unique elements from both sets.

# st1 = {1,2,3,4,5}
# st2 = {4,5,6,7,8}

# print(set(list(st1)+list(st2)))

# 2. **Intersection of Sets**: Given two sets, create a new set that contains elements common to both sets.

# st1 = {1,2,3,4,5}
# st2 = {4,5,6,7,8}

# ans = st1.intersection(st2)

# print(ans)


# 3. **Difference of Sets**: Given two sets, create a new set with elements from the first set that are not in the second.

# st1 = {1,2,3,4,5}
# st2 = {4,5,6,7,8}

# ans = st1.difference(st2)

# print(ans)

# 4. **Check Subset**: Given two sets, check if one set is a subset of the other.

# st1 = {1,2,3,4,5}
# st2 = {4,5,6,7,8}

# ans = st1.issubset(st2)

# print(ans)

# 5. **Check Element**: Given a set and an element, check if the element exists in the set.
# st1 = {1,2,3,4,5}
# element = 3

# print("element exists in the set:", element in st1)

# 6. **Set Length**: Determine the number of unique elements in a set.

# st1 = {1,2,3,4,5}
# print(len(st1))

# 7. **Convert List to Set**: Given a list, create a new set that contains only the unique elements from that list.

# arr = [4124, 12, 124,325 ,125, 4121, 49, 1241,124, 214, 2135]

# ans = set(arr)

# print(ans)

# 8. **Remove Element**: Given a set and an element, remove the element if it exists.

# arr = {4124, 12, 124,325 ,125, 4121, 49, 1241,124, 214, 2135}
# element = 124
# arr.discard(124)

# print(arr)

# 9. **Clear Set**: Create a new empty set from an existing set.

# arr = {4124, 12, 124,325 ,125, 4121, 49, 1241,124, 214, 2135}
# arr.clear()

# print(arr)

# 10. **Check if Set is Empty**: Determine if a set has any elements.'

# arr = {4124, 12, 124,325 ,125, 4121, 49, 1241,124, 214, 2135}


# print("set has elements:", bool(arr))

# 11. **Symmetric Difference**: Given two sets, create a new set that contains elements that are in either set but not in both.




# 12. **Add Element**: Given a set and an element, add the element to the set if it is not already present.



# 13. **Pop Element**: Given a set, remove and return an arbitrary element from the set.



# 14. **Find Maximum**: From a given set of numbers, find the maximum element.




# 15. **Find Minimum**: From a given set of numbers, find the minimum element.



# 16. **Filter Even Numbers**: Given a set of integers, create a new set that contains only the even numbers.



# 17. **Filter Odd Numbers**: Given a set of integers, create a new set that contains only the odd numbers.



# 18. **Create a Set of a Range**: Create a set of numbers in a specified range (e.g., from 1 to 10).
# 19. **Merge and Deduplicate**: Given two lists, create a new set that merges both lists and removes duplicates.
# 20. **Check Disjoint Sets**: Given two sets, check if they have no elements in common.
# 21. **Remove Duplicates from a List**: Given a list, create a set from it to remove duplicates, then convert back to a list.
# 22. **Count Unique Elements**: Given a list, determine the count of unique elements using a set.
# 23. **Generate Random Set**: Create a set with a specified number of random integers within a certain range.


# ### Dictionary Tasks

# 1. **Get Value**: Given a dictionary and a key, retrieve the associated value, considering what to return if the key doesn’t exist.
# 2. **Check Key**: Given a dictionary and a key, check if the key is present in the dictionary.
# 3. **Count Keys**: Determine the number of keys in the dictionary.
# 4. **Get All Keys**: Create a list that contains all the keys in the dictionary.
# 5. **Get All Values**: Create a list that contains all the values in the dictionary.
# 6. **Merge Dictionaries**: Given two dictionaries, create a new dictionary that combines both.
# 7. **Remove Key**: Given a dictionary and a key, remove the key if it exists, handling the case if it doesn’t.
# 8. **Clear Dictionary**: Create a new empty dictionary.
# 9. **Check if Dictionary is Empty**: Determine if a dictionary has any elements.
# 10. **Get Key-Value Pair**: Given a dictionary and a key, retrieve the key-value pair if the key exists.
# 11. **Update Value**: Given a dictionary, update the value for a specified key.
# 12. **Count Value Occurrences**: Given a dictionary, count how many times a specific value appears across the keys.
# 13. **Invert Dictionary**: Given a dictionary, create a new dictionary that swaps keys and values.
# 14. **Find Keys with Value**: Given a dictionary and a value, create a list of all keys that have that value.
# 15. **Create a Dictionary from Lists**: Given two lists (one of keys and one of values), create a dictionary that pairs them.
# 16. **Check for Nested Dictionaries**: Given a dictionary, check if any values are also dictionaries.
# 17. **Get Nested Value**: Given a nested dictionary, retrieve a value from within one of the inner dictionaries.
# 18. **Create Default Dictionary**: Create a dictionary that provides a default value for missing keys.
# 19. **Count Unique Values**: Given a dictionary, determine the number of unique values it contains.
# 20. **Sort Dictionary by Key**: Create a new dictionary sorted by keys.
# 21. **Sort Dictionary by Value**: Create a new dictionary sorted by values.
# 22. **Filter by Value**: Given a dictionary, create a new dictionary that only includes items with values that meet a certain condition.
# 23. **Check for Common Keys**: Given two dictionaries, check if they have any keys in common.
# 24. **Create Dictionary from Tuple**: Given a tuple of key-value pairs, create a dictionary from it.
# 25. **Get the First Key-Value Pair**: Retrieve the first key-value pair from a dictionary.

