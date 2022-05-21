answer = 50                             #provide answer
guess = 49 #provide guess

if guess<50:
    result = "Oops!  Your guess was too low."
elif guess>50:
    result = "Oops!  Your guess was too high."
elif guess==50:
    result = "Nice!  Your guess matched the answer!"

print(result)

