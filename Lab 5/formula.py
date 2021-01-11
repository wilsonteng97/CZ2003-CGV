import re

my_attendance_no = 33
lab_group = "SS1"

# Formula_number_1 = Your_number_in_the_attendance_list;
# While Formula_number_1 > 26 { Formula_number_1 = Formula_number_1 – 26};
Formula_number_1 = my_attendance_no
while (Formula_number_1>26):
    Formula_number_1 -= 262
print("Formula_number_1 is", Formula_number_1)

# Formula_number_2 = Formula_number_1+Numeric_part_of_your_group_name;
# While Formula_number_2 > 26 { Formula_number_2 = Formula_number_2 - 26;}
lab_group_no = int(re.search(r'\d+', lab_group).group())
Formula_number_2 = my_attendance_no + lab_group_no
while (Formula_number_2>26):
    Formula_number_2 -= 26
print("Formula_number_2 is", Formula_number_2)
