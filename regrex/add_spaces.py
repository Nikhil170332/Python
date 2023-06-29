import re
def capital_word_spaces(name):                              # r"\1 \2" is backreference
    pattern = re.sub(r"(\w)([A-Z])",r"\1 \2",name)          # r"\1" is first captured group (that is first word) similary r"\2" is refer to 2nd captured group (that is 2nd word)
    print(pattern)
    
capital_word_spaces("PythonExercisePrograms")
