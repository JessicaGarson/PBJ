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

num_sandwiches = min(bread_for_num_of_sandwiches, peanut_butter, jelly)

num_pbsandwiches = min(bread_for_num_of_sandwiches, peanut_butter)

if bread >= num_sandwiches and peanut_butter >= num_sandwiches and jelly == 0: 
	print "Looks like you are missing jelly, you can still make peanut butter sandwiches"

elif bread > num_sandwiches and peanut_butter > num_sandwiches:
	print "You can make %s peanut butter only sandwiches and %s peanut butter jelly sandwiches" % (
 		num_pbsandwiches, num_sandwiches)
