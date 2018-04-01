#多线程查询数据库
import threading
from .models import datalist

global data
data = {}

def threads_main(select,starttime1,endtime1):
    threads = []
    for i in range(10):
        if i == 0:
            t = threading.Thread(target=my_main,args=(select,starttime1,endtime1))
        else:
            t = threading.Thread(target=my_main,args=(select,starttime1,endtime1))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    return data

def my_main(select,starttime1,endtime1):
    global data
    data = datalist.objects.filter(time__range=(starttime1, endtime1)).filter(category__in=select)

if __name__ == '__main__':
    my_main()