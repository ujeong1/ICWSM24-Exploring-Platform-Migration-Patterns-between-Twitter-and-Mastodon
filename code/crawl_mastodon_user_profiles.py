from mastodon import Mastodon
from tqdm import tqdm
import pandas as pd


def get_api_data(user_id, instance_name):
    # You should change this ACCT and PASSWD according to the instance you crawl
    ACCT = "{your_mastodon_account_for_the_instance_you_crawl}"
    PASSWD = "{your_mastodon_account_password}"

    # Create an application and get client_id and client_secret
    Mastodon.create_app(
         'pytooterapp',
         api_base_url = f'https://{instance_name}',
         to_file = 'pytooter_clientcred.secret'
    )

    # Log in - either every time, or use persisted
    mastodon = Mastodon(
        client_id = 'pytooter_clientcred.secret',
        api_base_url = f'https://{instance_name}'
    )
    mastodon.log_in(
        ACCT,
        PASSWD,
        to_file = 'pytooter_usercred.secret'
    )
    user_data = mastodon.account(user_id)
    return user_data
    
output_filename = "{your_output_filename}.csv"    
df = pd.read_csv("../data/twitter_mastodon_users_id_mapped.csv")
mastodon_profiles = []
for i, user in tqdm(df.iterrows(), total=len(df)):
    user_id = int(user['mstdn_user_id'])
    hostname = user['mstdn_instance']
    try:
        user_json =get_api_data(user_id, hostname)
    except Exception as e:
        print(e)
        continue
    mastodon_profiles.append(user_json)
columns = mastodon_profiles[0].keys()
df = pd.DataFrame(mastodon_profiles, columns=columns)
df.to_csv(output_filename, index=False)
