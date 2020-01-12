def produce_answer(input)
	for character in input.split(""):
		if not "+-*/1234567890 ".contains(character):
			return "bruh...wHy"
	if input == "" or " " in input