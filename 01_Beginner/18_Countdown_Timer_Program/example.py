import time

my_time = int(input('Enter the time ind seconds: '))
for x in range(my_time, 0 , -1):
    time.sleep(1)
    hours= x // 3600
    minutes = (x % 3600) // 60 
    seconds = x % 60
    print(f"{hours:02}:{minutes:02}:{seconds:02}")