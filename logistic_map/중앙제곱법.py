import time
def random_num():
    seed =  6100 #time.time()*10000
    seed_str = str(seed)
    middle_num = int(seed_str[0:4])#10:14])
    for i in range(1, 10):
        seed_square = middle_num**2
        print(seed_square)
        print(middle_num)
        seed_square_str = str(seed_square)
        length = len(seed_square_str)
        start_index = int((length-4)/2)
        print(start_index)
        middle_num = int(seed_square_str[start_index:start_index+4])
    return middle_num
print(random_num())