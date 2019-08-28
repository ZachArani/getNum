from random import uniform
from collections import deque
from RandomNumGenerator import RandomGen

""" This is a test stand for testing the random number generator. The name has ground on it because instead of using 
internet, it uses the class directly so we can generate lots of random number. the generated numbers stored in the list 
then get checked for number of similar numbers. It can handle large checks like 1 million"""

randGen = RandomGen()
queue = deque()
print("Enter the amount of checks:")

number_of_checks = int(input())

responses = []
try_count = 0
print("Generating {0} random number...".format(number_of_checks))
while try_count < number_of_checks:
    # time.sleep(0.5)
    _num = randGen.get_num()
    if _num is None:
        pass
    else:
        try_count += 1
        # print("Progress: %{:.0f}".format(try_count / number_of_checks * 100))
        responses.append(_num)
print("Counting the number of recurrences...")
responses.sort()
recurrence_count = 0
number_of_similarity = 0
for i in range(0, len(responses)):
    flag = False

    if i+1 == len(responses):
        break

    if responses[i] == responses[i+1]:
        number_of_similarity += 1

    while responses[i] == responses[i+1]:
        flag = True
        recurrence_count += 1
        # print("Recurrences event: #" + str(recurrence_count))
        i += 1

print("Number of recurrences: {0} , \nNumber of Similarity: {0}".format(recurrence_count,number_of_similarity))
print("Uniqueness: %{:.2f}".format(100-number_of_similarity/number_of_checks*100))
