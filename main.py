import pandas as pd
df=pd.read_csv('spam.csv',encoding='ISO-8859-1')
df.head()

#run the lines on individual cell of jupyter notebook
df.drop(['unnamed2','unnamed3'],axis='columns',inplace=True)
df['spam']=df['category'].apply(lambda x: 1 if x=='spam' else 0 )
df.head()


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(df.message,df.spam,test_size=0.25)

from sklearn.feature_extraction.text import CountVectorizer
v=CountVectorizer()
x_train_count=v.fit_transform(x_train.values)
x_train_count.toarray()[:3]

from sklearn.naive_bayes import MultinomialNB
model=MultinomialNB()
model.fit(x_train_count,y_train)

emails=[
    'hey mohan,can we get together to watch football game tomorrow?',
    'Upto 20% discount on parking, exclusive offer just for you,Dont miss this reward!'
]
email_count=v.transform(emails)
model.predict(email_count)
