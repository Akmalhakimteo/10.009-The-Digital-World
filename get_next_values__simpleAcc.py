from fsm import SM

class SimpleAccount(SM):
	def __init__(self, startMoney):
		self.balance = startMoney
		if (self.balance >= 100):
			self.startState = 1 # more than 100
		else:
			self.startState = 0 # less than 100

	def getNextValues(self, state, inp):
 
		new_balance = self.balance + inp

		if new_balance >= 100:
			self.balance = new_balance # this line is problematic
			return 1, self.balance

		else:
			if (inp < 0 and state == 0):
				self.balance = new_balance - 5 # this line too
				return 0, self.balance

			else:
				self.balance = new_balance # a big nono
				return 0, self.balance



sa = SimpleAccount(100)
print(sa.transduce([20, -70, -10, 20, 20]))

my_acc = SimpleAccount(0)

# Lets say, I would like to deposit 20$ everyday
# At the same time, I would need to withdraw 10$ everyday
# After how many days, I will not get withdrawal penalty? 

# I just want to check!, not actually do it. So I just want to
# use the getNextValues as a means for lookup
day_count = 0

my_hypothetical_state, my_hypothetical_bal = my_acc.getNextValues(my_acc.startState, 20) # the first 20 deposit

while(True):
	if (my_hypothetical_bal <  100):
		# will have penalty to withdraw
		day_count += 1
		my_hypothetical_state, my_hypothetical_bal = my_acc.getNextValues(my_hypothetical_state, -10)
		# deposit again
		my_hypothetical_state, my_hypothetical_bal = my_acc.getNextValues(my_hypothetical_state, 20)
	else:
		break

print("number of days until no withdrawal penalty: {0}.".format(day_count))

# The result below should be zero, because i am doing only a hypothetical search and not STEP
# but it prints that my_acc.balance has 100!
# getNextValues, shouldnt change your money
# It should be just a "lookup table"
print("money in my account after get_next_values: {0} ".format(my_acc.balance)) 	


#better design
import copy

class SimplerAccount(SM):
	def __init__(self, startMoney):
		# store startMoney inside state
		if (startMoney >= 100):
			self.startState = [1, startMoney] # more than 100
		else:
			self.startState = [0, startMoney] # less than 100

	# this function is now PURE, i.e: doesn't utilize
	# anything OUTSIDE of the function
	def getNextValues(self, state, inp):
		new_balance = state[1] + inp

		if new_balance >= 100:
			new_state = [1, new_balance]
			return new_state, new_state[1]

		else:
			if (inp < 0 and state[0] == 0):
				new_state = [0, new_balance - 5]
				return new_state, new_state[1]

			else:
				new_state = [0, new_balance]
				return new_state, new_state[1]


# ==== REDO the test ==== #
my_acc = SimplerAccount(0)
my_acc.start()

# Lets say, I would like to deposit 20$ everyday
# At the same time, I would need to withdraw 10$ everyday
# After how many days, I will not get withdrawal penalty? 

# I just want to check!, not actually do it. So I just want to
# use the getNextValues as a means for lookup
day_count = 0

my_hypothetical_state, my_hypothetical_bal = my_acc.getNextValues(my_acc.startState, 20) # the first 20 deposit

while(True):
	if (my_hypothetical_bal <  100):
		# will have penalty to withdraw
		day_count += 1
		my_hypothetical_state, my_hypothetical_bal = my_acc.getNextValues(my_hypothetical_state, -10)
		# deposit again
		my_hypothetical_state, my_hypothetical_bal = my_acc.getNextValues(my_hypothetical_state, 20)
	else:
		break

print("number of days until no withdrawal penalty: {0}.".format(day_count))
print("money in my account after get_next_values: {0} ".format(my_acc.state[1])) 	# money should still be zero now
			
