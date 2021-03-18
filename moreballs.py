letters = ['B', 'A', 'L', 'L', 'S']
ball = ''

for letter in letters:
    ball += letter
print(ball)
ball = ''
for letter in letters[::-1]:
    ball += letter
print(ball)