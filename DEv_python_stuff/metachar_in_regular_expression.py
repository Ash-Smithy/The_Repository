"""
    ^ matches at the beginning of the line || example --> HI^ ||remarks --> it will match hi at the start of the string 
    $ matches at the end of the line
    . matches any single character except the new line character
    [..] matches any single character in the bracket
    [^..] matches any single character not in the bracket
    re* matches 0 or more occurences of regular expression.  ||Example --> [a-z]*
    re+ matches 1 or more occurences of regular expression 
    re? matches 0 or 1 occurrences of the regular expression
    re{n} matches exactly n number of occurrences of RE ||Example --> 42{1}5
    re{n,} matches n or more occurences of RE || example --> 42{1,}5
    re{n,m} matches atleast n and atmost m occurrences of RE || 42{1,3}5
    a|b matches either a or b
    \w matches word characters
    \W matches non word characters
    \s matches whitespace equivalent to [\t\n\r\f]
    \S natcges non whitespace equivalent to [^t\n\r\f]
    \d{n} matches exactly n digits
    \d{n,} matches n or more digits
    \d{n,m} matches n and atmost m digits
    \D matches non-digits
    \A matches beginning of the string
    \Z matches end of the string
    \G matches point where last match finished
    \b matches word boundaries when outside brackets. Matches backspace when inside brackets
    \B matches non word boundaries
    \n,\t, etc Matches newlines, tabs, etc """