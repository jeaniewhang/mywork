# def friends(dictionary):
#     for key, value in sorted(dictionary.items()):
#         print(key, value)

names_ages = {
    'Lucy': 54,
    'Jonny': 20,
    'Eddie': 23,
    'Phillips': 58
}
total_age = 0

for name, age in names_ages.items():
    print(age)
    total_age += age

print(total_age/len(names_ages))

names_ages.sort()
rangeOfAges = ages[len(ages) - 1] - ages[0]

# avg = sum.value(dictionary.items()):
# total = 0
# for a in avg:
#     total += 0
#     print(avg)
#
# print(sum/len(names_ages))
