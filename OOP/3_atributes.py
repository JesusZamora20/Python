class Person:
    age = 27
    name = "Jesus"
    country = "Colombia"

engineer = Person()
print(f"Name: {engineer.name}")
print(f"Name: {getattr(engineer, "name")}")
print (f"Does the eng has an age? {hasattr(engineer, "age")}")
print (f"Does the eng has an address? {hasattr(engineer, "address")}")

setattr(engineer, "name", "David")
print(f"Name: {engineer.name}")


delattr(engineer, "country")
print(f"Does the eng has an address? {hasattr(engineer, "country")}")

