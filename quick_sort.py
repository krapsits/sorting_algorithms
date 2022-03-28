
from dati import our_list 
from dati import words


def quick_sort(our_list):

    elements = len(our_list)

    if elements < 2:
        return our_list
    
    current_position = 0 

    for i in range(1, elements): 
         if our_list[i] <= our_list[0]:
              current_position += 1
              temp = our_list[i]
              our_list[i] = our_list[current_position]
              our_list[current_position] = temp

    temp = our_list[0]
    our_list[0] = our_list[current_position] 
    our_list[current_position] = temp 
    
    left = quick_sort(our_list[0:current_position]) 
    right = quick_sort(our_list[current_position+1:elements]) 

    arr = left + [our_list[current_position]] + right 
    
    return arr

def quick_sort(words):

    elements = len(words)

    if elements < 2:
        return words
    
    current_position = 0 

    for i in range(1, elements): 
         if words[i] <= words[0]:
              current_position += 1
              temp = words[i]
              words[i] = words[current_position]
              words[current_position] = temp

    temp = words[0]
    words[0] = words[current_position] 
    words[current_position] = temp 
    
    left = quick_sort(words[0:current_position]) 
    right = quick_sort(words[current_position+1:elements]) 

    arr = left + [words[current_position]] + right 
    
    return arr

quick_sort(words)
quick_sort(our_list)
