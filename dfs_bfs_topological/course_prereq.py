def courses_to_take(course_to_prereqs):
    # Build a map of maps "course => preqreuisites" for better efficiency.
    course_to_prereqs = {c: set(p) for c, p in course_to_prereqs.items()}
    # print(course_to_prereqs)

    # Used to find courses D which have C as a prerequiste
    prereq_to_course = {}
    for course in course_to_prereqs:
        # print(course)
        for prereq in course_to_prereqs[course]:
            # print(course_to_prereqs[course])
            # print(prereq, "prereq")
            if prereq not in prereq_to_course:
                prereq_to_course[prereq] = []
            prereq_to_course[prereq].append(course)
    # print(prereq_to_course)

    result = []  # courses we need to take in order
    todo = [c for c, p in course_to_prereqs.items() if not p]
    # print(todo, "todo")
    # print([c for c, p in course_to_prereqs.items() if not p])

    while todo:
        prereq = todo.pop()
        result.append(prereq)

        # Find which courses are now free to take
        for c in prereq_to_course.get(prereq, []):
            print(c)
            print(course_to_prereqs[c])
            course_to_prereqs[c].remove(prereq)
            print(course_to_prereqs[c], "removed")

            if not course_to_prereqs[c]:
                print("in", c)
                todo.append(c)
    # Circular dependency
    if len(result) < len(course_to_prereqs):
        return None
    return result


def courses_to_take(course_to_prereqs):
    adv_courses_to_prereq = {k: set(v) for k, v in course_to_prereqs.items()}

    prereq_to_adv_course = {}
    for course in course_to_prereqs:
        for adv_course in adv_courses_to_prereq[course]:
            if adv_course not in prereq_to_adv_course:
                prereq_to_adv_course[adv_course] = []
            prereq_to_adv_course[adv_course].append(course)

    todo = [k for k, v in course_to_prereqs.items() if not v]
    result = []

    print(prereq_to_adv_course)
    while todo:
        ordered_class = todo.pop()
        result.append(ordered_class)
        for adv_class in prereq_to_adv_course.get(ordered_class, []):
            print(prereq_to_adv_course.get(ordered_class, []))

            adv_courses_to_prereq[adv_class].remove(ordered_class)
            if not adv_courses_to_prereq[adv_class]:
                todo.append(adv_class)
    if len(result) < len(todo):
        return None
    return result


courses = {
    'CSC300': ['CSC100', 'CSC200'],
    'CSC200': ['CSC100'],
    'CSC100': []
}
print courses_to_take(courses)
