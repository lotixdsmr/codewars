input_one = 'AAAABBBCCDAABBB'
input_two = [1,2,2,3]

def unique_in_order(iterable):
	uniq = []

	temp = "temp"

	for element in list(iterable):
		if element is not temp:
			temp = element
			uniq.append(element)

	return uniq


def test_unique_in_order():
	assert unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B'], "Should be ['A', 'B', 'C', 'D', 'A', 'B']"
	assert unique_in_order([1,2,2,3]) == [1,2,3], "Should be [1, 2, 3]"

	print("Tests passed!")

test_unique_in_order()