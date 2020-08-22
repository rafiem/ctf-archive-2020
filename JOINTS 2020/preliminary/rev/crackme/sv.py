from z3 import *


s = [Int(str(i)) for i in range(25)]

solver=Solver()

solver.add(s[20] - s[0] == 24)
solver.add(s[8] + s[5] == 126)
solver.add(s[14] * s[5] == 3696)
solver.add(s[21] - s[1] == 33)
solver.add(s[10] - s[0] == 2)
solver.add(s[17] - s[0] == 19)
solver.add(s[17] * s[1] == 3848)
solver.add(s[4] + s[6] == 123)
solver.add(s[13] * s[16] == 4488)
solver.add(s[1] * s[6] == 2600)
solver.add(s[13] * s[23] == 3536)
solver.add(s[8] - s[5] == 14)
solver.add(s[15] + s[5] == 123)
solver.add(s[20] - s[17] == 5)
solver.add(s[17] + s[16] == 140)
solver.add(s[16] + s[14] == 132)
solver.add(s[3] * s[6] == 4250)
solver.add(s[18] + s[14] == 145)
solver.add(s[13] + s[13] == 136)
solver.add(s[17] - s[10] == 17)
solver.add(s[11] + s[8] == 145)
solver.add(s[9] + s[1] == 135)
solver.add(s[11] + s[24] == 146)
solver.add(s[3] - s[7] == 11)
solver.add(s[0] - s[2] == 2)
solver.add(s[11] - s[13] == 7)
solver.add(s[3] + s[4] == 158)
solver.add(s[3] - s[16] == 19)
solver.add(s[4] - s[14] == 7)
solver.add(s[12] * s[1] == 4056)
solver.add(s[20] + s[8] == 149)
solver.add(s[9] - s[4] == 10)
solver.add(s[9] - s[6] == 33)
solver.add(s[9] * s[13] == 5644)
solver.add(s[16] + s[5] == 122)
solver.add(s[16] - s[10] == 9)
solver.add(s[17] + s[24] == 145)
solver.add(s[20] - s[13] == 11)
solver.add(s[18] * s[11] == 5925)
solver.add(s[21] * s[23] == 4420)
solver.add(s[22] * s[7] == 5698)
solver.add(s[15] - s[19] == 12)
solver.add(s[16] - s[1] == 14)
solver.add(s[3] - s[13] == 17)
solver.add(s[12] * s[8] == 5460)
solver.add(s[21] * s[13] == 5780)
solver.add(s[7] * s[1] == 3848)
solver.add(s[22] + s[6] == 127)
solver.add(s[13] + s[5] == 124)
solver.add(s[24] + s[1] == 123)

print(solver.check())
res = solver.model()

for i in range(25):
	print(chr(res[s[i]].as_long()),end='')
# w=['']*25
# for i in range(len(w)):
# 	exec("w[{res[i]}]=chr({res[res[i]]})")
# print(''.join(w))