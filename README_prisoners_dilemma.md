# "Prisoners' Dilemma"  
+ *Pure Strategy: 1 dorminant strategy*

## 1. Introduction

In "Prisoners' Dilemma", two suspects are required to propose whether or not the other is guilty, "Y" for yes, "N" for deny. The final penalty for each depends on both suspects' choices.

Payoff here means years number that suspect would spend in prison.
In order to generalize the experiment, year numbers are changed into minus value.
Therefore, the more the year is, the longer time spent in prison, the lower the payoff is, the worse the result is.

Below are years suspect will stay in prison:

| 1 \ 2 | Y | N|
|:----:|:----:|:----:|
| Y | (5, 5) | (0, 10) |
| N | (10, 0) | (1, 1) |
> When A chooses "YES" but B chooses "DENY", A will be released(0 year in prison), while B will spend 10 years in prison;
> When A chooses "YES" and B chooses "YES", A and B will both be in prison for 5 years;
> When A chooses "DENY" and B chooses "DENY", A and B will both be in prison for 1 years;

Year value are converted into minus value, and then all plus 10.
| 1 \ 2 | Y | N|
|:----:|:----:|:----:|
| Y | (5, 5) | (0, 10) |
| N | (10, 0) | (1, 1) |
> ex. in (Y, Y) choice pair, player 1 will stay in prison for 5 years; 
>	 the payoff in this project is set as (-5)+10 = 5

## 2. Iteration Result

To reach NE, the "Prisoners' Dilemma" game has 1 pure dorminant strategy: **("Y","Y")**.
> If one chooses "YES", I will get better result if I choose "YES"
> If one chooses "DENY", I will get better result if I choose "YES"
> Therefore, whatever the other person's choice, "YES" will always be a better choice.

Below present result from model. Notice that each line only refer to the FIRST choice possilibity. In this game, image seperately plot out the possibility of player 1(red)&2(blue) choosing "Y", and it changes through iteration.

![image](https://github.com/CnDE-M/Game_Theory_Model_Iteration_strategy/blob/master/result_images/prisoners_dilemma_1000.png)

<p align="center"> *Group Size = 1000; Iteration Time = 10* </p>

From the result, when reaching NE, choice pair is ("Y", "Y"). This result is consistent to pure strategy analysis.

However, reminded by the "Paper, Scissor and Rock" game, let's gradiently increase group size to see if the pattern will change

![image](https://github.com/CnDE-M/Game_Theory_Model_Iteration_strategy/blob/master/result_images/prisoners_dilemma_10000.png)

<p align="center">*Group Size = 10000; Iteration Time = 10*</p>

![image](https://github.com/CnDE-M/Game_Theory_Model_Iteration_strategy/blob/master/result_images/prisoners_dilemma_100000.png)

<p align="center">*Group Size = 100000; Iteration Time = 10*</p>

![image](https://github.com/CnDE-M/Game_Theory_Model_Iteration_strategy/blob/master/result_images/prisoners_dilemma_500000.png)

<p align="center">*Group Size = 500000; Iteration Time = 10*</p>

With the increase of group size, choice strategies of both players are consistent: both proning to ("Y", "N") = (1,0).
