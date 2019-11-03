import math
import random
import WeightRandomGenerator.py

## payoff setting
payoff_YN_Y=0; # in (Y,N) payoff of Y
payoff_YN_N=10;# in (Y,N) payoff of N
payoff_NN=3; # in (N,N) payoff of both N
payoff_YY=20;# in (Y,Y) payoff of both Y

payoff_dict = {"YY":payoff_YY, "NN": payoff_NN, "YN": payoff_YN_Y, "NY":payoff_YN_N};

PRISONER_NUM=1000; # subject number per generation

# At the start, both Y and N are equally distributed
INITIAL_Y=int(0.5*PRISONER_NUM); 
INITIAL_N=int(0.5*PRISONER_NUM);

# generatiom: game iteration time
TOTAL_GENERATION=20;

## main
Y_num=INITIAL_Y  # Y number at the start of each generation
N_num=INITIAL_N  # N number at the start of each generation

## Record dynamic number change of Y&N
RECORD_Y=[Y_num] # record Y number for each generation 
RECORD_N=[N_num] # record N number for each generation 

for generation in range(TOTAL_GENERATION):

    # randomly generate choices of two prisoner, the choices are ["Yes","Deny"];
    prisoner_1 = WeightRandomGenerator(["Y", "N"], [Y_num, N_num], PRISONER_NUM);
    prisoner_2 = WeightRandomGenerator(["Y", "N"], [Y_num, N_num], PRISONER_NUM);
    
    # Composite the choices of each pair
    game_comp = ["".join([prisoner_1[ii], prisoner_2[ii]]) for ii in range(PRISONER_NUM)];
    
    # get payoff list of prisoner_1
    payoff_list = [payoff_dict[game_comp[ii]] for ii in range(PRISONER_NUM) ];
    index_Y = [idx for idx,ii in enumerate(prisoner_1) if ii=="Y"];
    index_N = [idx for idx,ii in enumerate(prisoner_1) if ii=="N"];
    payoff_Y = sum([payoff_list[ii] for ii in index_Y]);    
    payoff_N = sum([payoff_list[ii] for ii in index_N]);  
    
    
    # Strategy : 
    # The choice causes higher payoff will lose P percent of subjects, 
    # who switch to choice that causes less payoff in this generation
    # 
    # P percent = (higher payoff - less payoff) / less payoff
    #
    lost_percent = abs(payoff_Y - payoff_N) / max([payoff_Y, payoff_N]);
    
    if payoff_Y > payoff_N: # if Y causes longer years in prison
        Y_num = math.ceil(Y_num*(1-lost_percent));
        N_num = PRISONER_NUM - Y_num;
    elif payoff_Y < payoff_N:# if N causes longer years in prison
        N_num = math.ceil(N_num*(1-lost_percent));
        Y_num = PRISONER_NUM - N_num;
    elif payoff_Y == payoff_N:# if payoff are the same, reach Nash Equilibrium
        break;
        
    RECORD_Y.append(Y_num); # record Y number for each generation 
    RECORD_N.append(N_num);
        
        
    
######################## visualize dynamic process ########################
import matplotlib.pyplot as plt 
plt.figure(figsize=(16,5))
plt.title("Dynamic choice distribution in Prisoners's dilemma")
x=[x+1 for x in range(len(RECORD_N))]
plt.plot(x,RECORD_Y,"r.",linestyle="-")
plt.plot(x,RECORD_N,"b.",linestyle="-")
plt.legend(["YES","NO"])
plt.grid()
plt.show()