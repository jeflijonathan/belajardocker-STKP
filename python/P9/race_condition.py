import threading
import time

counter = 0 

def tambah(name_thread):
    global counter
    for _ in range(1000):
        print(name_thread, counter)
        temp = counter
        time.sleep(0)
        counter = temp + 1
        # if counter  == 1000:
        #     break
        # else:
        #     counter = temp + 1
        #     continue

t1 = threading.Thread(target=tambah,args=("thread 1",))
t2 = threading.Thread(target=tambah, args=("thread 2",))

t1.start()
t2.start()

t1.join()
t2.join()

print("Harapan:", 2000)
print("Hasil:", counter, "<- salah karena race condition" )