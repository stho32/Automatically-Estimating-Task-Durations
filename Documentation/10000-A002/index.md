
\newpage{}

# A002 - Simply an average

## Description

Another algorithm could just calculate an average. Take all tasks and their durations, divide them by their count. Is this better?

From visually reviewing the data we know that most tasks have a duration of a few hours max. Some take very long.

An average is not just an average as we know. There are several ways to calculate one:

- there is the "simple average" that includes all data (A002.1)
- there is the possibility of a boxplot like calculation, include only the middle n% of the values (A002.2)

## Using the algorithm from powershell

### A002.1

Have a look at Quality-Assurance_A002_1_swe2020.ps1 if you need more. But actually it is just calculating the average. It is not even necessary to do this in a programming language alltogether.

```
$averageTaskDuration = ($historicData.DurationInSeconds | Measure-Object -Average).Average

$anyEstimation = $averageTaskDuration
```

### A002.2

For that average let us only use the middle 90% of duration values. That will cut extreme points and should reduce the error.

Quality-Assurance_A002_2_swe2020.ps1:
```
$historicData = $historicData | Sort-Object DurationInSeconds
$count = ($historicData | Measure-Object).Count
$fivePercent = [int]($count * 0.05)
$historicData = $historicData[$fivePercent..($count-$fivePercent)]
```

## How good is it?

### A002.1

**on swe2020 data**

Mean squared error: 765.929.757
Percent of estimates that are too high: 83,68 %

![QA a002.1 - swe 2020](Documentation/10000-A002/a002_1-swe2020.png)

**on swe2021 data**

Mean squared error: 321.140.140
Percent of estimates that are too high: 85,55 %

![QA a002.1 - swe 2021](Documentation/10000-A002/a002_1-swe2021.png)

### A002.2

**on swe2020 data**

Mean squared error: 780.036.288 
Percent of estimates that are too high: 69,01 %

![QA a002.1 - swe 2020](Documentation/10000-A002/a002_2-swe2020.png)

**on swe2021 data**

Mean squared error: 323.888.830  
Percent of estimates that are too high: 69,94 %

![QA a002.1 - swe 2021](Documentation/10000-A002/a002_2-swe2021.png)

