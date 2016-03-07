# AmazonReviewPredictor
Machine learning model to predict the "helpfulness" rating of Amazon product reviews.

For the first iteration additional features seem to add only
slight incrememntal inreases in predictive power if any at all

The UniqueIDs feature did not seem to produce any value for the model and may even have decreased 
the models overall accuracy;

Struggeling to find an effective method to include counts of multiple reviews by individual users
as a feature I ended up stripping out users who did not write more than one review, effectively 
cutting the amount of data I had to work with in half.

Adding the additional features which I included in the original data set resulted in a similar bump in 
accuracy in the smaller data set, but there is not enough evidence to suggest the decrease in accuracy
seen in the repeat review writers trial would be remedied by including the rest of the data.
We'll see.
