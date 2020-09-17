pythonist_skills = [
    {"Gohar": "Python Basics"},
    {"Lilit": "OOP"},
    {"Janna": "Git"},
    {"Luiza": "C++"},
    {"Lilit": "Business Analyst"},
    {"Janna": "Numpy"},
    {"Luiza": "Animation"},
    {"Gohar": "Business Consultant"}
]

grand_list = []

for dicts in pythonist_skills:
    keyss = tuple(dicts.keys())
    skills = list(dicts.values())[0]
    skills_list = []
    new_dicts = {keyss[0]: skills_list}
    grand_list.append(new_dicts)
    for dictss in grand_list:
        new_key = tuple(dictss.keys())[0]
        if keyss[0] == new_key:
            dictss[new_key].append(skills)

print(grand_list)