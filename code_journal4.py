# Declare a class with favorite animal
class Monkey:
#Write an initialization function that sets values of data members
	def __init__(self, wingspan, leg_length, num_eyes, has_tail, is_furry):
		self.wingspan = wingspan
		self.leg_length = leg_length
		self.num_eyes = num_eyes
		self.has_tail = has_tail
		self.is_furry = is_furry


# Write a function to describe the characteristics
	def describe(self):
		print(f'Monkey Attributes')
		print(f' Wingspan: {self.wingspan} cm')
		print(f' - Leg Length: {self.leg_length} cm')
		print(f" - Number of Eyes: {self.num_eyes}")
		print(f" - Has a Tail: {'Yes' if self.has_tail else 'No'}")
		print(f" - Is Furry: {'Yes' if self.is_furry else 'No'}")

my_monkey = Monkey(wingspan=248, leg_length=80, num_eyes=2, has_tail =True, is_furry=True)
my_monkey.describe()

