
from dati import our_list
from dati import words

def shell_sort(our_list):

    n = len(our_list)
    gap = n//2
  

    while gap > 0:
  
        for i in range(gap,n):
  
            
            temp = our_list[i]

            j = i
            while  j >= gap and our_list[j-gap] >temp:
                our_list[j] = our_list[j-gap]
                j = j  -  gap
  
            our_list[j] = temp
        gap = gap //  2

def shell_sort(words):

    n = len(words)
    gap = n//2
  

    while gap > 0:
  
        for i in range(gap,n):
  
            
            temp = words[i]

            j = i
            while  j >= gap and words[j-gap] >temp:
                words[j] = words[j-gap]
                j = j - gap
  
            words[j] = temp
        gap = gap // 2

shell_sort(our_list)
shell_sort(words)