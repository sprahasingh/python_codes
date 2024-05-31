def get_valid_scores():
    """Prompts the user for scores, validates them, and returns a list of valid scores."""
    list_student_scores = []
    while True:
        scores = input("Enter scores separated by space\n").split()
        for score_str in scores:
            try:
                score = float(score_str)
                list_student_scores.append(score)
            except ValueError:
                print("Invalid score entered. Please enter numbers only.")
                break
        if list_student_scores and len(list_student_scores) == len(scores):
            return list_student_scores
        else:
            list_student_scores = []


student_scores = get_valid_scores()
value = 0
for n in student_scores:
    if n > value:
        value = n
print(f"The highest score in the class is: {value}")
