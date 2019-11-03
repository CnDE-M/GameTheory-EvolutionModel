################# Prisoner's Dilemma #################
choice_list = [ ["Y", "N"],["Y", "N"] ];
payoff_list = [[5, 5],[10, 0],[0, 10],[9, 9]];
TOTAL_GENERATION = 10;
# PRISONER_NUM=1000; 

iterate_game(choice_list, payoff_list, TOTAL_GENERATION);


################# Battle of Sex #################

choice_list = [ ["S", "C"],["S", "C"] ];
payoff_list = [[6, 5],[1, 1],[0, 0],[5, 6]];
TOTAL_GENERATION = 20;
# PRISONER_NUM=1000; 

iterate_game(choice_list, payoff_list, TOTAL_GENERATION);

# To caluculate the average least iteration time reaching NE 
import statistics
a=[];
for ii in range(30):
    b=iterate_game(choice_list, payoff_list,TOTAL_GENERATION);
    a.append(b);
statistics.mean(a)

################# Paper, Scissor and Rock #################

choice_list = [ ["A", "B"],["A", "B"] ];
payoff_list = [[2, 0],[0, 1],[0, 1],[2, 0]];
TOTAL_GENERATION = 10;
# PRISONER_NUM=1000; 

iterate_game(choice_list, payoff_list);