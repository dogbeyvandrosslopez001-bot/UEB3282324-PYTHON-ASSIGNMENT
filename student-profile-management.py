print("===== STUDENT PROFILE SYSTEM =====")
print("Please enter your details below:\n")

raw_name = input("Full Name: ")
raw_age = input("Age: ")
raw_gpa = input("GPA: ")
raw_courses = input("Courses (comma-separated): ")

name = raw_name
age = int(raw_age)
gpa = float(raw_gpa)
courses = [c.strip() for c in raw_courses.split(",")]
num_courses = len(courses)

is_adult = age >= 18
deans_list = gpa >= 3.5

student_profile = {
    "name": name,
    "age": age,
    "gpa": gpa,
    "courses": courses,
    "num_courses": num_courses
}

print("\n--- Type Conversion Demo ---")
print(f"raw_age:  '{raw_age}'  → type: {type(raw_age).__name__}  →  {age}  type: {type(age).__name__}")
print(f"raw_gpa:  '{raw_gpa}'  → type: {type(raw_gpa).__name__}  →  {gpa}  type: {type(gpa).__name__}")
print(f"raw_courses: '{raw_courses}'")
print(f"  → type: {type(raw_courses).__name__}  →  {courses}  type: {type(courses).__name__}")

print("\n===== STUDENT PROFILE =====")
print(f"{'Name:':<13} {student_profile['name']}")
print(f"{'Age:':<13} {student_profile['age']} ({'Adult' if is_adult else 'Minor'})")
print(f"{'GPA:':<13} {student_profile['gpa']:.2f}")
print(f"{'Courses:':<13} {student_profile['courses']}")
print(f"{'# Courses:':<13} {student_profile['num_courses']}")
print(f"{'Deans List:':<13} {'Yes' if deans_list else 'No'}")
print("===========================")

print("\n--- Data Types Used ---")
print(f"str:   {type(name).__name__}  → {name}")
print(f"int:   {type(age).__name__}   → {age}")
print(f"float: {type(gpa).__name__} → {gpa}")
print(f"bool:  {type(is_adult).__name__}  → is_adult = {is_adult}, deans_list = {deans_list}")
print(f"list:  {type(courses).__name__}  → {courses}")
print(f"dict:  {type(student_profile).__name__}   → keys: {list(student_profile.keys())}")