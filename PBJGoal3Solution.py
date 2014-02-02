def check(bread_for_num_of_sandwiches):
    if bread_for_num_of_sandwiches%2==0:
        print "You have an evan amount of bread! You should be good for making sandwiches"
    elif bread < 2 and peanut_butter < 1 and jelly < 1: 
		print "Looks like I don't have lunch today" 
    else:
        print "You will need to make one open faced sandwich"

print "How many slices of bread do you have"
bread = raw_input()
print "How many scoops of peanut butter do you have?"
peanut_butter = raw_input()
print "How many scoops of jelly do you have?"
jelly = raw_input()

bread = int(bread)
peanut_butter = int(peanut_butter)
jelly = int(jelly)

print "So you have %s slices of bread, %s scoops of peanut butter and %s scoops of jelly" % (
		bread, peanut_butter, jelly)

bread_for_num_of_sandwiches = bread / 2 
check(bread)

