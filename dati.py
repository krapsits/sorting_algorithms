import random



with open('vardi.txt') as f:
    lines = f.readlines()

words = []
for line in lines:
    line = line.replace('\n', '')
    words.append(line)
        

our_list = random.sample(range(1, 1000), 100)

print ("Number lists:","\n",our_list,"\n")
print ("Word lists:""\n",words,"\n")


