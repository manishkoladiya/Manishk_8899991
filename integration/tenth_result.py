import pytest
def calculate_total(subject_marks):
    return sum(subject_marks)

def calculate_average(subject_marks):
    return sum(subject_marks) / len(subject_marks)

def calculate_percentage(total_marks, total_possible_marks):
    return (total_marks / total_possible_marks) * 100

def main():
    subjects = ["Hindi", "English", "Maths", "Science", "Social Science"]
    subject_marks = []

    for subject in subjects:
        marks = float(input(f"Enter marks for {subject}: "))
        subject_marks.append(marks)

    total_marks = calculate_total(subject_marks)
    total_possible_marks = len(subjects) * 100
    average_marks = calculate_average(subject_marks)
    percentage = calculate_percentage(total_marks, total_possible_marks)

    print("\nSubject-wise Marks:")
    for i in range(len(subjects)):
        print(f"{subjects[i]}: {subject_marks[i]}")

    print("\nTotal Marks:", total_marks, "/", total_possible_marks)
    print("Average Marks:", average_marks)
    print("Percentage:", percentage, "%")

if __name__ == "__main__":

    main()