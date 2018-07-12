# To print multiplication table a given number
print("\nTo print multiplication table of a given number.")
multiplication_Table = input("Which multiplication table you want to print? ")
count = 10
for counter in range(1, count + 1):
	product = int(multiplication_Table) * counter
	print(multiplication_Table + " x " + "{:>2}".format(str(counter)) + " = " + "{:>3}".format(str(product)))