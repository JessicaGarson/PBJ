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

if bread == 0 and peanut_butter >= 1 and jelly >= 1: 
	print "Looks like you are missing bread"

if bread >= 1 and peanut_butter == 0 and jelly >= 1: 
	print "Looks like you are missing peanut butter"

if bread >= 1 and peanut_butter >= 0 and jelly == 0:
	print "Looks like you are missing jelly"