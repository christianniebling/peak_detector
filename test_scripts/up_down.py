from enum import Enum

def count(RR_input, BP_input, RR_thresh, BP_thresh):

    class direction(Enum):
        nil = 1
        up = 2
        down = 3

    up_count = 0
    down_count = 0
    qualifying_count_num = 3
    temp_count = 0
    d1 = direction.nil
    size = len(RR_input)

    if len(RR_input) != len(BP_input):
        print('[count]: lengths are not equal')

    for i in range(1, size):
        if RR_input[i] <= (RR_input[i-1] - RR_thresh) and BP_input[i] >= (BP_input[i-1] + BP_thresh): # up
            if d1 == direction.down:
                if temp_count >= qualifying_count_num:
                    down_count += 1
                temp_count = 0

            temp_count += 1
            d1 = direction.up
        elif RR_input[i] >= (RR_input[i-1] + RR_thresh) and BP_input[i] <= (BP_input[i-1] - BP_thresh): # down
            if d1 == direction.up:
                if temp_count >= qualifying_count_num:
                    up_count += 1
                temp_count = 0

            temp_count += 1
            d1 = direction.down
        else:
            if temp_count >= qualifying_count_num:
                if d1 == direction.up:
                    up_count += 1
                elif d1 == direction.down:
                    down_count += 1
                    
            temp_count = 0
            d1 = direction.nil

        # if i == size-1:
        #     if temp_count >= qualifying_count_num:
        #         if d1 == direction.up:
        #             up_count += 1
        #         elif d1 == direction.down:
        #             down_count += 1

    return up_count, down_count


RR_interval = [901, 890, 885, 880, 891]
RR_interval = [901, 890, 885, 880, 891,901, 890, 885, 880, 891,901, 890, 885, 880, 891,901, 890, 885, 880, 891,901, 890, 885, 880, 891,901, 890, 885, 880, 891,901, 890, 885, 880, 891,901, 890, 885, 880, 891,901, 890, 885, 880, 891,901, 890, 885, 880, 891]

BP_interval = [120, 124, 126, 130, 120]
BP_interval = [120, 124, 126, 130, 120,120, 124, 126, 130, 120,120, 124, 126, 130, 120,120, 124, 126, 130, 120,120, 124, 126, 130, 120,120, 124, 126, 130, 120,120, 124, 126, 130, 120,120, 124, 126, 130, 120,120, 124, 126, 130, 120,120, 124, 126, 130, 120]

l1, l2 = count(RR_interval, BP_interval, 4, 1)

print(l1)
print(l2)