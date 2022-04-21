def get_grade(final_grade):
    if final_grade > 91:
        return "A"
    elif final_grade > 76:
        return "B"
    elif final_grade > 65:
        return "C"
    elif final_grade > 50:
        return "D"
    else:
        return "F"