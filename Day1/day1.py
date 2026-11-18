print("hello world")

# Escape Sequences
course = "   Python \"for beginners"
print(course)

# Formatted Strings
first = "John"
last = "Smith"
# print(first + " " + last)
# or we can use formatted strings
full = f"{len(first)} {last}"
print(full)

# string methods
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
# strip() method removes any whitespace from the beginning or the end of a string

print(course.find("Python"))
print(course.replace("Python", "Java"))

# returns True if the string is found in the course variable
print("Python" in course)

# returns True if the string is not found in the course variable
print("Python" not in course)
