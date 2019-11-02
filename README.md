# Iterated_Prisoners_Dilemma_Model

In the classic "Prisoners' Dilemma" game, two suspects are required to propose whether or not the other is guilty, 
("Y" for yes; "N" for deny);
and the final penalty of each depends on both suspects choices.

Payoff here means the period suspect would spend in prison. 
Apparently, the less payoff is, the more suspect wants to get the result.

Below are payoff table:

| 1 \ 2 | Y | N|
|:----:|:----:|:----:|
| Y | (20,20) | (0,10) |
| N | (10, 0) | (3, 3) |

> When A chooses "YES" but B chooses "DENY", A will be released(0 year in prison), while B will spend 10 years in prison;
> When A chooses "YES" and B chooses "YES", A and B will both be in prison for 5 years;
> When A chooses "DENY" and B chooses "DENY", A and B will both be in prison for 3 years;

In traditional uniterated-game, we can get a dorminant strategy: both suspects will choose "Y".
> If one chooses "YES", I will get better result if I choose "YES"
> If one chooses "DENY", I will get better result if I choose "YES"
> Therefore, whatever the other person's choice, "YES" will always be a better choice.




Now let's change the payoff change, something more interesting happen:

Below are payoff table:

| 1 \ 2 | Y | N|
|:----:|:----:|:----:|
| Y | (20,20) | (0,10) |
| N | (10, 0) | (3, 3) |

> When A chooses "Y" but B chooses "D", A will be released(0 year in prison), while B will spend 10 years in prison;
> When A chooses "Y" and B chooses "Y", A and B will both be in prison for 20 years;
> When A chooses "D" and B chooses "D", A and B will both be in prison for 1 years;

To analyze this problem is to stand in one prison's shoes and guess:
if he/she chooses "YES", I will get better result if I choose "DENY"
if he/she chooses "DENY", I will get better result if I choose "YES"
Now the choice begins to osillate. And in the code the fluctuation can be shown directly.



