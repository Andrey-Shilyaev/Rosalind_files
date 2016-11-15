from functools import lru_cache

@lru_cache(maxsize=None)
def u_d_search(f, s):
    if len(f) == 0 or len(s) == 0 or s[-1] not in f:
        return 0, ''
    else:
        one_count, subseq1 = u_d_search(f, s[:-1])
        pos = f.rindex(s[-1])
        two_count, subseq2 = u_d_search(f[:pos], s[:-1])
        if one_count > two_count+1:
            return one_count, subseq1
        else:
            return two_count + 1, subseq2+s[-1]


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

x = u_d_search(first, second)
with open('output.txt', 'w') as outf:
    outf.write(x[1])
print(u_d_search.cache_info())
