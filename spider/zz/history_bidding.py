import requests

class History_bidding:

    def __init__(self):

        self.cateId = 101
        self.channel = 1322
        self.init_from = "4_1_7594_0"
        self.zzv = "7.5.0"
        self.tt = "47384E1A89F6AC306E8BC4908E2AFD25"
        self.auctionType = 0            # 拍卖类型
        self.businessType = 1           # 业务类型

        self.pageSize = 10
        self.fastSwitchOpt = 0          # 阀

        pass

    def _get_zhuanplusinfo(self):

        url = "https://app.zhuanzhuan.com/zz/transfer/getindexzhuanplusinfo"

        headers = {
            "Host": "app.zhuanzhuan.com",
            "Accept": "*/*",
            "Cookie": 'tk=833bec9025efa6ee1d55488a2ff42517dc8a6e22;uid=46028783232276;lon=113.9480794784491;idfa=3AC5544B-FA69-4DCC-8193-9CE31FA1822F;brand=Apple;PPU="TT=f1eb3e4ac7491731daaa9ce8592e44a0c1dd22e9&UID=46028783232276&SF=ZHUANZHUAN&SCT=1578545264708&V=1&ET=1581133664708"; Version=1; Domain=zhuanzhuan.com; Path=/;lat=22.52955052041277;t=16;sts=1578539644761;model=iPhone9%2C1;v=7.5.0;zz_t=16;',
            "User-Agent": "zhuanzhuan/7.5.0 (iPhone; iOS 13.3; Scale/2.00)",
            "Accept-Language": "zh-Hans-CN;q=1",
            "Accept-Encoding": "gzip,deflate",
            "Connection": "keep-alive"
        }

        try:
            res = requests.get(url, headers=headers)
            cookie = res.headers['Set-Cookie']
            print('cookie 1: ', cookie)
        except Exception as e:
            print('error : ', e)

    def _get_basicinfo(self):

        url = "https://app.zhuanzhuan.com/zz/transfer/getindexbasicinfo"

        headers = {
            "Host": "app.zhuanzhuan.com",
            "Accept": "*/*",
            "Cookie": 'tk=833bec9025efa6ee1d55488a2ff42517dc8a6e22;uid=46028783232276;lon=113.9480794784491;idfa=3AC5544B-FA69-4DCC-8193-9CE31FA1822F;brand=Apple;PPU="TT=f1eb3e4ac7491731daaa9ce8592e44a0c1dd22e9&UID=46028783232276&SF=ZHUANZHUAN&SCT=1578545264708&V=1&ET=1581133664708"; Version=1; Domain=zhuanzhuan.com; Path=/;lat=22.52955052041277;t=16;sts=1578539644761;model=iPhone9%2C1;v=7.5.0;zz_t=16;',
            "User-Agent": "zhuanzhuan/7.5.0 (iPhone; iOS 13.3; Scale/2.00)",
            "Accept-Language": "zh-Hans-CN;q=1",
            "Accept-Encoding": "gzip,deflate",
            "Connection": "keep-alive"
        }

        try:
            res = requests.get(url, headers=headers)
            cookie = res.headers['Set-Cookie']
            print('cookie 2: ', cookie)

            return cookie
        except Exception as e:
            print('error: ', e)

    def _get_fineness(self, cookie, xinghao_id):

        url = "https://app.zhuanzhuan.com/zzopen/ypdeal/getFineness?cateId={}".format(self.cateId)

        headers = {
            "Host": "app.zhuanzhuan.com",
            "Origin": "https://m.zhuanzhuan.com",
            "Cookie": cookie,
            "Connection": "keep-alive",
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 58ZhuanZhuan",
            "Accept-Language": "zh-cn",
            "Referer": "https://m.zhuanzhuan.com/u/bmmain/auctionroom/history?channel={}&init_from={}&cateId={}&xinghaoId={}&zzv={}&tt={}".format(self.channel, self.init_from, self.cateId, xinghao_id, self.zzv, self.tt),
            "Accept-Encoding": "gzip, deflate, br"
        }

        try:
            res = requests.get(url, headers=headers)
            print('成色:', res.status_code)
            print('成色:', res.text)

        except Exception as e:
            print('error: ', e)

        pass

    def _get_model_query_params(self, cookie, xinghao_id):

        url = "https://app.zhuanzhuan.com/zzopen/ypdeal/getModelQueryParams?cate3Id={}".format(xinghao_id)

        headers = {
            "Host": "app.zhuanzhuan.com",
            "Origin": "https://m.zhuanzhuan.com",
            "Cookie": cookie,
            "Connection": "keep-alive",
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 58ZhuanZhuan",
            "Accept-Language": "zh-cn",
            "Referer": "https://m.zhuanzhuan.com/u/bmmain/auctionroom/history?channel={}&init_from={}&cateId=&xinghaoId={}&zzv={}&tt={}".format(self.channel, self.init_from, self.cateId, xinghao_id, self.zzv, self.tt),
            "Accept-Encoding": "gzip, deflate, br"
        }

        try:
            res = requests.get(url, headers=headers)
            print('机型SKU选项:', res.status_code)
            print('机型SKU选项:', res.text)

        except Exception as e:
            print('error: ', e)

    def _get_brand_and_spu(self, cookie, xinghao_id):

        url = "https://app.zhuanzhuan.com/zzopen/ypdeal/getAuctionCate?cateId={}&auctionType={}&businessType={}".format(self.cateId, self.auctionType, self.businessType)

        headers = {
            "Host": "app.zhuanzhuan.com",
            "Origin": "https://m.zhuanzhuan.com",
            "Cookie": cookie,
            "Connection": "keep-alive",
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 58ZhuanZhuan",
            "Accept-Language": "zh-cn",
            "Referer": "https://m.zhuanzhuan.com/u/bmmain/auctionroom/history?channel={}&init_from={}&cateId={}&xinghaoId={}&zzv={}&tt={}".format(self.channel, self.init_from, self.cateId, xinghao_id, self.zzv, self.tt),
            "Accept-Encoding": "gzip, deflate, br"
        }

        try:
            res = requests.get(url, headers=headers)
            print('品牌和机型:', res.status_code)
            print('品牌和机型:', res.text)

        except Exception as e:
            print('error: ', e)

    def _get_history_list(self, cookie, pinpai_id, xinghao_id, pageNum = 500):
        '''
        获取历史列表
        :param cookie:
        :param pinpai_id:   品牌ID
        :param xinghao_id:  型号ID
        :param pageNum:     第几页
        :return:
        '''
        url = "https://app.zhuanzhuan.com/zzopen/ypdeal/getHistoryList?pageNum={}&pageSize={}&auctionType={}&businessType={}&fastSwitchOpt={}&pinpaiId={}&xinghaoId={}&cateId={}".format(pageNum, self.pageSize, self.auctionType, self.businessType, self.fastSwitchOpt, pinpai_id, xinghao_id, self.cateId)

        headers = {
            "Host": "app.zhuanzhuan.com",
            "Origin": "https://m.zhuanzhuan.com",
            "Cookie": cookie,
            "Connection": "keep-alive",
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 58ZhuanZhuan",
            "Accept-Language": "zh-cn",
            "Referer": "https://m.zhuanzhuan.com/u/bmmain/auctionroom/history?channel=1322&init_from=4_1_7594_0&cateId=101&xinghaoId=2101018011&zzv=7.5.0&tt=47384E1A89F6AC306E8BC4908E2AFD25",
            "Accept-Encoding": "gzip, deflate, br"
        }

        try:
            res = requests.get(url, headers=headers)
            print('历史交易列表:', res.status_code)
            print('历史交易列表:', res.text)


        except Exception as e:
            print('error: ', e)

    def _get_buyer_activity_detail(self, cookie, activity_id):

        url = "https://app.zhuanzhuan.com/zzopen/ypdeal/buyerActivityDetail?activityId={}&channel={}&init_from={}&zzv={}&tt={}".format(activity_id, self.channel, self.init_from, self.zzv, self.tt)

        headers = {
            "Host": "app.zhuanzhuan.com",
            "Origin": "https://m.zhuanzhuan.com",
            "Cookie": cookie,
            "Connection": "keep-alive",
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 58ZhuanZhuan",
            "Accept-Language": "zh-cn",
            "Referer": "https://m.zhuanzhuan.com/u/bmmain/auctionroom/{}?channel={}&init_from={}&zzv={}&tt={}".format(activity_id, self.channel, self.init_from, self.zzv, self.tt),
            "Accept-Encoding": "gzip, deflate, br"
        }

        try:
            res = requests.get(url, headers=headers)
            print('成交机型的SKU及机况详情:', res.status_code)
            print('成交机型的SKU及机况详情:', res.text)

        except Exception as e:
            print('error: ', e)



if __name__ == "__main__":
    history_bidding = History_bidding()

    cookie = history_bidding._get_basicinfo()
    pinpai_id = 2101018
    xinghao_id = 2101018011
    # history_bidding._get_fineness(cookie, xinghao_id)
    # history_bidding._get_model_query_params(cookie, xinghao_id)
    # history_bidding._get_brand_and_spu(cookie, xinghao_id)

    # history_bidding._get_history_list(cookie, pinpai_id, xinghao_id)

    activity_id = "300000000002058323"
    history_bidding._get_buyer_activity_detail(cookie, activity_id)

