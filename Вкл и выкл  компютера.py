import os
a = int(input('Введите "0", чтобы завершить сеанс работы с компьюетром, или "1", чтобы перейти в спящий режим\n'))
if a < 1:
   os.system('shutdown -s')
else :
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

