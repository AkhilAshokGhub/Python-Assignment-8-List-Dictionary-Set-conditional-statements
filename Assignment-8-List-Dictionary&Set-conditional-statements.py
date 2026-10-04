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
student_marks["Janani"] = 80
student_marks["Aarav"] = 82
print(student_marks.keys())
print(student_marks.values())
print(student_marks.items())





