import threading


my_threading=threading.Thread(target=test,args=tuple(ls))
my_threading.start()
