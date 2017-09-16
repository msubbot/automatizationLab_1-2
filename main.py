from entity.Subject import Subject
from entity.Student import Student
from entity.Group import Group
from entity.Faculty import Faculty
from entity.University import University
from handler.countAverageRatingHangler import countAverageRating
from const import SubjectsNames


Subbot_Math = Subject(SubjectsNames.MATH, 5, 3, 4)
Subbot_DIFF = Subject(SubjectsNames.DIFF, 5, 3, 4)
Subbot_FR = Subject(SubjectsNames.FR, 5, 3, 4)

Daniluk_Math = Subject(SubjectsNames.MATH, 5, 7, 6)
Daniluk_PRG = Subject(SubjectsNames.PRG, 6, 8, 4)
Daniluk_FR = Subject(SubjectsNames.FR, 8, 6, 4)

Melnik_Math = Subject(SubjectsNames.MATH, 5, 3, 4)
Melnik_DIFF = Subject(SubjectsNames.DIFF, 7, 5, 4)
Melnik_FR = Subject(SubjectsNames.FR, 2, 8, 4)

Saiko_Math = Subject(SubjectsNames.MATH, 5, 3, 4)
Saiko_PHS = Subject(SubjectsNames.PHS, 2, 9, 4)
Saiko_FR = Subject(SubjectsNames.FR, 4, 10, 4)

Zubowitch_Math = Subject(SubjectsNames.MATH, 8, 10, 6)
Zubowitch_DIFF = Subject(SubjectsNames.DIFF, 4, 10, 10)
Zubowitch_PRG = Subject(SubjectsNames.PRG, 8, 8, 8)

Subbot = Student("Nikita", "Subbot", Subbot_Math, Subbot_DIFF, Subbot_FR)
Daniluk = Student("Sasha", "Daniluk", Daniluk_Math, Daniluk_PRG, Daniluk_FR)
Melnik = Student("Daniil", "Melnik", Melnik_Math, Melnik_DIFF, Melnik_FR)
Saiko = Student("Eugen", "Saiko", Saiko_Math, Saiko_PHS, Saiko_FR)
Zubowitch = Student("Vova", "Zubowitch", Zubowitch_Math, Zubowitch_DIFF, Zubowitch_PRG)

group_17 = Group('17', Subbot, Melnik, Saiko, Zubowitch)
group_18 = Group('18', Daniluk, Zubowitch)
group_19 = Group('19', Melnik, Saiko, Zubowitch)

faculty_MMF = Faculty('MMF', group_17, group_18)
faculty_RAF = Faculty('RAF', group_18, group_19)
faculty_FSM = Faculty('FSM', group_17)

university_BSU = University('BSU', faculty_MMF, faculty_RAF)
university_BSPU = University('BSPU', faculty_FSM)

print("Average rating of subject " + Subbot_Math.name + ": " + str(countAverageRating(Subbot_Math)))
print("Average rating of student " + Subbot.name + ": " + str(countAverageRating(Subbot)))
print("Average rating of group " + group_17.number + ": " + str(countAverageRating(group_17)))
print("Average rating of faculty " + faculty_MMF.name + ": " + str(countAverageRating(faculty_MMF)))
print("Average rating of university " + university_BSU.name + ": " + str(countAverageRating(university_BSU)))