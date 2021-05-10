import time
  
s_time = time.time()
while True:
    if time.time() - s_time > 5:
                    count =+ 1
                    s_time = time.time()
                    print(count)