## "Paper, Scissor and Rock"
+ mix strategy


------------------------
1. Introduction

The "Paper, Scissor and Rock" game is a classic game that doesn't have a pure strategy. To reach NE, we will choose to use mix strategy, that we make choice according to a percentage, and this also indicates that the strategy will work only if we perform the game iterally.

Payoff here means scores player get. The higher payoff is, the better the result is.

To simplify the game, I reduce the game to 2 choice ("A", "B").

Below are payoff table:

| 1 \ 2 | A | B |
|:----:|:----:|:----:|
| A | (2, 0)| (0, 1) |
| B | (0, 1) | (2, 0) |



------------------------
2. Iteration Result

The results model produced are not as expected. For this game, players are expected to perform mix strategies, that is 
+ player 1: (A, B) = (0.5, 0.5) 
+ player 2: (A, B) = (0.5, 0.5)  

Initially group number is set in 1000. The model isn't stable at the best mix strategy above. It will instead prone to one strategy randomly.

![image](https://github.com/CnDE-M/Game_Theory_Model_Iteration_strategy/blob/master/result_images/psr_1000.png)     

Let's raise group number to 10000

<p align="center">Group number = 10000; Iteration Time =20, Stable when n = **3**</p>

![image](https://github.com/CnDE-M/Game_Theory_Model_Iteration_strategy/blob/master/result_images/psr_10000.png)   

Now it is getting a bit of interesting. In the early iteration ( n = ), it is stable around (0.5, 0.5), but then gradually slide to a pure strategy. Perhaps it is because the system's size is not big enough to resist random factor.

Then keep raising!

<p align="center">Group number = 100000; Iteration Time =20, Stable when n = **5**</p>

![image](https://github.com/CnDE-M/Game_Theory_Model_Iteration_strategy/blob/master/result_images/psr_100000.png)  

<p align="center">Group number = 1000000, Iteration Time = 20, Stable when n = **6**</p>

![image](https://github.com/CnDE-M/Game_Theory_Model_Iteration_strategy/blob/master/result_images/psr_1000000.png)  

<p align="center">Group number = 2000000, Iteration Time = 10; Stable when n = **6**</p>

![image](https://github.com/CnDE-M/Game_Theory_Model_Iteration_strategy/blob/master/result_images/psr_2000000.png)  

......

With the increase of group size, the iteration time when system keeps stable gets a bit of bigger. 
