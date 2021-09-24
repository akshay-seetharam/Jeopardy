import matplotlib.pyplot as plt
plt.xkcd()

rt = 0
correct = 0
wrong = 0
#HEY HEY HEY LOOK HERE
#For a daily double, a correct answer is the value of the normal clue, and a wrong answer is not a loss
last_right_or_wrong = []
scores = [0]
cluevalue = input(
    "Enter the clue value/100 or type \"end\" to end the game.\nTo undo the last right or wrong response that affected your score, type \"undo\".\n"
)
clues_responded = 0
while (cluevalue != "end"):
    if cluevalue == "undo":
        scores.pop()
        last = int(last_right_or_wrong.pop())
        rt -= last
        if last < 0:
            wrong -= 1
        else:
            correct -= 1
    elif int(cluevalue) == 0:
        print("Entering 0 as a cluevalue is invalid.")
        break
    

    else:
        status = input(
            "If you got it right, enter \"y\". If not, type \"n\". Otherwise, enter nothing.\nRemember the Daily Double coryat rules (+normal clue value if right, if wrong no effect so type nothing).\n"
        )
        if status == "y":
            rt += int(cluevalue) * 100
            correct += 1
            last_right_or_wrong.append(int(cluevalue) * 100)
            clues_responded += 1
        elif status == "n":
            rt -= int(cluevalue) * 100
            wrong += 1
            last_right_or_wrong.append(-int(cluevalue) * 100)
            clues_responded += 1
    print(rt)
    scores.append(rt)
    plt.plot(scores)
    plt.savefig("score_progression.png")
    print("Correct: " + str(correct))
    print("Wrong: " + str(wrong))
    cluevalue = input(
        "Enter the clue value/100 or type \"end\" to end the game.\nTo undo the last right or wrong response that affected your score, type \"undo\".\n"
    )

print("Score: " + str(rt))
print("Correct: " + str(correct))
print("Wrong: " + str(wrong))
print("No Guess: " + str(60 - (correct + wrong)))

# plt.plot(scores)
# plt.show()
