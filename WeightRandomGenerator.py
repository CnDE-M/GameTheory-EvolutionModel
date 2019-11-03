import random
import math
def WeightRandomGenerator(choice_list, p, rand_num):
    ## description:
    # generate random number in distribution probability;
    # ex. generate X∈{"a"，"b"}, P(X="a")=0.6; P(X="b")=0.4; 

    ## Input arg:
    # (1) choice_list: 2 choices of player
    # (2) p: possibility of first choice
    # (3) rand_num: number of items to generate

    ## Output arg:
    # randomly generate one item according to probability distribution
    start = 0;
    cp_list=[];
    dt_list = [math.ceil((p*rand_num)), rand_num-math.ceil((p*rand_num))];
    for ii in range(0,len(choice_list)):
        cp_list[start:start+dt_list[ii]] = choice_list[ii] * dt_list[ii];
        start = start+dt_list[ii]+1;
        
    random_numbers=[random.randint(1,sum(dt_list))-1 for _ in range(rand_num)];
    return [cp_list[ii] for ii in random_numbers];