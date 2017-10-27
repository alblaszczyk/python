# Test Checker
results= []
answers     = [2,3,5,7,7]
my_answers  = [2,3,5,7,7]

def check_answers(my_answers,answers):
    counter     = 0
    correct     = 0
    incorrect   = 0

    for i in range(len(answers)):
        if answers[counter] == my_answers[counter]:
            results.append("True")
            correct +=1
        else:
            results.append("False")
            incorrect +=1
        counter += 1

    if 1 == 1:
        print "yes"
    print correct

    if correct /5 >= 0.7:
        return "Congratulations, you passed the test! You scored "  +str(correct) + " out of 5."
    elif incorrect/5 >= 0.3:
        return "Unfortunately, you did not pass. You scored "       +str(correct) + " out of 5."

        def check_answer(my_answer, answer):
    if my_answer == answer:
        return True
    else:
        return False

def check_answers(my_answers,answers):
    #Checks the five answers provided to a multiple choice quiz and returns the results.
    results = []
    for i in range(len(my_answers)):
        results.append(check_answer(my_answers[i], answers[i]))
    count_correct = 0

    for result in results:
        if result:
            count_correct += 1

    if count_correct/len(results) > 0.7:
        return "Congratulations, you passed the test!"
    elif (len(results) - count_correct)/len(results) >= 0.3:
        return "Unfortunately, you did not pass."

        def check_answers(my_answers,key):
            """
            Checks the five answers provided to a multiple choice quiz and returns the results.
            """
            correct_no = 0
            incorrect_no = 0
            counter = 0
            for i in range(len(my_answers)):
                if my_answers[counter] == key[counter]:
                    correct_no += 1
                else:
                    incorrect_no += 1
                counter += 1
            if correct_no/5 > 0.7:
                return "Congratulations, you passed the test! You scored " + str(correct_no) + " out of 5."
            else:
                return "Unfortunately, you did not pass. You scored " + str(correct_no) + " out of 5."
        print(check_answers([1,2,3,4,5],[1,2,3,4,5]))
