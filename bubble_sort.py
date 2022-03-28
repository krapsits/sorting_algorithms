from dati import our_list
from dati import words


def bubble_sort(our_list):
    
    # We go through the list as many times as there are elements
    for i in range(len(our_list)):
        # We want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(len(our_list) - 1):
            if our_list[j] > our_list[j+1]:
                # Swap
                our_list[j], our_list[j+1] = our_list[j+1], our_list[j]
              


def bubble_sort(words):
    # We go through the list as many times as there are elements
    for i in range(len(words)):
        # We want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(len(words) - 1):
            if words[j] > words[j+1]:
                # Swap
                words[j], words[j+1] = words[j+1], words[j]

bubble_sort(our_list)
bubble_sort(words)
