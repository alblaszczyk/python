def scores_to_rating(score1,score2,score3,score4,score5):
    """
    Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
    convert_to_numeric
def convert_to_numeric(score):
    converted_score = float(score)
    return converted_score

    #STEP 2 and STEP 3 find the average of the middle three scores
def sum_of_middle_three(score1,score2,score3,score4,score5):
    """
    Find the sum of the middle three numbers out of the five given.
    """
    max_score = max(score1,score2,score3,score4,score5)
    min_score = min(score1,score2,score3,score4,score5)
    sum = score1 + score2 + score3 + score4 + score5 - max_score - min_score
    return sum
def average_score(sum_middle):
    average_score = (sum_of_the_middle_three / 3)

def score_to_rating_string(average_score):
    if average_score < 1:
         return "Terrible"
    elif average_score < 2:
        return "Bad"
    elif average_score < 3:
        return "OK"
    elif average_score < 4:
        return "Good"
    else:
        return "Excellent"

    return rating
