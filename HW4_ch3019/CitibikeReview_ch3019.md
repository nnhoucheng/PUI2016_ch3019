Hi Reid Kelsey,

I have read your Assignment2 python notebook for Homework3. I will say that your Null and alternative hypothesis are formulated correctly. But it will be even better if you state your mathematical formulae in a more clear way.

Your mathematical formulae:
<img src="Screen Shot 2016-10-04 at 21.47.13.png" width="342" height="82">

It will be better:

$$ H_0: T_{Customer} \geqslant T_{Subscriber} $$

$$ H_1: T_{Customer} < T_{Subscriber} $$

You did a great job in cleaning and wrangling the original dataset. But I will be sorry to point out that your selected data is grouped in a wrong way if you want to test for your null hypothesis. Your statement is

<img src="Screen Shot 2016-10-04 at 22.13.27.png" width="753" height="81">

So you should group the data by weeks(Typically, a month has 4 week) instead of by weekdays.

If you would like to test for the null hypothesis, I would prefer to use of t-test ranther than z-test. It is because that we don’t know the population variance/standard deviation.