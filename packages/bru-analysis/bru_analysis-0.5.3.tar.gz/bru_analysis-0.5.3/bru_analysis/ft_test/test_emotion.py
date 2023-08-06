import pandas as pd
from bru_analysis.sentiment_emotion import emotSent
from bru_analysis.common.nlp_utils import CleanText

FOLDER_DATA = '/home/oscar/Labs'

df_e = pd.read_csv(f'{FOLDER_DATA}/bru_analysis/bru_analysis/ft_test/data/Facebook/facebook_lib_facebook_comments.csv')
df_e = df_e.sample(n=15)

df_e['clean_text'] = df_e['message'].apply(lambda x: CleanText(x).process_text())

emotion = emotSent(df_p=df_e, batch=5).sentiment_emotion()

print(emotion[['_id', 'clean_text', 'emotion', 'sentiment']])
