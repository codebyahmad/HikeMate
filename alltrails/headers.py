# a web scraping project by ahmad

# This script provides the necessary headers and cookie values for web scraping AllTrails trail data.
# Cookie values are set for authentication and consent purposes. Make sure to update these values as needed.

# Instructions:
# 1. Replace the values for auth_token_value and datadome_value. To obtain these values:
#    - Visit https://www.alltrails.com
#    - First you should login so that an _auth_token is generated
#    - Open the browser's developer tools (F12)
#    - Go to the Network tab
#    - Refresh the page once
#    - Find the first request where the type is "document"
#    - Click on it, go to Headers, and in Request Headers tab locate the values for Cookie

# Set the values for cookie
referrer_value = "eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBZ2lIR2gwZEhCek9pOHZkM2QzTG1kdmIyZHNaUzVqYjIwdiIsImV4cCI6IjIwMjMtMTItMjBUMTk6MTI6NDdaIiwicHVyIjpudWxsfX0%3D--a3f2536cdf02605329106ed7a70196c4eccbb018"
cx_savetoday_shown_value = "true"
osano_consentmanager_uuid_value = "bc062375-59e7-451d-b66e-b0c8cdead2a6"
osano_consentmanager_value = "GELynzPAnBMNZTFAyUDjG5P-jXYlnGWbHXMgQ2CTwE4uVbZAR0E5zpmuSgkOK3v8nYHXWvurfDmNYUNx-19_yFD6rVe_-aQM4QMiKQrfqsTWHk17RKI2CGUPLFGIrFytsTw4tFzCRq9JvoaowkApYNpOwiZNQXgP4uumHgFWHA12o8P_HBTsn4N5_jlfL2m_09ZRyIkMdIIUnsIR9qOZlxzDYOvo30oPzv-o2ht_nAO35JWkuNQE27xaCFhH1MdWddTChfnjL1LvIgZfuIAuS6JJMpk="
G_ENABLED_IDPS_value = "google"
g_state_value = '{"i_p":1701126935130,"i_l":1}'
at_redirected_lang_amt_value = "1"
at_former_lang_code_pre_redirect_value = "en"
amp_6ad463_value = "b74b4722-1132-4f03-b09c-b51adc45ac42.........."
at_osano_value = "{%22consent%22:{%22ESSENTIAL%22:%22ACCEPT%22%2C%22STORAGE%22:%22DENY%22%2C%22MARKETING%22:%22DENY%22%2C%22PERSONALIZATION%22:%22DENY%22%2C%22ANALYTICS%22:%22DENY%22%2C%22OPT_OUT%22:%22ACCEPT%22}}"
at_redirected_lang_msg_shown_value = "true"
return_to_value = "https%3A%2F%2Fwww.alltrails.com%2F"
_auth_token_value = "xZwXw5swhmFk_mrJVY7K"
datadome_value = "aNKnFrUBLHtFTZMF0EhAoK_GP4oqci56bP0gRe2sFieidnMZwhqL3fmz0VWVbyr9u2iUuU6JlivZIU66uxavlFw3b1KNM4mXPOjYMHLsynkWJRryLV7ptWambEpHGwPx"
_alltrails_session_value = "Y0lNWU5jS1U4Tk94WEE4TWdTSU00T2tIN1IyMkpPL1VOcmlkeDFmcVVYQkF3Y0ZUQTlXV3FYRWJ5T3RrYWNaWS9ZZE1XYU8zTWNGeU5LOUdKMHVpN1RncC85T0c4VHQwTXV0d0lyNWNIL3J6UFZkSFExSXZYcjdBdUkyRzJ0eWFWMmh4ZXd0MHMwZ0FvUG5oUC9WUE1pWFE1UWdJQkQyMnZSTlZLSHU0RXF0TURiU0VKYUFMeGc0ZU9lcnZkeEFsRzdNeWtKV3ZiajMxR3lLVEZ3VzA5K2xjbjlhZEwxRjdwUENvdTR3QU1ZK1lzQ3JLQU5lTEtiTmJ2SUQxUjFlOE1xWlZrZzY5VCtLVjZscEJIZE9EemZySFl5VENoZzFCVU9aWEp5MlM2clllTGoxeGFtWHd1WVBiQk9ZK2FhNTNOWUVhMzF2ZjRSL0JQNWIra3FHOGh0aEVJS3RzdFpMQkY0TkVBTGdnOGRFUHpZdkR5d1plNE1qd2JqdzhVNEV2aDl1azViMURVdlByNGxYa1pFTUNSM05aMHA0RVZIa041Y21VYldqNUJIc3ZPcUR6RmNYWkROSnpnQlZJSnNVaURuT3cvNEpUVzVXSFQvQzJCb3hadEYyamFJZVRGc1FSbXN1c0hSeDE4SHZIR29GbGFpUXVVK252ZVFuK0o3VlpFQU05MHhUVmxUdlJucWRzcStWUWM2NHZFN01TMXZSK0M0NlloRHQwcWVCNjN5dFg1TCtQTjBWYWQzRGR0VEVKbGpjUkNwQ3ZQNTRVL04wOEk3bWxOeWxZRHpxaEowZDFML1Q3Q2FsbWl6QT0tLS9ITUYvRDJPT2g1NmRrQmFjZU16MWc9PQ%3D%3D--06f2dcfe20e47bce247385cd1bb58432cf9a23b4"

# Assign variables to headers for trail data
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Cookie": f"referrer={referrer_value}; cx_savetoday_shown={cx_savetoday_shown_value}; osano_consentmanager_uuid={osano_consentmanager_uuid_value}; osano_consentmanager={osano_consentmanager_value}; G_ENABLED_IDPS={G_ENABLED_IDPS_value}; g_state={g_state_value}; at_redirected_lang_amt={at_redirected_lang_amt_value}; at_former_lang_code_pre_redirect={at_former_lang_code_pre_redirect_value}; amp_6ad463={amp_6ad463_value}; at_osano={at_osano_value}; at_redirected_lang_msg_shown={at_redirected_lang_msg_shown_value}; return_to={return_to_value}; _auth_token={_auth_token_value}; datadome={datadome_value}; _alltrails_session={_alltrails_session_value}",
    "Dnt": "1",
    "If-None-Match": 'W/"1d6e354de51c5789eb8cd2bb35ccaae5"',
    "Sec-Ch-Device-Memory": "8",
    "Sec-Ch-Ua": '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    "Sec-Ch-Ua-Arch": '""',
    "Sec-Ch-Ua-Full-Version-List": '"Google Chrome";v="119.0.6045.160", "Chromium";v="119.0.6045.160", "Not?A_Brand";v="24.0.0.0"',
    "Sec-Ch-Ua-Mobile": "?1",
    "Sec-Ch-Ua-Model": '"Nexus 5"',
    "Sec-Ch-Ua-Platform": '"Android"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36"
}