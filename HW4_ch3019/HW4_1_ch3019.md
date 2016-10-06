### Null and Alternative Hypothesis

So as to not change your original idea too much, I would slightly adjust the null hypothesis to define the "longer" trips with something similar to a follows: "the number of men that take trips longer than 30 minutes on Citi Bike is the same or lower than the number of women that take trips longer than 30 minutes on Citi Bike".

If you did not want to specify a time you could change the hypothesis slightly with something like: "the average amount of time spent per Citi Bike trip for men is the same or lower than the average amount of time spent per Citi Bike trip for women". I think that unless you define a specific amount of time to be the threshold of a long trip versus a short trip thinking about the average trip length will be more telling. The average may also be a good measurement because different people may define a long trip as different amounts of time.

The alternative hypothesis being what you expect/want to happen would be "the number of men that take trips longer than 30 minutes on Citi Bike is higher than the number of women that take trips longer than 30 minutes on Citi Bike" or "the average amount of time spent per Citi Bike trip for men is higher than the average amount of time spent per Citi Bike trip for women", respectively.


### Data for the Project

I believe the data processed is what is needed to support the project. I would make a comment within the code when you manipulate the date to plot it just so it is clear that 1 = male and 2 = female riders. Also the trip duration information is reported as seconds so when reporting findings ensure this is noted. Perhaps convert the figures into minutes (divide values by 60) as it is a more common way to measure/discuss time.

### Test to Test H0

I suggest performing a t-Test because you a looking to answer the question "Do differences exist between 2 groups on one DV?" In this project, the dichotomous independent variable is gender and the dependent variable is trip ('longer ride' as however defined or amount of time').

### Additional Comments

I think once you flush out a final null/alternative hypothesis you will be able to report the findings of the performed test more accurately. Additionally, I would not scale down the data set to 100 as making your sample size larger will make your results more representative of Citi Bike users. Perhaps even use a .csv file from the warmer months where there will be more data entries.

