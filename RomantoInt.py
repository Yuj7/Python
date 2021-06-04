def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    values = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    result = 0
    i = 0

    while (i < len(s)): 
        r1 = values[s[i]]
        if (i+1 < len(s)): 
            r2 = values[s[i+1]]
            if (r1 >= r2): 
                result = result + r1 
                i = i + 1
            else: 
                result = result - r1 
                i = i + 1
        else: 
            result = result + r1 
            i = i + 1
    print(result)

romanToInt("MCIV")