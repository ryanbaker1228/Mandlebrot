import random



def _bigint_addition_test() -> str:
	test: str = "//  ADDITION\n {{{\n"
	num_tests: int = 100

	for i in range(num_tests): 
		left:  int = random.randrange(-2**4096, 2**4096)
		right: int = random.randrange(-2**4096, 2**4096)
		plus:  int = left + right

		test += "mu_assert((BigInt(\"" + str(left) + "\") + BigInt(\"" + str(right) + "\")) == BigInt(\"" + str(plus) + "\"));\n"

	return test + "}}}\n\n"


def _bigint_subtraction_test() -> str:
	test: str  = "// SUBTRACTION\n{{{\n"
	num_tests: int = 100

	for i in range(num_tests): 
		left:  int = random.randrange(-2**4096, 2**4096)
		right: int = random.randrange(-2**4096, 2**4096)
		diff:  int = left - right

		test += "mu_assert((BigInt(\"" + str(left) + "\") - BigInt(\"" + str(right) + "\")) == BigInt(\"" + str(diff) + "\"));\n"

	return test + "}}}\n\n"


def _bigint_multiplication_test() -> str:
	test: str = "// MULTIPLICATION\n{{{\n"
	num_tests: int = 25

	for i in range(num_tests):
		left:  int = random.randrange(-2**4096, 2**4096)
		right: int = random.randrange(-2**4096, 2**4096)
		prod:  int = left * right

		test += "mu_assert((BigInt(\"" + str(left) + "\") * BigInt(\"" + str(right) + "\")) == BigInt(\"" + str(prod) + "\"));\n"

	return test + "}}}\n\n"


def write_bigint_tests() -> None:
	write_location  = "test_bignums.cpp"
	safe_copy 		= "copy_of_test_bignums.cpp"
	start_delimiter = "#test_BigInt::_large_operations::begin_writing"
	end_delimiter   = "#test_BigInt::_large_operations::stop_truncating"

	with open(write_location, 'r+') as file:
		lines = file.readlines()

		with open(safe_copy, 'w') as copy:
			copy.truncate()
			copy.writelines(lines)
			copy.close()

		start_idx, end_idx = -1, -1

		for i, line in enumerate(lines):
			if start_delimiter in line:
				start_idx = i
			elif end_delimiter in line:
				end_idx = i
				break

		assert(end_idx > start_idx and start_idx > -1)

		file.seek(0)
		file.truncate()

		file.writelines(lines[:start_idx + 1])

		file.write('\n')
		file.write(_bigint_addition_test())
		file.write(_bigint_subtraction_test())
		file.write(_bigint_multiplication_test())

		file.writelines(lines[end_idx:])


write_bigint_tests()
