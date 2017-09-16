from entity.Subject import Subject
from entity.Student import Student
from entity.Group import Group
from entity.Faculty import Faculty
from entity.University import University

def countAverageRating(inWhat):
    if type(inWhat) == Subject:
        summary = 0
        for x in range(len(inWhat.rating)):
            summary = summary + inWhat.rating[x]
        return summary / len(inWhat.rating)

    if type(inWhat) == Student:
        summary = 0
        markNumbers = 0
        for x in range(len(inWhat.subjects)):
            for y in range(len(inWhat.subjects[x].rating)):
                summary = summary + inWhat.subjects[x].rating[y]
                markNumbers = markNumbers + 1
        return summary / markNumbers

    if type(inWhat) == Group:
        summary = 0
        markNumbers = 0
        for x in range(len(inWhat.students)):
            for y in range(len(inWhat.students[x].subjects)):
                for z in range(len(inWhat.students[x].subjects[y].rating)):
                    summary = summary + inWhat.students[x].subjects[y].rating[z]
                    markNumbers = markNumbers + 1
        return summary / markNumbers

    if type(inWhat) == Faculty:
        summary = 0
        markNumbers = 0
        for x in range(len(inWhat.groups)):
            for y in range(len(inWhat.groups[x].students)):
                for z in range(len(inWhat.groups[x].students[y].subjects)):
                    for i in range(len(inWhat.groups[x].students[y].subjects[z].rating)):
                        summary = summary + inWhat.groups[x].students[y].subjects[z].rating[i]
                        markNumbers = markNumbers + 1
        return summary / markNumbers

    if type(inWhat) == University:
        summary = 0
        markNumbers = 0
        for x in range(len(inWhat.faculties)):
            for y in range(len(inWhat.faculties[x].groups)):
                for z in range(len(inWhat.faculties[x].groups[y].students)):
                    for i in range(len(inWhat.faculties[x].groups[y].students[z].subjects)):
                        for k in range(len(inWhat.faculties[x].groups[y].students[z].subjects[i].rating)):
                            summary = summary + inWhat.faculties[x].groups[y].students[z].subjects[i].rating[k]
                            markNumbers = markNumbers + 1
        return summary / markNumbers