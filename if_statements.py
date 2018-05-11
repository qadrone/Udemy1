# should_continue == True
# if should_continue: #same as "if should_continue == True:"
#     print("bugger")

known_people = ["jon", "jim", "jay"]
person = input("Enter person you know: ")
if person in known_people:
    print("{}'s an asshole.".format(person))
#if person not in known_people: (use "else" instead of duplicating stuff)
else:
    print("{} is also an asshole.".format(person))