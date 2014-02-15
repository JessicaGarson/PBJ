# Goal #1: Write a new version of the PB&J program that uses a while loop.  Print "Making sandwich #" and the number of the sandwich until you are out of bread, peanut butter, or jelly.

# Example:

bread = 4
peanut_butter = 3
jelly = 10

bread_for_pbj = bread / 2
pbj_sandwiches = min(bread_for_pbj, peanut_butter, jelly)

sandwich_number = jelly_remianing = 0 
peanut_butter_remaining = 0 

while (sandwich_number < pbj_sandwiches):
	sandwich_number +=1
	print "I'm making sandwich number {0}".format(sandwich_number)

print "All done only had enough for {0} sandwiches".format(pbj_sandwiches)

# Output:
# Making sandwich #1
# Making sandwich #2
# All done; only had enough bread for 2 sandwiches.

# Goal #2: Modify that program to say how many sandwiches-worth of each ingredient remains.

# Example 2:

# Output:
# Making sandwich #1
# I have enough bread for 4 more sandwiches, enough peanut butter for 9 more, and enough jelly for 3 more.
# Making sandwich #2
# I have enough bread for 3 more sandwiches, enough peanut butter for 8 more, and enough jelly for 2 more.
# Making sandwich #3
# I have enough bread for 2 more sandwiches, enough peanut butter for 7 more, and enough jelly for 1 more.
# Making sandwich #4
# All done; I ran out of jelly.