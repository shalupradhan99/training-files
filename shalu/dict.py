thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Finding length of a Dictionary
print(len(thisdict))

# check if a element exists in a Dictionary
if "model" in thisdict:
    print("Yes, 'model' is one of the keys")

# Adding an element to a Dictionary
thisdict["color"] = "red"
print(thisdict)

# Removing an element with specified key
thisdict.pop("model")
print(thisdict)
