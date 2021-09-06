
\newpage{}

# Introducing Quality Assurance 

Now we have our first easy algorithm. Now we need something to tell how good it is. 

## The graphical approach

One easy way would be to draw a graph wich shows the predictions and the real values for time spent, while each task is understod a category of its own.

## The numerical approach

The mean squared error is a common approach to calculate a value for the quality of an algorithm.

The formula can be described as:

For every value you predict: 
  - Calculate the difference between the predicted value and the real value
  - Sum the squares of each difference
  - Divide all the sum by the count of the data entries you check

## Or/And both combined

Since we are not limited by any constraints here 

## The Data

For training and estimating the quality of algorithms I use herein a dataset that consists of all the tasks that we at the software development shop at my employer recorded during the time between july and december 2020 and january 2021 to august 2021. That means there are two datasets available.

Unfortunately - since this is confidential information - I cannot publish it alongside this material. But the errors and images can be shared at it can advance the algorithms - and it is everything that I have right now. So that will do.

I'll call them: swe2020 and swe2021. 

Now let us get a glance at the data as well the first Duration-Per-Word-Algorithm. 




