import sys, string

def main():
    sequence = int(sys.argv[1])
    #matrix given
    m = [s.strip() for s in sys.stdin]
    print(occurence_finder(m, sequence))

def occurence_finder(m, sequence):
    count_nums = [0, 0, 0, 0, 0]
    
    i = 0
    for s in m:
        j = 0
        for c in s:
            if c == "x":
                count_nums[0] += 1
                #print(count_nums)
    
                if count_nums[0] == sequence:
                    count_nums[4] += 1
                    #print(sequence)
                for x in range(0, sequence):
                    try:
                        if m[i + x][j - x] == m[x + i + 1][j - x - 1] == "x":
                            count_nums[3] += 1
                    
                            if count_nums[3] == sequence - 1:
                                count_nums[4] += 1
                                #print(count_nums)
                        else:
                            count_nums[3] = 0
                            #print(count_nums)
                    
                    except:
                        pass


                    try:
                        if m[i+ x][x + j] == m[x + i + 1][x + j + 1] == "x" or "X":
                            count_nums[2] += 1
                            if count_nums[2] == sequence - 1:
                                count_nums[4] += 1
                        else:
                            count_nums[2] = 0
                    
                    except:
                        pass
                    
                    try:
                        if m[i + x][j] == m[x + i + 1][j] == "x":
                            count_nums[1] += 1
                            #print(x)
                            if count_nums[1] == sequence - 1:
                                count_nums[4] += 1
                                #print(c)
                        else:
                            count_nums[1] = 0
                            #print(count_nums)
                    #use except Exception, repeat each time
                    except:
                        pass

            else:
                count_nums[0] = 0
                #print(count_nums)
            j += 1
        i += 1
    if sequence == 1: #or 1:
        return count_nums[4] * 4
    else:
        return count_nums[4]

if __name__ == '__main__':
    main()