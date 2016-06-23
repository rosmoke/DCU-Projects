def count_char(s, c):
	if len(s) == 0:
		return 0
	if s[0] == c:
		return 1 + count_char(s[1:], c)
	return count_char(s[1:], c)


def count(i, j):
   if i < j:
      i += 1
      return(1 + count(i, j))
   return 0

print(count(1,5))
#print(2 + count_char("daniell", "i"))