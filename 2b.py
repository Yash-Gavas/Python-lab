def list_operations():
    subjects = []
    num_of_subjects = int(input("Enter the number of subjects you want to add: "))
    
    for i in range(num_of_subjects):
        subject = input(f"Enter subject {i + 1}: ")
        subjects.append(subject)

    # Display the list using for loop
    for subject in subjects:
        print(subject)
    
    # Display 2nd and 5th elements
    print(f"2nd element: {subjects[1]}")
    print(f"5th element: {subjects[4]}")
    
    # Display first 4 elements
    print(f"First 4 elements: {subjects[:4]}")
    
    # Display last 4 elements
    print(f"Last 4 elements: {subjects[-4:]}")
    
    # Check for a specific subject
    print("Python Programming Lab" in subjects)
    
    # Append and insert
    subjects.append("DCN lab")
    subjects.insert(2, "R")
    
    # Remove and pop
    subjects.remove("Math")
    subjects.pop(3)
    
    print(subjects)

list_operations()
