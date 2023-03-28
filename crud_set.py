set_Countries = {"col", "ecu", "ar"}
print(set_Countries)
print(type(set_Countries))

size = len(set_Countries)
print(size)

print("col" in set_Countries)

set_Countries.add("per")
print(set_Countries)

set_Countries.update({"ar","bra","per"})
print(set_Countries)

set_Countries.remove("ar")
print(set_Countries)

set_Countries.clear()
print(set_Countries)
size = len(set_Countries)
print(size)