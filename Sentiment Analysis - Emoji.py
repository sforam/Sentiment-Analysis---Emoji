#!/usr/bin/env python
# coding: utf-8

# In[56]:


pip install textblob


# In[1]:


#importing TextBlob library for sentimental analysis
from textblob import TextBlob


# In[58]:


#Loading dataset
import pandas as pd
df = pd.read_csv('C:/Users/nancy/Downloads/test.csv')
df



# In[59]:


#creating a function for analysis using TextBlob
def get_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
   
    if sentiment > 0:
        return 'positive'
    elif sentiment == 0:
        return 'neutral'
    else:
        return 'negative'
    print(sentiment)


# Adding a new column with sentiment labels
df['sentiment'] = df['text'].apply(get_sentiment)



# In[60]:


#printing sentiment column
df


# In[61]:


#creating a polarity value column based on the text of sentiment column
for index, row in df.iterrows():
    # Get the text from the current row
    text = row['text']
    
    # Use TextBlob to get the polarity of the text
    polarity = TextBlob(text).sentiment.polarity
    
    # Add the polarity value to a new column in the dataframe
    df.at[index, 'polarity'] = polarity



# In[62]:


df


# In[63]:


#assinging emojis to sentiment values
emoji_dict = {
    'positive': '😍',
    'negative': '😩',
    'neutral' :'😀'
}

# Adding a new column with emojis
df['emoji'] = df['sentiment'].map(emoji_dict)



# In[64]:


#printing dataset converting analysis into emojis
df


# In[ ]:




