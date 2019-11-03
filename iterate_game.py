def iterate_game(choice_list, payoff_list, TOTAL_GENERATION=30, PRISONER_NUM=1000):

    import math
    import numpy as np
    import random
    # import WeightRandomGenerator.py

    ######## choice & payoffs ###########
    #
    choice_pair=[];
    payoff_dict={};
    for ii in range(len(choice_list[0])):
        for jj in range(len(choice_list[1])):
            pair = "".join([choice_list[0][ii],choice_list[1][jj]]);
            choice_pair.append(pair);

    for ii in range(len(choice_pair)):
        payoff_dict[choice_pair[ii]]=payoff_list[ii];


    ######## Players ###########
    #
    ## Record Choice Strategy
    # Record possibility of the FIRST CHOICE
    # CS_record[1] means in the 1st generation, possibility of FIRST CHOICE for [Player 1, PLayer 2]
    CS_record = [[0.5,0.5]];

    for generation in range(TOTAL_GENERATION):

        # randomly generate choices of two prisoner, the choices are ["Yes","Deny"];
        prisoner_1 = WeightRandomGenerator(choice_list[0], CS_record[generation][0], PRISONER_NUM);
        prisoner_2 = WeightRandomGenerator(choice_list[1], CS_record[generation][1], PRISONER_NUM);
        prisoner_list = np.array([prisoner_1,prisoner_2]);

        # Composite the choices of each pair
        game_comp = ["".join([prisoner_1[ii], prisoner_2[ii]]) for ii in range(PRISONER_NUM)];
        # get payoff list of prisoner_1
        payoff_list = [payoff_dict[game_comp[ii]] for ii in range(PRISONER_NUM) ];

        payoff_total=[[0,0],[0,0]];
        for player in range(2):
            for c in range(2):
                choice = choice_list[player][c];
                index =[ii for ii in range(PRISONER_NUM) if prisoner_list[player][ii]==choice];
                payoff_total[player][c] = sum([payoff_list[ii][player] for ii in index]);
        payoff_total = np.array(payoff_total);
            
        # Strategy : 
        # The choice causes higher payoff will lose P percent of subjects, 
        # who switch to choice that causes less payoff in this generation
        # 
        # P percent = (higher payoff - less payoff) / less payoff
        #
        CS_record.append([0,0]);
        for player in range(2):

            if  max(payoff_total[player]) == 0:
                lost_percent =1;
            else:
                lost_percent = abs(payoff_total[player][0] - payoff_total[player][1]) / max(payoff_total[player]);

            max_payoff = max(payoff_total[player]);
            max_index = [ii for ii in range(2) if max_payoff ==payoff_total[player][ii] ];
            max_index = max_index[0]
            if max_index == 0: # first choice caused max payoff
                CS_record[generation+1][player] = CS_record[generation][player] +(1-CS_record[generation][player])*lost_percent;
            else:
                CS_record[generation+1][player] = CS_record[generation][player]*(1-lost_percent);

    ######## Get minimum iteration time #########
    # The the least iteration time when reaching NE
    max_payoff = CS_record[0];
    for ii in range(1,TOTAL_GENERATION):
        if max_payoff == CS_record[ii]:
            max_payoff_index=ii-1;
            break;
        else:
            max_payoff = CS_record[ii];
    if ii == TOTAL_GENERATION-1:
        max_payoff_index=ii;


    ######################## visualize dynamic process ########################
    import matplotlib.pyplot as plt 
    plt.figure(figsize=(16,5));
    plt.title("Dynamic choice distribution(First choice possibility)");
    x=[x+1 for x in range(TOTAL_GENERATION)];
    player_1 = [CS_record[ii][0] for ii in range(TOTAL_GENERATION)];
    player_2 = [CS_record[ii][1] for ii in range(TOTAL_GENERATION)];
    plt.plot(x,player_1,"r.",linestyle="-")
    plt.plot(x,player_2,"b.",linestyle="-")
    plt.legend(["Player_1","Player_2"])
    plt.grid()
    plt.show()

