# Iterated Models of 3 classic game in game Theory
---------------------------------------------------------------------------------------------------
This project analyzed 3 types of classic game theory models: 
+ "Prisoners' Dilemma" - 1 pure strategy
+ "Battle of Sex" - 2 pure strategies
+ "Paper, Scissor and Rock" - mix strategy

---------------------------------------------------------------------------------------------------
The project produced a generalized way of analyzing those game based on **evolution theory** idea. 

First, the project hypothesizes,
+ those games are performed in group of individuals, instead of simply 2 player
+ the game would iterate until reaching Nash Equilibrium (NE), instead of playing only one time.

Each game is perfectly defined including:
+ **Players**: 
  individuals' number in the group

  > individuals number in the group that make choice in each iteration.
  > 1000, 10000, 100000, ...

+ **Choices strategy**:
  ex. for each player's choice X, P(X=1)=0.4, P(X=2)=0.6 
  For each player, his/her choice is generated randomly according to this possibility. This could well simulate the mix strategy performance, either in collectives like evolution games, or for induvidual that have P percentage to make X choice.

  The Choice Strategy will keep been recorded through iterations, and eventually plot out. In this way, the project would show an dynamic process approaching to NE.

  > Initially, all choices' possibility are equal;

+ **Payoff**:
  gain or lose after both players make choices
  
+ **Iteration**
  The game will continue iterate, until:
> If the game has a stable NE, the game will reach equal payoffs for all choices;
> If the game keeps fluctuating, we will set a maximum iteration time;

+ **Evolution Strategy**

> After one iteration, players update their choice possibility based on the last iteration's payoff.
> The choice caused higher payoff will decrease P%;
> P% = abs(higher payoff - lower payoff ) / higher payoff;
  
  + If higher payoff equals to lower payoff, P = 0, reach NE;
  + If lower payoff = 0, P = 1, all players would choose choice that lead to low payoff in the next iteration. 
  + However, if the game doesn't have a pure dorminant strategy, the result will keep fluctuate between the extreme value. In case of this situation, we will always make sure 1% players would stay choice caused higher payoff (In reality, this would happen as individuals react unreasonably.)

Finally, the model would output plot showing dynamic process each game approaching to strategy that leads to NE.

---------------------------------------------------------------------------------------------------
The project is a nice tool for fresh in game theory to understand how strategy changing to reach NE directly.

Comparing model result with classic aanalysis result, deficiency, or incompatability of the iteration model to the 3 games are also shown, especially in "Paper, Scissor and Rock" game (See "README_paper_scissor_rock.md").

> + Infinite subjects' number:
> When randomly generating players choice according to choice strategy, the more the players are, the less difference is between actual ratio of choice and designed choice strategy.
> The project set group numbers in 100, 1000, 10000 seperately, which would cause bias.

> + random overwhelming effect:
> As iterations progress continuously, choice strategy are highly relied on the last iteration payoffs. This would easily leads to overwhelming effect for either of the choices randomly, such that sometimes bad choice unintuitionally can win over goo choice.
