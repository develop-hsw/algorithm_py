n = input()
length = len(n)
left = 0
right = 0

for i in range(0, int(length/2)):
    left += int(n[i])

for i in range(int(length/2), length):
    right += int(n[i])

if left == right:
    print("LUCKY")
else:
    print("READY")