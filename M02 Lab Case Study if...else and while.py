"""
Author: Jonas Treadwell
File Name: M02 Lab Case Study if...else and while.py
Description: This app lets you input the last and first names of students along with their GPA. 
If the GPA is equal or above 3.5, the student is in the Dean's List. If the GPA is equal or above 3.25, the student is in the Honor Roll,
otherwise, the student doesn't qualify for any honors.
This is possible due to if, else, elif, and while statements.
"""
# variables: last_name / first_name / gpa

# defining the main program
def main():
    # starting statements 
    print("Dean List / Honor Roll Checker")
    print("Enter 'ZZZ' as the last name to quit. ")
    # start of loop
    while True:   
        last_name = input("Enter student's last name: ") # string input for last name
        if last_name == 'ZZZ':
            break # program ends if the last name is 'ZZZ'
        first_name = input("Enter student's first name: ") # string input for first name
        gpa = float(input("Enter student's GPA: ")) # float integer for gpa
        if gpa >= 3.5: # if statement for Dean's List requirements
            print(f"{first_name} {last_name} has made the Dean's List.")
        elif gpa >= 3.25: # if statment for Honor Roll requirements
            print(f"{first_name} {last_name} has made the Honor Roll.")
        else: # else statement if previous requirements don't match
            print(f"{first_name} {last_name} does not qualify for any honors.")
if __name__ == "__main__":
    main()