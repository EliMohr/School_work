class MyClass():
    def __init__(self, Name, CourseCode, Section, Objectives):
        self.Name = Name
        self.CourseCode = CourseCode
        self.Section = Section
        self.Objectives = Objectives

courseA = MyClass("Baking 101", "BAK101", 1, "Learn to bake bread", "Learn to bake cakes", "Learn to bake pastries")
courseB = MyClass("Painting Basics", "ART201", 2, "Learn color theory", "Learn brush techniques", "Create a landscape painting") 

print(courseA.Name)
print(courseA.CourseCode)
print(courseA.Section)
print(courseA.Objectives)
print(courseB.Name)
