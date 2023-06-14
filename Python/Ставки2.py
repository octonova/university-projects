import itertools
import functools
print(*(tuple([[[0]]]) + tuple(*map(lambda data:
filter(lambda x: tuple(x[0]) == x[1], map(lambda
var: (filter(lambda sta: ((var.index(sta[0]) >=
var.index(sta[1])) ^ (var.index(sta[2]) >=
var.index(sta[3]))), data[1]), data[1], var +
data[2]), data[0])), map(lambda x:
(itertools.permutations(set(functools.reduce(lambda
x,y: x + y ,x[1]))), x[1], tuple(set(range(1, x[0] + 1)) -
set(functools.reduce(lambda x,y: x + y ,x[1])))),
map(lambda vvod: (next(vvod), tuple(set(map(lambda y: tuple(y),
map(lambda x: map(int, input().split()), range(next(vvod))))))),
[map(int, input().split())])))))[-1][-1])