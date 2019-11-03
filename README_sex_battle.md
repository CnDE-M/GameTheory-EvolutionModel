## "Battle of Sex" 
+ Pure Strategy: 2 dorminant strategies

1. Introduction


In "Battle of Sex", one couple is heading to a place for dating, but for some reason they didn't determine the specific place. 
They have two choices, either the ideal place for Man or for Woman. 
Let's say choices are: "sport game" for Man("S" for short); "cinema" for Woman("C" for short).

Payoff here means the gain(maybe emotionally or so) after they get to the suspected place. They would be happy if they successfully meet the lover,
and even happier if the place is where he/she prefers. The higher the payoff is, the better the result is.

Below are payoff table:

| M \ W | S | C |
|:----:|:----:|:----:|
| S | (6, 5)| (1, 1) |
| C | (0, 0) | (5, 6) |

> If Man/Woman doesn't meet each other, they will get nothing; If they meet and get to have a date, both will gain +5;
> If Man/Woman get to the place they prefer, whether or not they meet, he/she will gain +1;
> Gain in both situation could be accumulated;

To reach NE, players have 2 pure dorminant strategies: **("C","C") & ("S","S")**.

2. Iteration Result

The model will randomly produce 3 kinds of dynamic processes:

	(1) "Rock & Water" Relationship: 
These results are consistent to pure strategy analysis, that the game have 2 pure dorminant strategies

(M, W): (S, S)
![](sex_battle_3.png)

(M, W): (C, C)
![](sex_battle_2.png)
 
I call these results implying for "compromised relationship". Because to interpret the result, we can see that in the couple:
+ **"Rock"** 
	Strictly following his/her preference, even ignoring the beloved one. 
+ **"Water"**
	More flexible role in the relationship, hesitate when choosing the lover or his/her interest, even compromise to the beloved one.

What is fasinating is that you could literally see the "internal fight" from "Water"'s "heart", that they would always first approaching to their preference in the early iteration, but then suddenly make a sharp turn, and eventually cater to what the beloved prefer.

	(2) Counterbalance Relationship
This result is not predicted by pure strategy analysis, for (S, C) is not stable.
> The "stable" means that no players prone to switch his/her choice for better payoff.

![](sex_battle_2.png)

Intuitionally, it would be surprised to find the third result, (S, C) choice leads to far less payoff for both players. And when we see into the actual payoff, the first situation will lead to either(5000, 6000) or (6000, 5000), while the second situation only lead to (1000, 1000). Why would it happen?

The model itself should reason for this. Think back to "Rock & Water" relationship. In the early iterations, both players are approaching to their own preference. Once one of the players(let's say, **Rock**) first reach his threshold that high enough to make the other(so to be **Water**)'s payoff decline if water insist on his/her preference. Eventually, **Water** gets pushed back to cater to **Rock**'s preference (Or in a more flattering way, **Water** kindly compromised)

However, what if both happens to reach their high threshold nearly simutaneuosly (Rock & Rock), OR both are willing to compromise (Water & Water)? 
In **Rock & Rock** relationship, the high payoff from meet(5) becomes extremely low for its low possibility to happen, that it attracts neither of the player to cater.
In **Water & Water** relationship, (C, S), the worst result gets to happen too often that eventually, they "learned" the lesson, and choose to stay in their comfort zone.

More interestingly, if we repeat the game and average the iteration time that first reach NE, like we repeat **50** times, the average iteration time is: 8.71. That is to say, the average dating times for couple to adjusting to each other is around **9**.


--------------------------------------------------------------
Reminded by the "Paper, Scissor and Rock" game, different group number are also checked and see if the result is caused from random factors.


Unlike results in "Paper, Scissor and Rock" game, results in "Battle of Sex" are consistent to 2 patterns mentioned above, while results of "Paper, Scissor and Rock" game showed no regulat pattern.


BTW, the results above indeed, *Just Like Love* (￣▽￣)""
