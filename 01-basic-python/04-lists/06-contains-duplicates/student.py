def contains_duplicates(xs):
    for i in xs:
        if i in xs:
            return "contains duplicates"

print(contains_duplicates([1,2,3]))
