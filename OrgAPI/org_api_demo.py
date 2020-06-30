import hashlib
import hmac
import requests
import time


class Request(object):
    def __init__(self, api_key, secret_key, entry_point):
        if not entry_point.endswith("/"):
            entry_point = entry_point + "/"
        self.api_key = api_key
        self.secret_key = secret_key
        self.entry_point = entry_point

    def _request(self, uri, data, **kwargs):
        data["signature"] = self._generate_signature(data)
        # print("signature:%s" % data["signature"])
        kwargs["timeout"] = 60

        kwargs["headers"] = {
            "User-Agent": "wallex-P 1.0",
            "X-ACCESS-KEY": self.api_key,
        }
        response = requests.post(self.entry_point + uri, data=data, **kwargs)
        return self._handle_response(response)

    def _generate_signature(self, data):
        params = []
        for key, value in data.items():
            params.append("%s=%s" % (key, value))
        params.sort()
        original_str = ""
        for param in params:
            original_str = original_str + (param + "&")
        params_str = original_str[0:len(original_str) - 1]
        print("original_str:%s" % params_str)

        digest = hmac.new(
            self.secret_key.encode(encoding="UTF8"),
            params_str.encode(encoding="UTF8"),
            digestmod=hashlib.sha256,
        ).hexdigest()
        return digest

    @staticmethod
    def sorted_dict_values(data):
        items = data.items()
        items.sort()
        return [(key, value) for key, value in items]

    @staticmethod
    def _handle_response(response):
        print(response.text)
        # print(response.cookies)
        if not str(response.status_code).startswith("2"):
            raise Exception(response)
        try:
            return response.json()
        except ValueError:
            raise Exception("Invalid Response: %s" % response.text)


class OrgApi(Request):
    def time(self, **params):
        return self._request("basic/time", data=params)

    def tokens(self, **params):
        return self._request("basic/tokens", data=params)

    def quote_tokens(self, **params):
        return self._request("basic/quote_tokens", data=params)

    def symbols(self, **params):
        return self._request("basic/symbols", data=params)

    def login(self, **params):
        return self._request("user/login", data=params)

    def parse_token(self, **params):
        return self._request("user/parse_token", data=params)

    def get_base_info(self, **params):
        return self._request("user/get_base_info", data=params)

    def get_invite_info(self, **params):
        return self._request("user/get_invite_info", data=params)

    def user_balance(self, **params):
        return self._request("account/balance", data=params)

    def user_balance_flow(self, **params):
        return self._request("account/balance_flow", data=params)

    def create_order(self, **params):
        return self._request("order/create", data=params)

    def cancel_order(self, **params):
        return self._request("order/cancel", data=params)

    def get_order(self, **params):
        return self._request("order/get", data=params)

    def open_orders(self, **params):
        return self._request("order/open_orders", data=params)

    def trade_orders(self, **params):
        return self._request("order/trade_orders", data=params)

    def match_info(self, **params):
        return self._request("order/match_info", data=params)

    def my_trades(self, **params):
        return self._request("order/my_trades", data=params)

    def deposit_order_detail(self, **params):
        return self._request("asset/deposit/order/detail", data=params)

    def withdraw_order_detail(self, **params):
        return self._request("asset/withdraw/order/detail", data=params)

    def token_hold_detail(self, **params):
        return self._request("statistics/token_hold_detail", data=params)

    def token_hold_summary(self, **params):
        return self._request("statistics/token_hold_summary", data=params)

    def trade_fee(self, **params):
        return self._request("statistics/trade_fee", data=params)

    def trade_detail(self, **params):
        return self._request("statistics/trade_detail", data=params)

    def batch_transfer(self, **params):
        return self._request("finance/batch_transfer", data=params)

    def transfer(self, **params):
        return self._request("finance/transfer", data=params)

    def air_drop(self, **params):
        return self._request("finance/air_drop", data=params)

    def get_batch_transfer(self, **params):
        return self._request("finance/get_batch_transfer_result", data=params)

    def get_air_drop(self, **params):
        return self._request("finance/get_air_drop_result", data=params)

    def batch_lock(self, **params):
        return self._request("finance/batch_lock_position", data=params)

    def batch_unlock(self, **params):
        return self._request("finance/batch_unlock_position", data=params)

    def lock(self, **params):
        return self._request("finance/lock", data=params)

    def unlock(self, **params):
        return self._request("finance/unlock", data=params)

    def get_batch_lock_result(self, **params):
        return self._request("finance/get_batch_lock_position_result",
                             data=params)

    def get_batch_unlock_result(self, **params):
        return self._request("finance/get_batch_unlock_position_result",
                             data=params)

    def lock_record(self, **params):
        return self._request("statistics/lock_record", data=params)

    def unlock_record(self, **params):
        return self._request("statistics/unlock_record", data=params)

    def withdraw_quota_info(self, **params):
        return self._request("asset/withdraw/quota_info", data=params)

    def withdraw(self, **params):
        return self._request("asset/withdraw", data=params)


api = OrgApi(api_key='xxxxxx-xxxx-xxxxx',
             secret_key='xxxx-xxxx-xxxx',
             entry_point='https://www.xxxx.xx/api/v2/org/')

api.time()

api.user_balance(user_id='83214971450163200')
# api.get_invite_info(user_id='83214971450163200')

# api.get_base_info(user_id='387535761693773824')
# api.trade_fee(start_time=1561046400000, end_time=1561132800000)
# api.trade_detail(start_time=1566309620000, end_time=1566310220000, limit=20)
# api.addresses(user_id=97298429944266752)
# api.token_hold_detail(token_id='BTC', limit=20)
# api.token_hold_summary()