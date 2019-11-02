## import random
def WeightRandomGenerator(item_list,dt_list,rand_num):
    ## description:
    # generate random number in distribution probability;
    # ex. generate X∈{"a"，"b"}, P(X="a")=0.6; P(X="b")=0.4; 

    ## Input arg:
    # (1) item_list: item to be generated;
    # (2) dt_list: distribution of each item; integer distribution
    #     ex. item=[1,2] -- dt=[6,4] <=> P(X=1)=0.6; P(X=2)=0.4; \
    # (3) rand_num: number of items to generate

    ## Output arg:
    # randomly generate one item according to probability distribution
    start = 0;
    cp_list=[];
    for ii in range(0,len(dt_list)):
        cp_list[start:start+dt_list[ii]] = item_list[ii]*dt_list[ii];
        start = start+dt_list[ii]+1;
        
    random_numbers=[random.randint(1,sum(dt_list))-1 for _ in range(rand_num)];
    return [cp_list[ii] for ii in random_numbers];

