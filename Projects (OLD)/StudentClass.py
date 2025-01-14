class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self.courses = []
        
    def enroll(self, course):
        self.courses.append(course)
        print(f"{self.name} has enrolled in the {course} course.")

    def display_courses(self):
        if not self.courses:
            print(f"{self.name} is not enrolled in any courses.")
        else:
            print(f"{self.name}'s enrolled courses:")
            for course in self.courses:
                print(course)

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

# Example usage:
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

student1.enroll("Math")
student1.enroll("History")
student2.enroll("Computer Science")

student1.display_courses()
student2.display_courses()
