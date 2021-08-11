# Duration per Word

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


