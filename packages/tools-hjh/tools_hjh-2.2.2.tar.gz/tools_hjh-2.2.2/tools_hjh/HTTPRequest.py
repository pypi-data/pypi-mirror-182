# coding:utf-8
import requests
from tools_hjh import other as tools
import os


class HTTPRequest:
    """ 用户向网站提出请求的类 """

    def connect(self, url, headers=None, data=None, proxies=None, encoding='UTF-8'):
        """ 发出get或post请求, 返回状态码 """
        self.url = url.strip()
        self.headers = headers
        self.data = data
        self.proxies = proxies
        self.encoding = encoding
        
        try:
            if data is None:
                self.response = requests.get(self.url, headers=self.headers, proxies=self.proxies, stream=True, allow_redirects=True)
            else:
                self.response = requests.post(self.url, headers=self.headers, data=self.data, proxies=self.proxies, stream=True, allow_redirects=True)
            self.response.encoding = self.encoding
        except:
            pass
            
        return self.get_status_code()
                
    def get_size(self):
        """ 返回请求大小，现在如果报错会返回0 """
        try:
            head = requests.head(self.url, headers=self.headers, data=self.data, proxies=self.proxies, timeout=(3.05, 9.05))
            size = int(head.headers['Content-Length'])
        except:
            size = 0
        return size
        
    def get_text(self):
        """ 返回请求页面text, 异常返回空字符 """
        try:
            s = self.response.text
        except:
            s = ''
        return s
    
    def get_content(self):
        """ 返回请求页面content, 异常返回空字符 """
        try:
            s = self.response.content
        except:
            s = ''
        return s
    
    def download(self, dstfile, if_check_size=True):
        """ 下载请求的文件, 返回文件大小, 下载失败返回0, 不负责断网等问题需要重试相关 """
        path = dstfile.rsplit('/', 1)[0] + '/'
        tools.mkdir(path)
        
        # 判断文件是否已经存在，如果存在且大小一致，视为已下载，不重复下载
        content_size = self.get_size()
        if content_size > 0 and os.path.exists(dstfile):
            existsFileSize = os.path.getsize(dstfile)
            if existsFileSize == content_size:
                return existsFileSize
        elif content_size == 0:
            if_check_size = False
        
        download_size = 0
        try:
            with open(dstfile, 'wb') as f:
                for ch in self.response.iter_content(1024 * 64):
                    if ch:
                        download_size = download_size + f.write(ch)
        except:
            tools.rm(dstfile)
            download_size = 0
        finally:
            try:
                f.close()
            except:
                pass
            
        if if_check_size:
            if content_size != download_size:
                tools.rm(dstfile)
                download_size = 0
                
        return download_size
    
    def get_status_code(self):
        """ 返回请求状态码 """
        try:
            status_code = int(self.response.status_code)
        except:
            status_code = 0
        return status_code
    
    def close(self):
        self.response = None
        self.url = None
        self.headers = None
        self.data = None
    
    def __del__(self):
        self.close()
        
        
class Chrome():
    """ 使用浏览器解析url，返回源码
        __init__.param：
            chrome_path: chrome.exe路径
            chromedriver_path: chromedriver.exe路径
    """

    def __init__(self, chrome_path, chromedriver_path, is_hidden=False, is_display_picture=True, proxies=None):
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        if is_hidden:
            chrome_options.add_argument("--headless")
        chrome_options.binary_location = chrome_path
        if not is_display_picture:
            chrome_options.add_experimental_option('prefs', {'profile.managed_default_content_settings.images': 2})
        self.chrome = webdriver.Chrome(chromedriver_path, options=chrome_options)
        
    def close(self):
        self.chrome.close()
        
    def get(self, url, headers=None, data=None):
        self.chrome.get(url)
        return self.chrome.page_source
    
