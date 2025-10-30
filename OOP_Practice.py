class MyClass():
    def __init__(self, Name, CourseCode, Section, Objectives):
        self.Name = Name
        self.CourseCode = CourseCode
        self.Section = Section
        self.Objectives = Objectives
    
    def compareObjectives(self):
        for Objective in self.Objectives:
            print(Objective)

    def compareWithOtherCourse(self, otherCourse):
        common = []
        for obj in self.Objectives:
            for other_obj in otherCourse.Objectives:
                if obj == other_obj:
                    common.append(obj)

        print(f"Comparing '{self.Name}' with '{otherCourse.Name}':")
        if common:
            print(f"Common objectives: {common}")
        else:
            print("No common objectives.")
        return common

courseA = MyClass("Intro to Coding", "INFO 1020", 7, Objectives = [
    "Explain the role of quality assurance testing in software development.",
    "Describe the levels of testing software.",
    "Discuss means of documenting bugs in a software program.",
    "Recognize the verification and validation processes in software testing.",
    "Identify approaches to designing a test case.", "Testing"
])
courseB = MyClass("Fund. of Software Testing", "INFO 2341", 3, Objectives = [
    "Design and evaluate computational solutions for a purpose.",
    "Develop and implement algorithms.",
    "Develop programs that incorporate abstractions.",
    "Evaluate and test algorithms and programs.",
    "Investigate computing innovations.",
    "Implement common and advanced modularization techniques in computer programs.",
    "Apply data handling concepts, including datatype selection.",
    "Describe the Object-Oriented Programming paradigm.",
    "Collaborate with others on a software project.",
    "Identify bugs in existing code and update the code to apply fixes and new features.","Testing"
])

courseA.compareObjectives()
print("-----------------------------------------")
courseB.compareObjectives()
print("-----------------------------------------")
courseA.compareWithOtherCourse(courseB)