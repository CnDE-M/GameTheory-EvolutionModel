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

![](psr_1000.png)     

Let's raise group number to 10000

![](psr_10000.png)   
Well, in the early iteration ( n = ), it is stable around, then gradually slide to a pure strategy. The system is not big enough to resist random factor.

Then keep raising!

Group number = 100000
generation =20
stable until n =
![](psr_100000.png)   

Group number = 1000000
generation =20
stable until n =
![](psr_1000000.png)   

Group number = 5000000
generation = 10
stable until n =
![](psr_1000000.png)   

Therefore, to promote the model, the next step is to make model more resistable to random factors.
