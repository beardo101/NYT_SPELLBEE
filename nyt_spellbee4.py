primary_char = []
optional_chars = []
cleaned_words = []
over3_words = []
primary_words = []
solutions = []



def get_letters():
	global primary_char
	primary_char = input("Type the yellow letter: ")
	primary_char = primary_char.lower()
	for i in range(6):
		get_op_chars()


def get_op_chars():
	op_char = input("Type the next letter: ")
	op_char = op_char.lower()
	optional_chars.append(op_char)


def remove_car_return(orig_wordlist, new_wordlist):
	for word in orig_wordlist:
		new_wordlist.append(word[:-1])

def over3(orig_wordlist, new_wordlist):
	for word in orig_wordlist:
		if len(word) > 3:
			over3_words.append(word)

def check_primary(orig_wordlist, new_wordlist):
	for word in orig_wordlist:
		for i in word:
			if i in set(primary_char):
				new_wordlist.append(word)

def check_optional_char(orig_wordlist,new_wordlist):
	optional_chars.append(primary_char[0])
	for word in set(orig_wordlist):
		split = set(word)
		word_bools = []
		for letter in split:
			#print(letter)
			if letter in optional_chars:
				word_bools.append(True)
				#print(f"True:{word}")
			else:
				word_bools.append(False)
				#print(f"False:{word}")
		# print(word_bools)
		# print(f"all(word_bools) = {all(word_bools)}")
		if all(word_bools) == True:
			solutions.append(word)

with open ('english3.txt') as d:
	english_words = d.readlines()
print(f"Beginning length of english_words: {len(english_words)}")


get_letters()

print("\n\n")
print(f"Yellow Letter: {primary_char}")
print(f"Other Letters: {optional_chars}")

remove_car_return(english_words, cleaned_words)
over3(cleaned_words,over3_words)
check_primary(over3_words,primary_words)
check_optional_char(primary_words, solutions)

print(f"{len(solutions)} solutions: \n{solutions}")

with open('solutions.txt', 'w') as s:
    for line in solutions:
        s.write(line)
        s.write('\n')