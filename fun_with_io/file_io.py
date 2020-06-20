import os as os

def write_to_file(name, scores):
    """
    :param name: adds name input to file
    :param scores: adds score input to file
    :return: modified file (i'm not actually sure what I should say for this)
    """
    file_dir = os.path.dirname(__file__)
    file_name = "student_info.txt"
    f = open(os.path.join(file_dir, file_name), "w")
    f.write(get_student_info(name, scores))
    f.close()


def get_student_info(name, scores):
    """
    :param name: asks input for student name and stores as a kwarg
    :param scores: asks input for student scores and stores as a kwarg
    :return: kwargs stored in a variable after calling write to file function
    """
    student_name = input('Enter Student Name: ')
    student_scores = input('Enter as many scores as you want with each score followed by a comma - even if you enter 1 score: ')
    info = (name=student_name, scores=student_scores)
    write_to_file()
    return info


def read_file():
    action = f.read('student_info.txt', 'r')
    print(action)
    f.close()


if __name__ == '__main__':
    get_student_info(name, scores)
    get_student_info(name, scores)
    get_student_info(name, scores)
    get_student_info(name, scores)
    read_file()
    #unsure how to do press any key to exit




