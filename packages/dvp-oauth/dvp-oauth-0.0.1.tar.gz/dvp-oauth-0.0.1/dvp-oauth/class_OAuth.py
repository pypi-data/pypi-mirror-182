import requests
import json
import sys, os
import logging

from functools import wraps
from error import AuthClientError, MissingTokenError

# https://medium.com/@vinicius.ronconi/using-python-decorators-to-handle-expired-oauth-tokens-55e78316a188

config = json.load(open("config"))


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

py_handler = logging.FileHandler(f"{__name__}.log", mode='w')
py_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

py_handler.setFormatter(py_formatter)
logger.addHandler(py_handler)


def singleton(cls):
    @wraps(cls)
    def wrapper(*args, **kwargs):
        if not wrapper.instance:
            wrapper.instance = cls(*args, **kwargs)
        return wrapper.instance

    wrapper.instance = None
    return wrapper


def request_new_token():
    session = requests.Session()
    session.proxies = {
        "http": os.environ['QUOTAGUARDSTATIC_URL'], 
        "https": os.environ['QUOTAGUARDSTATIC_URL']
    }

    my_headers = {
          'Content-Type': 'application/x-www-form-urlencoded', 
          }
    params = {'grant_type': 'client_credentials'}

    resp = session.post(
              config['Authentication'],
              params = params,
              headers = my_headers, 
              data = {
                  'client_id':	config['client_id'],
                  'client_secret':	config['client_secret']
              }
          )
    
    a = json.loads(resp.content)
    print(a)
    token = a['access_token']
    return session, token


@singleton
class DVPOAuth:
    '''OAuth API for dvp app'''
    def __init__(self, token = None, session = None):
        self.token = token
        self.session = session
        

    ''' class decorator '''
    def _renew_token(foo):
        ''' private decorator '''
        def wrapper(self, *args, **kwargs):
            try:
                # print(f'token : {self.token}')
                logger.info(f'Existing token : {self.token}')
                return foo(self, *args, **kwargs)
            except (MissingTokenError, AuthClientError) as e:
                self.session, self.token = request_new_token()
                logger.info(f'New token : {self.token}')
                # print(f'token : {self.token}')
                return foo(self, *args, **kwargs)
        return wrapper
        
    @_renew_token
    def check_eligibility(self, account = None):
        if not self.token: raise MissingTokenError

        auth = 'Bearer '+ self.token
        eligibility_params = {
            'ContractAccountID': "\'" + account + "\'",
            'DUNSNumber': "\'" + config['DUNSNumber'] + "\'",
            '$format': 'json'
        }

        resp_query1 = self.session.get(
            config["Eligibility"],
            params=eligibility_params,
            headers={'Authorization': auth}
        )

        print(resp_query1.status_code)
        print(resp_query1.content)
        logger.info(f'Eligibiity status code : {resp_query1.status_code}')

        if resp_query1.status_code == 401:
            logger.exception("Eligibility 401 error.")
            raise AuthClientError
        

oauth = DVPOAuth()
oauth.check_eligibility('9714010007')
oauth2 = DVPOAuth()
print(oauth is oauth2)

# my_headers = {
#       'Content-Type': 'application/x-www-form-urlencoded', 
#       }
# params = {'grant_type': 'client_credentials'}

# resp = requests.post(
#           'https://ccapimqa.apimanagement.us21.hana.ondemand.com/v1/cc/OAuth/ClientCredentials/accesstoken',
#           params=params,
#           headers=my_headers, 
#           data={
#             'client_id':	'GlWTgF1B4hJ9LLO2IcxnrDwuqaM5v2T6',
#             'client_secret':	'1XmW2XJAzqM0kDiu'
#           }
#         )

# # print(resp)
# # print(resp.content)

# a = json.loads(resp.content)
# # print(a)

# token = a['access_token']
# print('request #1')
# print(token)

# # eligibility API

# auth = 'Bearer '+ token
# eligibility_params = {
#   'ContractAccountID': "'9714010007'",
#   'DUNSNumber': "'119560824'",
#   '$format': 'json'
#   }

# resp_query1 = requests.get(
#   'https://ccapimqa.apimanagement.us21.hana.ondemand.com/v1/cc/DSMVendorsInboundServices/ZDSMInquiry',
#   params=eligibility_params,
#   headers={'Authorization': auth}
# )
# print('request #2')
# print(resp_query1.content)

# # search API

# search_params = {
#   '$format': 'json',
#   '$filter': "InternetFunctionCode eq 'RETRACCT' and BillAccount eq '7063096361'",
#   '$expand': 'ZAcctSearchNav'
#   }

# resp_query2 = requests.get(
#   'https://ccapimqa.apimanagement.us21.hana.ondemand.com/v1/cc/DSMVendorsInboundServices/ZAcctSearchAndRetrieveSet',
#   params=search_params,
#   headers={'Authorization': auth}
# )
# print('request #3')
# print(resp_query2.content)

# # search API

# search_params = {
#   '$format': 'json',
#   '$filter': "InternetFunctionCode eq 'ACCTSRCH' and CallingApplication eq 'DSM' and ActiveBaOnly eq 'Y' and SearchType eq 'SSN' and SSN eq '1234'",
#   '$expand': 'ZAcctSearchNav'
#   }

# resp_query3 = requests.get(
#   'https://ccapimqa.apimanagement.us21.hana.ondemand.com/v1/cc/DSMVendorsInboundServices/ZAcctSearchAndRetrieveSet',
#   params=search_params,
#   headers={'Authorization': auth}
# )
# print('request #4')
# print(resp_query3.content)

