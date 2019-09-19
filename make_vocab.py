filename="alice_in_wonderland.txt"
with open(filename) as alice:
	context=alice.read()
words=context.split()
for word in words:
