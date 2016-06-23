s = raw_input()
is_palindrome = True
start = 0
end = len(s)


while is_palindrome == True:
	if s[start] == s[end - 1:len(s)]:
		start = start + 1
		end = end - 1
		print s
	else:
		is_palindrome = False