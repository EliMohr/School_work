class MyClass():
    def __init__(self, Name, CourseCode, Section, Objectives):
        self.Name = Name
        self.CourseCode = CourseCode
        self.Section = Section
        self.Objectives = Objectives

courseA = MyClass("Intro to Coding", "INFO 1020", 7, Objectives = [
    "Explain the role of quality assurance testing in software development.",
    "Describe the levels of testing software.",
    "Discuss means of documenting bugs in a software program.",
    "Recognize the verification and validation processes in software testing.",
    "Identify approaches to designing a test case."
])
courseB = MyClass("Painting Basics", "ART201", 2, Objectives = [
    "Understand color theory and its application in painting.",
    "Explore different painting techniques and mediums.",
    "Develop skills in composition and design."
])

print(courseA.Name, courseA.CourseCode, courseA.Section, courseA.Objectives[3])
print(courseB.Name, courseB.CourseCode, courseB.Section, courseB.Objectives[1])
