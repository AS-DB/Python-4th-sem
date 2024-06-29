#4>wap to enter two sets and performs all the set operations on it.

set1 = set(input("Enter elements of the first set separated by spaces: ").split())
set2 = set(input("Enter elements of the second set separated by spaces: ").split())

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference (Set 1 - Set 2):", set1.difference(set2))
print("Difference (Set 2 - Set 1):", set2.difference(set1))
print("Symmetric Difference:", set1.symmetric_difference(set2))
