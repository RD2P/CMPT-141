'''
Assume that grade records are dictionaries that always contain three keys: "Assignments", "Midterm", and "Final". 
An example of such a record might be: {"Assignments":[99,98,100,100,80], "Midterm":95, "Final": 90} 
Note that the "Assignments" key is associated with a list, rather than a single integer; this is because there were 5 assignment grades in the class. All numeric values will be in the range 0 to 100 (i.e. they are percentages). Also assume that dictionary_students is a dictionary in which the keys are student names and the values are grade records. 

Define a function called final_grades() that accepts dictionary_students as its only parameter. The function should add a new key-value pair to each grade record in dictionary_students. The key for this pair should always the be word "Grade", and the value should be the student's final overall grade in the class. The final grade can be calculated according to the following information from the course syllabus: Each assignment is worth 4% The midterm exam is worth 30% The final exam is worth 50% 
Finally, the function should return dictionary_students after all of its records have been modified.
'''

def final_grades(ds):
	assignment_wt = 0.04
	midterm_wt = 0.3
	final_wt = 0.5
	
	for name,record in ds.items():
		grade = 0
		for i in record["Assignments"]:
			grade += i * assignment_wt
		grade += record["Midterm"] * midterm_wt
		grade += record["Final"] * final_wt
		ds[name]["Grade"] = grade
	return ds