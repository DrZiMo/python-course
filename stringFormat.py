str1 = "Hello"
str1Index = str1.find("llo")  # get the index of the l
print(str1[str1Index])

# substring
word = "learning"
print(word[1:5])  # earn

word2 = "embossed"
print(word2[2:6])  # boss

# replacing function
aboutWeather = "It will be sunny today."
print(aboutWeather.replace("sunny", "rainy"))

email = "Hello, [insert name here]. i'd like to personally thank you for your contribution"
email = email.replace("[insert name here]", "Zuhayb")

print(email)
