from dati import our_list
from dati import words

def selection_sort(our_list):
   for i in range(len(our_list)-1):

        min_index = i

        for j in range(i+1, len(our_list)-1):
            if our_list[j] < our_list[min_index]:
                min_index = j
  
        our_list[i], our_list[min_index] = our_list[min_index], our_list[i]

def selection_sort(words):
   for i in range(len(words)-1):

        min_index = i

        for j in range(i+1, len(words)-1):
            if words[j] < words[min_index]:
                min_index = j
  
        words[i], words[min_index] = words[min_index], words[i]
    

selection_sort(our_list)
selection_sort(words)