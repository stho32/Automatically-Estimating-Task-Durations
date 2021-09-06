
\newpage{}

# A001 - Duration per Word

## The basic principle

Let us dive in with a very very simple algorithm. In fact it is the first algorithm I tought of. 

Let's say we have a task. May it read "Buy a big book and put it in the shelf". And this takes a certain amount of time. 

```
AmountOfTime = "Buy a big book and put it in the shelf"
```

Ok, I know, language doesn't really work like that. But lets us play stupid right now. We just split the thing into words and distribute the duration equally to each word. The sentence above is 10 words long, so each word gets a tenth of AmountOfTime associated with it.

Now we have a minimal time table. 

We can now take another input, like "Buy a small book".

We know the durations associated with "Buy", "a" and "book". We will have to do something about the unknown word. Ignore it, or add 10% to the sum of the known durations. Something like that. And voilà, we have a time estimate.

Funny thing: 

It is actually quite reasonable for the time being, that, in the absence of further information, assigning half the duration to each subtask is not the most stupid thing one could do. 

And it is actually quite reasonable to think that buying a small book is about the effort of buying a big one. But that is just the example. 

Anyways, we now have a time estimate and noone got hurt.

## Using the algorithm from powershell

The algorithm is added to EstimatePS, see Source/experiments/duration-per-word/experiment1.ps1 for a complete example with learning, caching and usage.

Finally it is as easy as:
```
$inSeconds = Get-DPWEstimate -Model $model -DurationInSecondsFor "add a new bookkeeping api" -ProbabilityInPercent 95
```

## How good is it?

As you can see there is a parameter in the algorithm, the "probability in percent" which decides if it should tend to higher values or not. Since it has influence and we want to know what that influence looks like I will use three different values for this validation:
25%, 50% and 75%. 

![QA a001 - swe 2020](10000-A001/a001_swe2020.png)

| Probability | Mean squared error | Percent guesses above real duration |
|-------------|--------------------|-------------------------------------|
|         25% |         46.205.433 |                              20,96% |
|         50% |         35.826.104 |                              51,33% |
|         75% |         28.595.545 |                              76,75% |

Our target mean squared error is 324.000.000
One hour is about 12.9 mio square seconds. 
Two hours is about 51.8 mio square seconds. That means that our error marin is about two hours here.

But this is the data we trained the model on, the 2020 tasks below 100000 seconds (which trims off only 12 tasks from more than 1000).

Now let us see how it performs on the 2021 tasks below 100000 seconds:

![QA a001 - swe 2021](./10000-A001/a001_swe2021.png)

| Probability | Mean squared error | Percent guesses above real duration |
|-------------|--------------------|-------------------------------------|
|         25% |         88.106.182 |                              25,96% |
|         50% |         84.227.983 |                              45,52% |
|         75% |         80.881.803 |                              70,20% |

We are still below our 5h target which makes the algorithm still acceptable, although the error margin is higher now. 

