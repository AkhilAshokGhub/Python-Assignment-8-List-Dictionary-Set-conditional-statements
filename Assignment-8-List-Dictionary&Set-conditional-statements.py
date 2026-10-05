age_list = [24, 25, 26, 27, 28] 
name_list = ["Akhil", "Aarav", "Advik", "Silpa", "Athira"]

name_list.append ("Yazhini")
age_list.insert(2, 30)
name_list.remove ("Yazhini")
age_list.pop()
age_list.extend([29, 30, 26])
age_list.sort (reverse=True)
print (age_list)
print (name_list)
print (max(age_list))
print (min(age_list))
print (sum(age_list))

print(name_list[0])
print(name_list[4])
print(name_list[2:5])
print(name_list[::-1])


# Dictionary (Creation, Modification and Access):  

student_marks = {
    "Aarav": 85,
    "Bhavya": 92,
    "Chirag": 74,
    "Divya": 88,
    "Eashan": 65
}
print(student_marks["Bhavya"])
student_marks["Janani"] = 80
student_marks["Aarav"] = 82
print(student_marks.keys())
print(student_marks.values())
print(student_marks.items())


my_set ={
    'a','e','i','o','u','a','a','i' }
print(my_set)
# Set is an unordered collection of unique elements. A set does not allow duplicate values
# my_set[4] = 's'
# TypeError: 'set' object does not support item assignment
# Sets are unordered and unindexed, so we cannot access or modify an element. We can add or remove elements by functions or methods 
my_set.add('s')
print(my_set)

set1 = {1, 3, 5, 7, 9}
set2 = {2, 3, 5, 8, 10}

union_set = set1.union(set2)
Intersection_set = set1.intersection(set2)
print(union_set)
print(Intersection_set)


score = float(input("Enter your score (0 to 10): "))
if score < 0 or score > 10:
    print("Invalid score! Please enter a score between 0 and 10.")
elif score > 7:
    print("Above Average: Excellent performance! Keep up the great work.")
elif score >= 4:
    print("Average: Good effort! Keep practicing, there's room for improvement.")
else:
    print("Below Average: Need to improve your performance. Consistent practice will lead to better results.")



