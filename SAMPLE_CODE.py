# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adpreview import AdPreview
from facebook_business.api import FacebookAdsApi

access_token = 'EAAaT5bZBbpF8BAJSBPrDuuRZB2iKTSP9dKNY2AVFsH9yp5aZAsRGqZAWVffsWO7BsZAu7g6RFZCvmnfbyhfmZCs9WTQkHZCI3ssW2fLEekzOWq3zkIozLfTMDJ9vk3es87Q82LuGEa6EVxtUWPFW78kzG8LCP9ZCy1R5fZAD0VjGQyCYM69vTd4d6u2IjMmZB3EJl8ZD'
ad_account_id = 'act_174072911572837'
app_secret = 'a540ac8b755bfb8f6abb044e0a521325'
page_id = '269881408229786'
app_id = '1851464831706207'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
    'name': 'My Campaign',
    'buying_type': 'AUCTION',
    'objective': 'REACH',
    'status': 'PAUSED',
}
campaign = AdAccount(ad_account_id).create_campaign(
    fields=fields,
    params=params,
)
print('campaign', campaign)

campaign_id = campaign.get_id()
print('campaign_id:', campaign_id, '\n')

fields = [
]
params = {
    'name': 'My AdSet',
    'optimization_goal': 'REACH',
    'billing_event': 'IMPRESSIONS',
    'promoted_object': {'page_id': page_id},
    'daily_budget': '1000',
    'campaign_id': campaign_id,
    'targeting': {'geo_locations':{'countries':['US']}},
    'status': 'PAUSED',
}
ad_set = AdAccount(ad_account_id).create_ad_set(
    fields=fields,
    params=params,
)
print 'ad_set', ad_set

ad_set_id = ad_set.get_id()
print 'ad_set_id:', ad_set_id, '\n'

fields = [
]
params = {
    'name': 'My Creative',
    'object_id': page_id,
    'title': 'My Page Like Ad',
    'body': 'Like My Page',
    'image_url': 'http://www.facebookmarketingdevelopers.com/static/images/resource_1.jpg',
}
creative = AdAccount(ad_account_id).create_ad_creative(
    fields=fields,
    params=params,
)
print 'creative', creative

creative_id = creative.get_id()
print 'creative_id:', creative_id, '\n'

fields = [
]
params = {
    'name': 'My Ad',
    'adset_id': ad_set_id,
    'creative': {'creative_id':creative_id},
    'status': 'PAUSED',
}
ad = AdAccount(ad_account_id).create_ad(
    fields=fields,
    params=params,
)
print 'ad', ad

ad_id = ad.get_id()
print 'ad_id:', ad_id, '\n'

fields = [
]
params = {
    'ad_format': 'DESKTOP_FEED_STANDARD',
}
print Ad(ad_id).get_previews(
    fields=fields,
    params=params,
)


