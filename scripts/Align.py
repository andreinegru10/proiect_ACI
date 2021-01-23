def LCSubStr3(X, Y, Z):
    m = len(X)
    n = len(Y)
    p = len(Z)

    LCSuff = [[[0 for i in range(p + 1)] for j in range(n + 1)] for k in range(m + 1)]
    length = 0
    row, col, dep = 0, 0, 0
 
    for i in range(m + 1):
        for j in range(n + 1):
            for k in range(p + 1):
                if i == 0 or j == 0 or k == 0:
                    LCSuff[i][j][k] = 0
                elif X[i - 1] == Y[j - 1] and X[i - 1] == Z[k - 1]:
                    LCSuff[i][j][k] = LCSuff[i - 1][j - 1][k - 1] + 1
                    if length < LCSuff[i][j][k]:
                        length = LCSuff[i][j][k]
                        row = i
                        col = j
                        dep = k
                else:
                    LCSuff[i][j][k] = 0
 
    if length == 0:
        return 0, ""

    resultStr = ["0"] * length
    while LCSuff[row][col][dep] != 0:
        length -= 1
        resultStr[length] = X[row - 1]
        row -= 1
        col -= 1
        dep -= 1
 
    return len(resultStr), "".join(resultStr)

def LCSubStr(X, Y):
    m = len(X)
    n = len(Y)

    LCSuff = [[0 for i in range(n + 1)] for j in range(m + 1)]
    length = 0
    row, col = 0, 0
 
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                LCSuff[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                LCSuff[i][j] = LCSuff[i - 1][j - 1] + 1
                if length < LCSuff[i][j]:
                    length = LCSuff[i][j]
                    row = i
                    col = j
            else:
                LCSuff[i][j] = 0
 
    if length == 0:
        return 0, ""

    resultStr = ["0"] * length
    while LCSuff[row][col] != 0:
        length -= 1
        resultStr[length] = X[row - 1]
        row -= 1
        col -= 1
 
    return len(resultStr), "".join(resultStr)

def align3(s1, s2, s3, c, ljust=True):
    if ljust:
        f1 = s1.ljust
        f2 = s2.ljust
        f3 = s3.ljust
    else:
        f1 = s1.rjust
        f2 = s2.rjust
        f3 = s3.rjust

    if s1 == "" and s2 != "" and s3 != "":
        sa2, sa3 = align(s2, s3, c, ljust)
        return f1(len(sa2), c), sa2, sa3
    elif s2 == "" and s1 != "" and s3 != "":
        sa1, sa3 = align(s1, s3, c, ljust)
        return sa1, f2(len(sa1), c), sa3
    elif s3 == "" and s1 != "" and s2 != "":
        sa1, sa2 = align(s1, s2, c, ljust)
        return sa1, sa2, f3(len(sa1), c)
    elif s1 == "" and s2 == "" and s3 == "":
        return s1, s2, s3
    
    ssLen, ss = LCSubStr3(s1, s2, s3)
    index1 = s1.find(ss)
    index2 = s2.find(ss)
    index3 = s3.find(ss)

    if ssLen == 0:
        #direct align
        maxLen = max(len(s1), len(s2), len(s3))
        return f1(maxLen, c), f2(maxLen, c), f3(maxLen, c)
    else:
        s1Left = s1[0:index1]
        s2Left = s2[0:index2]
        s3Left = s3[0:index3]
        s1Right = s1[index1+ssLen:]
        s2Right = s2[index2+ssLen:]
        s3Right = s3[index3+ssLen:]

        leftAlign1, leftAlign2, leftAlign3 = align3(s1Left, s2Left, s3Left, c)
        rightAlign1, rightAlign2, rightAlign3 = align3(s1Right, s2Right, s3Right, c)

        return leftAlign1+ss+rightAlign1, leftAlign2+ss+rightAlign2, leftAlign3+ss+rightAlign3

def align(s1, s2, c, ljust = True):
    if ljust:
        f1 = s1.ljust
        f2 = s2.ljust
    else:
        f1 = s1.rjust
        f2 = s2.rjust

    if s1 == "" and s2 != "":
        return f1(len(s2), c), s2
    elif s2 == "" and s1 != "":
        return s1, f2(len(s1), c)
    elif s2 == "" and s1 == "":
        return s1, s2
    
    ssLen, ss = LCSubStr(s1, s2)
    index1 = s1.find(ss)
    index2 = s2.find(ss)

    if ssLen == 0:
        #direct align
        maxLen = max(len(s1), len(s2), )
        return f1(maxLen, c), f2(maxLen, c)
    else:
        s1Left = s1[0:index1]
        s2Left = s2[0:index2]
        s1Right = s1[index1+ssLen:]
        s2Right = s2[index2+ssLen:]

        leftAlign1, leftAlign2 = align(s1Left, s2Left, c)
        rightAlign1, rightAlign2 = align(s1Right, s2Right, c)
        
        return leftAlign1+ss+rightAlign1, leftAlign2+ss+rightAlign2