
from dati import our_list 
from dati import words

def merge_sort(our_list):
    if len(our_list) > 1:
        mid = len(our_list) // 2
        leftList = our_list[:mid]
        rightList = our_list[mid:]

        merge_sort(leftList)
        merge_sort(rightList)

        m = 0
        n = 0

        z = 0

        while m < len(leftList) and n < len(rightList):
            if leftList[m] <= rightList[n]:

              our_list[z] = leftList[m]

              m += 1
            else:
                our_list[z] = rightList[n]
                n += 1
            z += 1

   
        while m < len(leftList):
            our_list[z] = leftList[m]
            m += 1
            z += 1

        while n < len(rightList):
            our_list[z]=rightList[n]
            n += 1
            z += 1

def merge_sort(words):
    if len(words) > 1:
        mid = len(words) // 2
        leftList = words[:mid]
        rightList = words[mid:]

        merge_sort(leftList)
        merge_sort(rightList)

        m = 0
        n = 0

        z = 0

        while m < len(leftList) and n < len(rightList):
            if leftList[m] <= rightList[n]:

              words[z] = leftList[m]

              m += 1
            else:
                words[z] = rightList[n]
                n += 1
            z += 1

   
        while m < len(leftList):
            words[z] = leftList[m]
            m += 1
            z += 1

        while n < len(rightList):
            words[z]=rightList[n]
            n += 1
            z += 1

        
merge_sort(our_list)
merge_sort(words)

