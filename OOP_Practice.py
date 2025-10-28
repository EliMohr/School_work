class MyClass():
    def __init__(self, Name, CourseCode, Section, Objectives):
        self.Name = Name
        self.CourseCode = CourseCode
        self.Section = Section
        self.Objectives = Objectives

courseA = MyClass("Baking 101", "BAK101", 1, "Learn to bake bread")
courseB = MyClass("Painting Basics", "ART201", 2, "Learn color theory") 

print(courseA.Name, courseA.CourseCode, courseA.Section, courseA.Objectives)
