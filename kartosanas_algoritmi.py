
from bubble_sort import our_list
from bubble_sort import words

from bubble_sort import bubble_sort

from insertion_sort import insertion_sort

from quick_sort import quick_sort

from selection_sort import selection_sort

from merge_sort import merge_sort

from shell_sort import shell_sort

import time


start_time = time.time()
bubble_sort(our_list)
bubble_sort(words)

print("Bubble sort Number list:",our_list,"\n")
print("Bubble sort Word list:",words,"\n")
print("Bubble sort time: %s seconds" % (time.time() - start_time),'\n')

start_time = time.time()
insertion_sort(our_list)
insertion_sort(words)

print("Insertion sort Number list:",our_list,"\n")
print("Insertion sort Word list:",words,"\n")
print("Insertionn sort time: %s seconds" % (time.time() - start_time),'\n')

start_time = time.time()
selection_sort(our_list)
selection_sort(words)

print("Selection sort Number list:",our_list,"\n")
print("Selection sort Word list:",words,"\n")
print("Selection sort time: %s seconds" % (time.time() - start_time),'\n')

start_time = time.time()
merge_sort(our_list)
merge_sort(words)

print("Merge sort Number list:",our_list,"\n")
print("Merge sort Word list:",words,"\n")
print("Merge sort time: %s seconds" % (time.time() - start_time),'\n')

start_time = time.time()
quick_sort(our_list)
quick_sort(words)

print("Quick sort Number list:",our_list,"\n")
print("Quick sort Word list:",words,"\n")
print("Quick sort time: %s seconds" % (time.time() - start_time),'\n')

start_time = time.time()
shell_sort(our_list)
shell_sort(words)

print("Shell sort Number list:",our_list,"\n")
print("Shell sort Word list:",words,"\n")
print("Shell sort time: %s seconds" % (time.time() - start_time),'\n')








