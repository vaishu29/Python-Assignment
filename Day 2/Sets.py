set1={1,2,3,4,5}
set2={10,15,4,5,30}
set1.add(100);
print(set1);
set2.remove(30);
print(set2);
print("the union of set and set2 = %s" %set1.union(set2));
print("the intersection of set and set2 = %s" %set1.intersection(set2));
print("the difference of set and set2 = %s" %set1.difference(set2));
print("the symmetric_differnce of set and set2 = %s" %set1.symmetric_difference(set2));



