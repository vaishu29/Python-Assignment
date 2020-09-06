d={"name":"John","age":29,"salary":25000,"company":"xyz"}
print("The items in dict are: %s" %d.items());
print("The keys in dict are: %s" %d.keys());
print("The values in dict are: %s" %d.values());
print("The length of dict = %s" %len(d));
d.pop("company");
print("Dictionary after a element is poped out %s"%d);