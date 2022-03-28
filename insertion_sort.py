from dati import our_list
from dati import words

def insertion_sort(our_list):
    for i in range(1, len(our_list)):

        key_item = our_list[i]
        j = i - 1
        while j >= 0 and our_list[j] > key_item:
            our_list[j + 1] = our_list[j]
            j -= 1
        our_list[j + 1] = key_item

    return our_list

def insertion_sort(words):
    for i in range(1, len(words)):

        key_item = words[i]
        j = i - 1
        while j >= 0 and words[j] > key_item:
            words[j + 1] = words[j]
            j -= 1
        words[j + 1] = key_item

    return words

insertion_sort(our_list)
insertion_sort(words)