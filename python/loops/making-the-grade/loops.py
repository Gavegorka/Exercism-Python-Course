"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    Parameters:
        student_scores (list[float]): Student exam scores.

    Returns:
        list[int]: Student scores *rounded* to the nearest integer value.
    """
    round_score = []
    for i in range(len(student_scores)):
        round_score.append(int(round(student_scores[i])))
    return round_score


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    Parameters:
        student_scores (list[int]): Student scores as ints.

    Returns:
        int: The count of student scores at or below 40.
    """
    count_fail = 0
    for i in range(len(student_scores)):
        if student_scores[i] <= 40:
            count_fail += 1
    return count_fail

def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    Parameters:
        student_scores (list[int]): Integer scores.
        threshold (int): The threshold to cross to be the "best" score.

    Returns:
        list[int]: Integer scores that are at or above the "best" threshold.
    """

    ab_treshold = []
    for score in student_scores:
        if score >= threshold:
            ab_treshold.append(score)
    return ab_treshold


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    Parameters:
        highest (int): The value of the highest exam score.

    Returns:
        list[int]: Lower threshold scores for each D-A letter grade interval.

        For example, where the highest score is 100, and failing is <= 40,
        The result would be [41, 56, 71, 86]:
            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    mark_range = (highest - 40) // 4
    letters = []
    treshold = 41
    for _ in range(4):
        letters.append(treshold)
        treshold += mark_range

    return letters

    


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    Parameters:
        student_scores (list): Scores in descending order.
        student_names (list[str]): Student names by exam score in descending order.

    Returns:
        list[str]: Strings in format ["<rank>. <student name>: <score>"].
    """

    answer = []
    rank = 1
    for index, name in enumerate(student_names):
        answer.append(f'{rank}. {name}: {student_scores[index]}')
        rank += 1
    return answer

    
def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    Parameters:
        student_info (list[list[str, int]]): List of [<student name>, <score>] lists.

    Returns:
        list: First `[<student name>, 100]` found OR `[]` if no student score of 100 is found.
    """

    answer = []
    for lst_info in student_info:
        if lst_info[1] == 100:
            answer.extend(lst_info)
            break
    return answer
