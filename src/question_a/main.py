#add import
from question_a import calculate_stats

numlist = []
for i in range(5):
    numlist.append(int(input("Please enter any number: ")))

lowest, highest, total, average = calculate_stats(numlist)

print(f'The lowest number is {lowest}')
print(f'The highest number is {highest}')
print(f'The sum of all the numbers is {total}')
print(f'The average of the numbers is {average}')