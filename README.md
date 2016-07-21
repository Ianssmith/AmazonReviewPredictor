# AmazonReviewPredictor
https://docs.google.com/presentation/d/1s0V5Rxpj1zC6UNL7ffNd-ScdfUDiF7aXAnSptVCEI8A/edit#slide=id.g1307426a92_0_36
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

##Update:
Running a count vectorizer on the Summary text of each review increased the 
models accuracy significantly. 

Based on this discovery further methods were run on the Summary and other 
text based elements of the data; Namely an NLTK Stemmer which was rolled into the CountVectorizer.
After this expansion the highest accuracy thus far was attained with
nearly a 50% increase in true positive rate. 

The Multinomial Naive Bayes classifier was chosen as the final model 
because while the overall accuracy was not the highest of the models run, 
it had a significantly higher true positive rate.(turns out 
if you guess that virtually none of the reviews are helpful 
you will have a relatively high true negative rate. :laughing:) 


