class Course:
    def __init__(self, code, title, units):
        self.code = code
        self.title = title
        self.units = units

    def __str__(self):
        return f"{self.code} - {self.title} ({self.units} units)"

class Programs_Offered:
    def __init__(self):
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def get_total_units(self):
        total_units = 0

        for course in self.courses:
            total_units += course.units

        return total_units

    def __str__(self):
        result = "Programs_Offered:\n"

        for course in self.courses:
            result += str(course) + "\n"

        result += f"Which Programs You Select: 1,2,3"

        return result

c1 = Course("CS101", "Introduction to Computer Science" , 1)
c2 = Course("ENG101", "Composition I" , 2)
c3 = Course( "SE202","Software Engineering" , 3)
Programs_Offered = Programs_Offered()
Programs_Offered.add_course(c1)
Programs_Offered.add_course(c2)
Programs_Offered.add_course(c3)

print(Programs_Offered)
