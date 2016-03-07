''' stuff that did not work and/or is being saved for later

Id = df['Id']
Productid = df['ProductId']
Userid = df['UserId']
Profile = ['ProfileName']
Score = df['Score']
Time = df['Time']
Summary = df['Summary']
Text = df['Text']

Id.reshape((455000,1))
Productid.reshape((455000,1))
Userid.reshape((455000,1))
Profile.reshape((455000,1))
Score.reshape((455000,1))
Time.reshape((455000,1))
Summary.reshape((455000,1))
Text.reshape((455000,1))
Id.tail()
Id.shape

uniqId stuff that didnt work:
#uniqids = np.unique(data.UserId)
#uniqids[:100]
#uniqids.shape
#type(uniqids)
#X = ravel(X)

#idcounts = idcounts.to_sparse(fill_value=0)
#idcounts = idcounts.as_matrix()
#idcounts.head(10)

#shape(idcounts)
#change object to numpy data type
#X = idcounts.as_matrix()
#type(X)
#X[:100]
#shape(X)


#y = (datacut.iloc[:, 12].values)

#y = ravel(y)

#type(uniqids)
#shape(uniqids)
#print(uniqids[:10])

#indices = np.nonzero(X) # a tuple of two arrays: 0th is row indices, 1st is cols
#X.tocsc()[indices]
#Xcounts = Xcounts.transpose()


#ids = data.UserId
#X = row_stack((X,ids))


#data['reviewLen'] = data['Text'].str.len()
#XScore = data.iloc[:, 7].values.reshape(data.shape[0], 1)
#XreviewLen = data.iloc[:, 13].values.reshape(data.shape[0], 1)
#Xtoadd = np.concatenate((XScore, XreviewLen), axis=1)
#Xtoadd

'''