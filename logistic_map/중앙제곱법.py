import time
def random_num():
    seed = time.time()*10000
    seed_str = str(seed)
    seed_digits = int(seed_str[10:14])
    for i in range(1,5):
        seed_square = seed_digits**2
        seed_square_str = str(seed_square)
        length = len(seed_square_str)
        start_index = int((length-4)/2)
        middle_num = seed_square_str[start_index:start_index+4]
    print(middle_num)
for j in range(1, 20):
    random_num()
