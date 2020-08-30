# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import time

from scrapy import signals
from DouYin.DouyinFun import *


class DouyinSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class DouyinDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class RandomUserAgent(object):
    def process_request(self, request, spider):
        STUB = ""
        url = 'https://api3-normal-c-lf.amemv.com/aweme/v1/im/group/share/?version_code=10.3.0&js_sdk_version=1.55.0.3&app_name=aweme&vid=C2E5976F-BC7C-43F3-BEAA-46E14DF616C7&app_version=10.3.0&device_id=3764332570087559&channel=App%20Store&mcc_mnc=46006&aid=1128&screen_width=750&openudid=0d1ae40e0147a7793ea10082d9a9469c76080f8e&cdid=48EC7C60-896E-408F-8F76-D5D25A36E490&os_api=18&ac=WIFI&os_version=13.6.1&device_platform=iphone&build_number=103020&iid=2163444591899117&device_type=iPhone8,1&is_vcd=1&idfa=F1B0785A-18C1-4060-A63F-B82A3D020F3A&share_type=2&share_scene=12&group_id={}'.format(6776519137922384387)
        cookies = 'd_ticket=5e30d08544e274f5c93d465e538386d35c277; odin_tt=73d7b7252b3114086297f00069d4b04c903ce78c58e6556a8a39143ebd247bd4fd0b4713b93f8126486519f72d27ad40eca5f3cc9cafb9014748f8bdde624503; sid_guard=471898e77b406a017c3acc5f5c27c8f3%7C1596176557%7C5184000%7CTue%2C+29-Sep-2020+06%3A22%3A37+GMT; uid_tt=e09eab304609eb8addb844d4e73fec05; sid_tt=471898e77b406a017c3acc5f5c27c8f3; sessionid=471898e77b406a017c3acc5f5c27c8f3; passport_csrf_token=4ba8109d55c7c9679e9f6630ad6a2feb; install_id=2427318944677447; ttreq=1$fc39d9c472c8c1ef3ffcf05559825698f269b47b'
        params = url[url.index('?') + 1:]
        s = getXGon(params, STUB, cookies)
        ts = str(time.time()).split(".")[0]
        gorgon = get_gorgon(ts, strToByte(s))

        request.headers.setdefault('authority', 'api3-normal-c-lf.amemv.com')
        request.headers.setdefault("x-tt-token", '00091549e1c9c85687b190363f7a97c66294103deea64cae92be63ed893da1856df385f3066575f4e3029f1cb1405818b9f')
        request.headers.setdefault("sdk-version", '1')
        request.headers.setdefault("user-agent", 'Aweme 10.3.0 rv:103020 (iPhone; iOS 13.6; zh_CN) Cronet')
        request.headers.setdefault("x-ss-dp", '1128')
        request.headers.setdefault("x-tt-trace-id", '00-0089231609872286b83408a916e10468-0089231609872286-01')
        request.headers.setdefault("accept-encoding", 'gzip, deflate, br')
        request.headers.setdefault("x-khronos", ts)
        request.headers.setdefault("x-gorgon", gorgon)


