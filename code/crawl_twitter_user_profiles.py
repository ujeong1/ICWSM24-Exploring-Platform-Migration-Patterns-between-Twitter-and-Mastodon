import tweepy
from tqdm import tqdm

consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_token, access_token_secret
)

api = tweepy.API(auth)

output_filename = "{your_output_filename}.csv"
df = pd.read_csv("../data/twitter_mastodon_users_id_mapped.csv")
twitter_user_profiles = []
for i, row in tqdm(df.iterrows(), total=len(df)):
    user_id = row["twitter_user_id"]
    user_profile = api.get_user(user_id=user_id)
    twitter_user_profiles.append(user_profile)

df["twitter_user_profile"] = twitter_user_profiles
df.to_csv(output_filename, index=False)
