from datetime import datetime

arq = open(r'D:\scripts\Python\algorithms\criados\boot_time.txt', 'a')
arq.write('\n'+str(datetime.today()))
arq.close()
#mais uma linha
#uma segunda linha
