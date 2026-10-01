from survey import AnonymousSurvey

question = "What language did you first learn? "

my_survey= AnonymousSurvey(question)
my_survey.show_question()

""" Take ainput from the user and store responses """

print("Enter 'q' at any time to quit.")

while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

""" Show the survey results. """
print("\nThank you to everyone who participated in the survey!")
my_survey.show_responses()
