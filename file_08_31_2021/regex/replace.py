import re
s=['11',
   'a = 1;',
   'b = input();',

   'if a + b > 0 && a - b < 0:',
   'start()',
   'elif a*b > 10 || a/b < 1:',
   'stop()',
   'print set(list(a)) | set(list(b))',
   '#Note do not change &&& or ||| or & or |',
   '#Only change those "&&" which have space on both sides.',
   '#Only change those "||" which have space on both sides.']

w =['x| ||&|& | & | &&  &&x',
'x& & |&||  || &&& & &x',
'x| &&||&& |  & |  |||x',
'x|&&& |&||  &|& |&|| x',
'x&& |   | ||&| |&|| &x',
'x|& &||& && &&&  &&| x',
'x|& &| | |&|& &  &| |x',
'x &&& |& & &||&|&&||&x',
'x  & &&| && ||  ||  |x',
'x&&& &&&  &|  || | ||x',
'x|&|& &&  |&   &|||&|x',
'x    &&&|&&| ||&&& &&x',
'x  & || |&&&&&|&&&&| x',
'x|&|&&&|&| || | &||& x',
'x&& |&|   |& &&&| && x',
'x &    &&&&& &|& &| |x',
'x|& & |   & |&  | |&|x',
'x&|&|&||||| &|&& || |x',
'x&|&  &&  |&|  &&&||&x',
'x || & | &&  &|&| |&|x']

for i in range(len(w)):

    line =w[i]

    if ' && ' in line:
        line =line.replace(' && ',' and ')
        print(line)
    if' || ' in line:
        line =line.replace(' || ',' or ')
        print(line)
    else:
        print(line)