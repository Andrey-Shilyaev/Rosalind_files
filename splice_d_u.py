
with open('input.txt') as f:
    f.readline()
    DNAs = []
    txt = ''
    for line in f.readlines():
        if line.startswith('>'):
            DNAs.append(txt)
            txt = ''
        else:
            txt += line.strip()
    DNAs.append(txt)
    first, second = DNAs

if len(first) < len(second):
    first, second = second, first
inf = len(first)+1
mas = [-1, ]+[inf]*(len(second))
cur_subs = {x: '' for x in range(len(second)+1)}
max_length = 0
for i in range(len(second)):
    cur_symb = second[i]
    for j in range(max_length+1, 0, -1):
        try:
            j_pos = first.index(cur_symb, mas[j-1]+1)
            if mas[j] > j_pos:
                if mas[j] == inf:
                    max_length = j
                mas[j] =  j_pos
                cur_subs[j]=cur_subs[j-1]+cur_symb
        except ValueError:
            pass

with open('output.txt', 'w') as outf:
    outf.write(cur_subs[max_length])
