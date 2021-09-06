
\newpage{}

# A004 - reducing dispersion by assigning a concrete value per word and learning from it

A001 collects as many different values for each word as it can get. When estimating, it uses any of those values more or less randomly (of cause smoothend by the fact that we take 100 random values and then only use a value from a certain position representing the percentage of certainty we want to have). Anyways, that hinders our ability to "learn". 

The idea behind this algorithm is to assign just one value to each word. This way, when we see our error margin we might design a little learning algorithm. 

For example:
- create an average model
- while the mean squared error is higher than ...
  - create 10 mutation of that model, for example by randomly adding or substracting 1/10th of the value to each weight of each word.
  - calculate the mean squared error for each mutation
  - take the model with the least mean squared error and repeat




