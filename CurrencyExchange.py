'''A simple script using a currency api to return the desired conversion.

The way to use this script is to pass in the arguments at the comman line.

e.g.
Passing in:
    >> CurrencyExchange.py 30 EUR USD
returns:
    >> The rate is: 1.0958
    >> New Amount:  32.87 USD'''

import requests
import json
import sys

# Unpacks the arguments passed in at the command line
script, curr_amt, curr_code, conv_curr_code = sys.argv

url = '''http://currency-api.appspot.com/api/%s/%s.json?amount=%s''' % (curr_code,
                                                        conv_curr_code, curr_amt)

# Grabs the site
site = requests.get(url)

# Loads the response that should be JSON
results = json.loads(site.text)
# Makes sure that the response was a success.
if results['success']:
    try:
        # Asserts that the rate is a string and the ammount is a decimal
        assert (type(results['rate']) == str)
        assert (type(results['amount']) == float)
        print("The rate is: %.6s" % results['rate'])
        print("New Amount: ",results['amount'],conv_curr_code)
    except:
        # If one of the asserts fails, than this code runs.
        # Sometimes the amount isn't a float.
        print("The rate is: %.6s" % results['rate'])
        print("New Amount: ",results['amount'],conv_curr_code)
else:
    # If the response isn't returned then this runs.
    print("Oops, something went wrong! Check the currency codes again.")
    print("If it still doesn't work, then those codes are not supported.")
