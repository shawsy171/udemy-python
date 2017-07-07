# farm_animals = {"pig", "sheep", "goat", "hen"}
# print(farm_animals)


# farm_animals.add("horse")
# for animal in farm_animals:
#     print(animal)

set1 = set(range(0, 20))
set2 = { 1, 2, 3, 6, 9 }

# # combine sets
# unified = set1.union(set2)
# print(unified)
# print(len(unified))
# print(sorted(unified))

# # numbers iin both sets
# print(set1.intersection(set2))
# print(set1 & set2)

# # remove numbers in set2 from set1
# print(set1.difference(set2))
# print(set1 - set2)

# set1.difference_update(set2)
# print("difference_update {}".format(sorted(set1)))

# set2.symmetric_difference(set1)
# print("symmetric_difference {}".format(sorted(set2)))

# set1.remove(13)

# set1.discard(17)

# print("after discard and remove {}".format(sorted(set1)))

try:
    set1.remove(13)
except:
    print("There is no 13 to remove")

if set2.issubset(set1):
    print("set2 is a subset of set")

if set1.issuperset(set2):
    print("set1 is a supersets of set2")

# frozenset is immutable
set3 = frozenset(range(0, 30))
set3.add(31)
