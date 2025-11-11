# show menu
print("Which of the following is your main study?")
print("1. Coding")
print("2. Art")
print("3. Architecture")
print("4. Baking")
# input was here before. leaving it off on purpose.
print("-----------------------------------------")

# make a simple class for courses
class MyClass():
    def __init__(self, Name, CourseCode, Section, Objectives):
        # store stuff
        self.Name = Name
        self.CourseCode = CourseCode
        self.Section = Section
        self.Objectives = Objectives
    
    def compareObjectives(self):
        # print each objective
        for Objective in self.Objectives:
            print(Objective)

    def compareWithOtherCourse(self, otherCourse):
        # find common objectives the slow way
        common = []
        for obj in self.Objectives:
            for other_obj in otherCourse.Objectives:
                if obj == other_obj:
                    common.append(obj)

        # show what matches
        print(f"Comparing '{self.Name}' with '{otherCourse.Name}':")
        if common:
            print(f"Common objectives: {common}")
        else:
            print("No common objectives.")
        return common

# coding courses. just data.
courseA = MyClass("Intro to Coding", "INFO 1020", 7, Objectives = [
    "Explain the role of quality assurance testing in software development.",
    "Describe the levels of testing software.",
    "Discuss means of documenting bugs in a software program.",
    "Recognize the verification and validation processes in software testing.",
    "Identify approaches to designing a test case.", "Making unique objectives with code",
    "understanding basics of programming and how it works with data"
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
    "Identify bugs in existing code and update the code to apply fixes and new features.","Making unique objectives with code",
    "Working with Data"
])
courseC = MyClass("Data Structures", "INFO 2020", 2, Objectives = [
    "Implement and analyze basic data structures such as arrays, linked lists, stacks, queues, trees, and graphs.",
    "Understand and apply algorithms for searching and sorting data.",
    "Evaluate the efficiency of different data structures and algorithms.",
    "Design and implement complex data structures to solve specific problems.",
    "Utilize recursion in data structure implementations.", "Making unique objectives with code", "Working with Data",
    "Understanding basics of programming and how it works with data"
])

# art courses. also just data.
courseD = MyClass("Art History", "ART 1010", 1, Objectives = [
    "Understand the historical context of major art movements.",
    "Analyze and interpret various forms of visual art.",
    "Recognize the contributions of key artists throughout history.",
    "Develop critical thinking skills through the study of art.",
    "Explore the relationship between art and culture."
])
courseE = MyClass("Introduction to Art", "ART 1001", 1, Objectives = [
    "Understand basic art concepts and terminology.",
    "Identify different art styles and movements.",
    "Develop foundational skills in various art techniques.",
    "Appreciate the role of art in society and culture."
])
courseF = MyClass("Advanced Art Techniques", "ART 2010", 2, Objectives = [
    "Master advanced techniques in painting, sculpture, and digital art.",
    "Experiment with mixed media and contemporary art forms.",
   "Develop a personal artistic style and portfolio."
])

# ------------------------------------------------------------
# architecture courses. share one goal. still data.
# common: "Apply fundamental design principles."
courseG = MyClass("Intro to Architecture", "ARCH 1010", 1, Objectives = [
    "Apply fundamental design principles.",
    "Identify major architectural styles and periods.",
    "Explain the role of form, function, and context in the built environment."
])

courseH = MyClass("Architectural Drawing & Modeling", "ARCH 1200", 1, Objectives = [
    "Apply fundamental design principles.",
    "Produce basic orthographic and isometric drawings.",
    "Create simple 3D models to communicate design intent."
])

courseI = MyClass("Sustainable Architecture", "ARCH 2100", 2, Objectives = [
    "Apply fundamental design principles.",
    "Evaluate materials and systems for energy efficiency.",
    "Incorporate passive design strategies into conceptual proposals."
])

# ------------------------------------------------------------
# baking courses. also share one goal. still data.
# common: "Practice kitchen safety and sanitation."
courseJ = MyClass("Baking Fundamentals", "BAKE 1001", 1, Objectives = [
    "Practice kitchen safety and sanitation.",
    "Measure and scale ingredients accurately.",
    "Understand the functions of leavening agents and gluten development."
])

courseK = MyClass("Pastry Techniques", "BAKE 2001", 2, Objectives = [
    "Practice kitchen safety and sanitation.",
    "Prepare laminated doughs and custards.",
    "Decorate pastries using piping and glazing fundamentals."
])

courseL = MyClass("Artisan Breads", "BAKE 2100", 2, Objectives = [
    "Practice kitchen safety and sanitation.",
    "Use preferments and fermentation control to develop flavor.",
    "Shape and score loaves for optimal oven spring and crust."
])

# make lists for each focus
coding_courses = [courseA, courseB, courseC]
art_courses = [courseD, courseE, courseF]
architecture_courses = [courseG, courseH, courseI]
baking_courses = [courseJ, courseK, courseL]

# read user pick 1-4
choice = input("Enter the number of your choice: ").strip()

# map pick to (name, list)
focus_map = {
    "1": ("Coding", coding_courses),
    "2": ("Art", art_courses),
    "3": ("Architecture", architecture_courses),
    "4": ("Baking", baking_courses),
}

# get the chosen list
focus_name, selected_list = focus_map.get(choice, (None, None))

if not selected_list:
    # bad pick
    print("No courses available for that selection (or invalid choice).")
else:
    # show the courses
    print(f"\nHere are the {focus_name} courses you can choose from:")
    print("-----------------------------------------")
    for c in selected_list:
        print(f"{c.Name} | {c.CourseCode} | Section {c.Section}")

# left off note. just keeping it.
# user pick and compare later maybe.

# old prints. keeping them off.
print("-----------------------------------------")
print("would you like to compare the objectives of these courses?")
input("Press Enter to continue...")
print("-----------------------------------------") 

# compare all pairs for the chosen focus, hardcoded paths
# yeah it's long, but simple
if choice == "1":
    courseA.compareWithOtherCourse(courseB)
    print("-----------------------------------------")
    courseA.compareWithOtherCourse(courseC)
    print("-----------------------------------------")
    courseB.compareWithOtherCourse(courseC)
    print("-----------------------------------------")
elif choice == "2":
    courseD.compareWithOtherCourse(courseE)
    print("-----------------------------------------")
    courseD.compareWithOtherCourse(courseF)
    print("-----------------------------------------")
    courseE.compareWithOtherCourse(courseF)
    print("-----------------------------------------")
elif choice == "3":
    courseG.compareWithOtherCourse(courseH)
    print("-----------------------------------------")
    courseG.compareWithOtherCourse(courseI)
    print("-----------------------------------------")
    courseH.compareWithOtherCourse(courseI)
    print("-----------------------------------------")
elif choice == "4":
    courseJ.compareWithOtherCourse(courseK)
    print("-----------------------------------------")
    courseJ.compareWithOtherCourse(courseL)
    print("-----------------------------------------")
    courseK.compareWithOtherCourse(courseL)
    print("-----------------------------------------")
else:
    # nothing to compare
    print("No courses to compare in this category.")

# ask about completed courses, simple 1/2
print("-----------------------------------------")
print("have you completed any of these courses?")
print("1. yes")
print("2. no")
completed_choice = input("enter 1 or 2: ").strip()

if completed_choice == "1":
    # get codes from user
    print("which ones")
    # example: INFO 1020, INFO 2341
    completed_codes = input("enter course codes with commas: ").split(",")
    # trim spaces
    completed_codes = [x.strip() for x in completed_codes if x.strip()]
    # show matches only
    print("you completed:")
    for c in selected_list:
        if c.CourseCode in completed_codes:
            print(f"{c.Name} | {c.CourseCode} | Section {c.Section}")
    with open("completed_courses.txt", "w") as f:
        f.write("Completed Courses:\n")
        f.write("-----------------------------------------\n")
        for c in selected_list:
            if c.CourseCode in completed_codes:
                f.write(f"{c.Name} | {c.CourseCode} | Section {c.Section}\n")
                f.write(f"Objectives: {c.Objectives}\n")
                f.write("-----------------------------------------\n")
    print("completed courses saved to 'completed_courses.txt'")
elif completed_choice == "2":
    # nothing done
    print("ok. none.")
else:
    # bad pick
    print("not a valid pick")


# save selected list to a file. simple write.
print("-----------------------------------------")
print("would you like to save these courses to a file?")
input("Press Enter to continue...")

with open("selected_courses.txt", "w") as f:
    # header
    f.write(f"Selected {focus_name} Courses:\n")
    f.write("-----------------------------------------\n")
    # each course
    for c in selected_list:
        f.write(f"{c.Name} | {c.CourseCode} | Section {c.Section}\n")
        f.write(f"Objectives: {c.Objectives}\n")
        f.write("-----------------------------------------\n")

print("courses saved to 'selected_courses.txt'")
