from facebookads.api import FacebookAdsApi
from facebookads.adobjects.business import Business
from facebookads.adobjects.campaign import Campaign
from facebookads.adobjects.adset import AdSet
from facebookads.adobjects.ad import Ad
from facebookads.adobjects.adsinsights import AdsInsights

from datetime import date

# Regex, for name search (Campaigns, Ad Sets, Ads)
# import regex

# Importing getpass module to automatically discover my user:
import getpass
user = getpass.getuser()
path = '/Users/' + user + '/Desktop/'
print('Selected path for your my_facebook_access.py:', path)

# Importing my_facebook_access.py file,
# where I store my Facebook private information, located on the Desktop:
import sys
sys.path.append(path)
from my_facebook_access import my_app_id,
                               my_app_secret,
                               my_access_token,
                               my_business_id,
                               campaigns_group

# print("my_app_id:", my_app_id)
# print("my_app_secret:", my_app_secret)
# print("my_access_token:", my_access_token)
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
my_business = Business(fbid=my_business_id)
# print("my_business:", my_business)
my_accounts = list(my_business.get_assigned_ad_accounts())
# print("All accounts:", my_accounts)

selected_account = my_accounts[0]
print("selected_account:", selected_account)

fields = [
    AdsInsights.Field.campaign_name,
    AdsInsights.Field.cpc,
    AdsInsights.Field.cpm,
    AdsInsights.Field.ctr,
    AdsInsights.Field.impressions,
    AdsInsights.Field.frequency,
    AdsInsights.Field.spend
]

params = {
    'time_range': {'since': str(date(2017, 1, 1)), 'until': str(date.today())},
    'level': 'campaign',
    'limit': 1000,
    'configured_status': 'ACTIVE'
}

insights = selected_account.get_insights(fields=fields, params=params)
print(insights)