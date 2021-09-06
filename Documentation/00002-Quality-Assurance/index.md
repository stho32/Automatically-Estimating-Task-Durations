
\newpage{}

# Quality Assurance 

Now if we create algorithms we need to say how good they are. For that we are using the following methods.  

## The graphical approach

One easy way would be to draw a graph which shows the predictions and the real values for time spent, while each task is understood as a category of its own.

We sort that graph by actual duration so we should see the distribution of durations and around that a hopping range of dots that describes what the algorithm tells us.

A better algorithm should be closer to the real data. Any algorithm should never match perfectly, as then we would have a 1:1 mapping. And that is an over-fit for sure.

## Mean squared error 

The mean squared error is a common approach to calculate a value for the quality of an algorithmi. It gets bigger with every estimate we did wrong.

The formula can be described as:

For every value you predict: 
  - Calculate the difference between the predicted value and the real value
  - Sum the squares of each difference
  - Divide all the sum by the count of the data entries you check

Now, since we want to prevent overfitting we need to prevent underfitting as well. Since we are talking about seconds and most of the recorded tasks have a duration in the range of up to 50000 seconds that means that most tasks are completed in about 13,89 hours.
So what about an error margin of about 5 hours. Which means just as something to think of, we want the squared error to not exceed squared(5x60x60) = 324.000.000 .

## Above and below

As a third criteria we have the idea that estimations might even each other out. In a prefect scenario this would mean that 50% of the estimations are too high while the other 50% are too low. To find out how good we match we add 1 to a variable for every estimation we find above the real value and then divide it by the number of tasks. The result should be .5 when hitting the target. 

## The Data

For training and estimating the quality of algorithms I use herein a dataset that consists of all the tasks that we at the software development shop at my employer recorded during the time between july and december 2020 and january 2021 to august 2021. That means there are two datasets available.

Unfortunately - since this is confidential information - I cannot publish it alongside this material. But the errors and images can be shared at it can advance the algorithms - and it is everything that I have right now. So that will do.

I'll call them: swe2020 and swe2021. 

Now let us get a glance at the data as well the first algorithm. 




