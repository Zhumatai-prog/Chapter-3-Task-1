sentence = input("Enter a text: ")
list_of_sen = list(sentence)
small = 0
big = 0

for i in list_of_sen:
	if i.islower():
		small = small + 1
	elif i.isupper():
		big = big + 1
	else:
		continue

sum = big + small
print(f"Small letters: {int((small * 100) / sum)}%")
print(f"Big letters: {int((big * 100) / sum)}%") 