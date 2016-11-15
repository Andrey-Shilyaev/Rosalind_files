
with open('input.txt') as f:
    first = f.readline().strip()
    second = f.readline().strip()

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
                mas[j] = j_pos
                cur_subs[j] = cur_subs[j-1]+cur_symb
        except ValueError:
            pass

# print(first, second, cur_subs[max_length], sep='\n')
max_substr = cur_subs[max_length]
f, s = first, second
prev_f_pos = prev_s_pos = 0
res = ''
for cur_symb in max_substr:
    f_pos = f.index(cur_symb, prev_f_pos)
    s_pos = s.index(cur_symb, prev_s_pos)
    res = res + f[prev_f_pos:f_pos] + s[prev_s_pos:s_pos] + cur_symb
    prev_f_pos = f_pos + 1
    prev_s_pos = s_pos + 1
res = res + f[prev_f_pos:] + s[prev_s_pos:]
# print(res)
with open('output.txt', 'w') as outf:
    outf.write(res)
