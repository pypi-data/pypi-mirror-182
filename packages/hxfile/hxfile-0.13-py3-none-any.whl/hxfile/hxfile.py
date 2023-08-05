#!/usr/bin/env python3
#coding:utf-8
"""
  Author:  Hadi Cahyadi --<licface13@gmail.com>
  Purpose: hxfile unofficial API
  Created: 12/18/22
"""

from __future__ import print_function

import os, sys, signal, traceback, getpass, re
#from make_colors import make_colors
try:
    from pydebugger.debug import debug
except:
    def debug(*args, **kwargs):
        return ''
import argparse
try:
    from xnotify import notify
except:
    class notify:
        @classmethod
        def send(self, *args, **kwargs):
            return ''
        
from unidecode import unidecode
try:
    from jsoncolor import jprint
except:
    jprint = print
from configset import configset
from parserheader import Parserheader
try:
    from . import logger as LOGGER
except:
    import logger as LOGGER
if sys.version_info.major == 3:
    raw_input = input

import logging
logger = logging.getLogger('HXFile')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(LOGGER.CustomFormatter())
logger.addHandler(ch)

import requests
if sys.version_info.major == 3:
    from urllib.parse import urlparse, unquote, quote
else:
    from urlparse import urlparse
    from urllib import unquote, quote
from bs4 import BeautifulSoup as bs
import bitmath
from datetime import datetime
import clipboard

class Hxfile(object):
    CONFIG = configset()
    URL = 'https://hxfile.co/'
    PROXIES = {}
    HEADERS = Parserheader.parserheader()
    debug(HEADERS = HEADERS)
    API_KEY_TEMP = ""
    API_KEY = API_KEY_TEMP or ''
    SESSION = requests.session()
    SESSION.headers.update(HEADERS)
    ID = None
    
    def __init__(self, api_key = None, url = None, headers = None, configfile = None, proxies = {}, id = None, api_key_temp = None):
        if configfile:
            if os.path.isfile(configfile): self.CONFIG = configset(configfile)        
        self.API_KEY = api_key or api_key_temp or self.API_KEY or self.CONFIG.get_config('api', 'key')
        if api_key_temp:
            self.API_KEY_TEMP = api_key_temp
        debug(self_API_KEY = self.API_KEY)
        if not self.API_KEY:
            logger.error('No API Key !')
            #os.kill(os.getpid(), signal.SIGTERM)
        self.URL = url or self.URL or self.CONFIG.get_config('general', 'url')
        
        if not self.URL:
            logger.error('No URL input or from configfile !')
            os.kill(os.getpid(), signal.SIGTERM)        
        self.HEADERS = headers or self.HEADERS
        if isinstance(self.HEADERS, str):
            try:
                self.HEADERS = Parserheader.parserheader(self.HEADERS)
            except Exception as e:
                logger.error("Error parse headers: {}".format(e))
                if os.getenv('TRACEBACK'):
                    print(traceback.format_exc())
        self.PROXIES = proxies or self.PROXIES
        self.ID = id or self.ID
        
    @classmethod
    def logger(self, message, status="info"):
        logfile = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.basename(self.CONFIG.configname).split(".")[0] + ".log")
        if not os.path.isfile(logfile):
            lf = open(logfile, 'wb')
            lf.close()
        real_size = bitmath.getsize(logfile).kB.value
        max_size = self.CONFIG.get_config("LOG", 'max_size')
        debug(max_size = max_size)
        if max_size:
            debug(is_max_size = True)
            try:
                max_size = bitmath.parse_string_unsafe(max_size).kB.value
            except:
                max_size = 0
            if real_size > max_size:
                try:
                    os.remove(logfile)
                except:
                    print("ERROR: [remove logfile]:", traceback.format_exc())
                try:
                    lf = open(logfile, 'wb')
                    lf.close()
                except:
                    print("ERROR: [renew logfile]:", traceback.format_exc())


        str_format = datetime.strftime(datetime.now(), "%Y/%m/%d %H:%M:%S.%f") + " - [{}] {}".format(status, message) + "\n"
        with open(logfile, 'ab') as ff:
            if sys.version_info.major == 3:
                ff.write(bytes(str_format, encoding='utf-8'))
            else:
                ff.write(str_format)
    
    @classmethod
    def get_id(self, id = None):
        debug(id = id)
        id = id or self.ID
        url = ''
        debug(id = id)
        if id[:4] == 'http' and "://" in id:
            id = urlparse(id).path[1:]
            debug(id = id)
            debug(url = url)
        else:
            url = self.URL + id
            debug(url = url)
        return id, url
    
    @classmethod
    def get_url(self, url):
        debug(url = url)
        if not url[:4] == 'http' and not "://" in url:
            
            debug(check_url1 = url[:3])
            debug(check_url2 = url[:4])
            debug(check_url3 = not url[:3] == 'api')
            debug(check_url4 = not url[:4] == '/api')
            debug(check_final = not url[:3] == 'api' or not url[:4] == '/api')
            for i in range(0, 10):
                if url[:3] == 'api':
                    url = url = self.URL + url
                    debug(url = url)
                    break
                elif url[:4] == '/api':
                    url = url = self.URL[:-1] + url
                    debug(url = url)
                    break
                elif not url[:3] == 'api' and not url[:1] == "/":
                    url = self.URL + "api/" + url
                    debug(url = url)
                    break
                elif not url[:3] == 'api' and url[:1] == "/":
                    url = self.URL + "api" + url
                    debug(url = url)
                    break
                elif not url[:4] == '/api' and not url[:1] == "/":
                    url = self.URL + "api/" + url
                    debug(url = url)
                    break
                elif not url[:4] == '/api' and url[:1] == "/":
                    url = self.URL + "api" + url
                    debug(url = url)
                    break                
                elif not url[0] == "/":
                    url = self.URL + "api" + url
                    debug(url = url)
                    break
                elif url[0] == "/":
                    url = self.URL + "api" + url[1:]
                    debug(url = url)
                    break
                else:
                    url = self.URL + url
                    debug(url = url)
                    break
                
            debug(url = url)
        return url
    
    @classmethod
    def generate(self, url):
        id, url = self.get_id(url)
        if not id:
            logger.error("invalid id !")
            return False
        
        debug(id = id)
        data = {
                    'op':'download2',
                        'id':id,
                        'rand':'',
                        'referer':'',
                        'method_free':'',
                        'method_premium':''

                }

        download_link = ''
        headers = {
                    'acccept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'accept-encoding': 'gzip, deflate',
                        'content-type' : 'application/x-www-form-urlencoded',
                        'accept-language' : 'en-US,en;q=0.9',
                        'cache-control' : 'max-age=0',
                        'content-length' : '72',
                        'origin' : 'https://hxfile.co',
                        'referer' : url,
                        'sec-fetch-dest' : 'document',
                        'sec-fetch-mode' : 'navigate',
                        'sec-fetch-site': 'same-origin',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
                }

        debug(headers = headers)
        debug(data = data)
        a = requests.post(url, data = data, headers = headers)
        content = a.content
        debug(response_headers = a.headers)
        debug(response_cookies = a.cookies)
        debug(response_url = a.url)
        debug(dir_a = dir(a))
        debug(content = a.content)
        #sys.exit()
        b = bs(content, 'lxml')
        download_button = b.find('div', {'class':'download-button'})
        debug(download_button = download_button)
        
        if download_button:
            download_link = download_button.find('a')
            if download_link:
                download_link = download_link.get('href')
            else:
                download_link = ''
        debug(download_link = download_link)
        return download_link
    
    @classmethod
    def get(self, url, params = {}, api_key = None, id = None):
        if id: id, _ = self.get_id(id)
        url = self.get_url(url)
        debug(url = url)
        debug(id = id)
        api_key = api_key or self.API_KEY or self.CONFIG.get_config('api', 'key')
        debug(api_key = api_key)
        _params = {'key': api_key,}
        debug(params = params)
        if params: _params.update(params)
        if id: _params.update({'file_code': id,})
        debug(params = _params)
        a = requests.get(url, params = _params)
        debug(content = a.content)
        debug(the_url = a.url)
        logger.debug(a)
        if a:
            result = a.json()
            debug(result = result)
            return result
        return {'msg': "ERROR", 'status': 404, 'result': {},}
    
    @classmethod
    def post(self, url, data = {}, params = {}, id = None, api_key = None, files = {}):
        if id:
            id, url = self.get_id(id)
        else:
            url = self.get_url(url)
        debug(url = url)
        debug(id = id)
        api_key = api_key or self.API_KEY or self.CONFIG.get_config('api', 'key')
        debug(api_key = api_key)
        _params = {'key': api_key,}
        debug(params = params)
        if params: _params.update(params)
        debug(params = _params)
        a = requests.post(url, data = data, params = _params, files = files)
        debug(content = a.content)
        debug(the_url = a.url)
        logger.debug(a)
        if a:
            result = a.json()
            debug(result = result)
            return result
        return {'msg': "ERROR", 'status': 404, 'result': {},}
    
    @classmethod
    def account_info(self, api_key = None):
        api_key = api_key or self.API_KEY or self.CONFIG.get_config('api', 'key')
        debug(api_key = api_key)
        return self.get('account/info', api_key = api_key)
    
    @classmethod
    def account_stats(self, api_key = None, last = None):
        api_key = api_key or self.API_KEY or self.CONFIG.get_config('api', 'key')
        debug(api_key = api_key)
        params = {}
        if last and str(last).isdigit():
            params = {'last': str(last),}
        return self.get('account/stats', params, api_key)
    
    @classmethod
    def get_upload_server(self, api_key = None):
        return self.get('upload/server', api_key = api_key)
    
    @classmethod
    def upload(self, file, api_key = None):
        if not os.path.isfile(file):
            logger.error('invalid file !')
            return False
        server = None
        data_server = self.get_upload_server(api_key = api_key)
        sess_id = ''
        if data_server:
            if isinstance(data_server, dict):
                if  data_server.get('msg') == 'OK':
                    server = data_server.get('result')
                    sess_id = data_server.get('sess_id')
        if not server or not sess_id:
            return False
        files = {'file': open(file, 'rb'),}
        data = {'sess_id': sess_id}
        
        return self.post(server, data, files = files, api_key=api_key)
                    
    @classmethod
    def file_info(self, id):
        if not isinstance(id, list): id = [id]
        return self.get('file/info', id = ",".join(id))
    @classmethod
    def file_list(self):
        return self.get('file/list')
    @classmethod
    def file_rename(self, id, new_name):
        if not isinstance(id, list): id = [id]
        return self.get('file/rename', {'name': new_name,}, id = ",".join(id))
    @classmethod
    def file_clone(self, id):
        if not isinstance(id, list): id = [id]
        return self.get('file/clone', id = ",".join(id))
    @classmethod
    def file_direct_link(self, id):
        '''
            youre files only
        '''
        if not isinstance(id, list): id = [id]
        return self.get('file/direct_link', id = ",".join(id))        
    @classmethod
    def file_set_folder(self, id, folder_id):
        folder_id = str(folder_id)
        if not str(folder_id).isdigit():
            return {'msg': 'failed', 'status': 404,}
        return self.get('file/set_folder', {'fld_id': folder_id,})
    @classmethod
    def file_move(self, id, folder_id):
        return self.file_set_folder(id, folder_id)
    
    @classmethod
    def folder_list(self, folder_id = 0):
        folder_id = str(folder_id)
        if not str(folder_id).isdigit():
            return {'msg': 'failed', 'status': 404,}
        return self.get('folder/list', {'fld_id': folder_id,})
    
    @classmethod
    def folder_new(self, name, pid = 0):
        return self.get('folder/create', {'parent_id': pid, 'name': name,})
    
    @classmethod
    def create_folder(self, name, pid = 0):
        return self.folder_new(name, pid)
    
    @classmethod
    def folder_rename(self, id, new_name):
        return self.get('folder/rename', {'fld_id': id, 'name': new_name,})
    
    @classmethod
    def files_delete(self, last = 0):
        last = str(last)
        if not str(last).isdigit():
            return {'msg': 'failed', 'status': 404,}
        return self.get('files/deleted', {'last': last,})
    
    @classmethod
    def files_dmca(self, last = 0):
        last = str(last)
        if not str(last).isdigit():
            return {'msg': 'failed', 'status': 404,}
        return self.get('files/dmca', {'last': last,})
    
    @classmethod
    def download1(self, id):
        c1 = self.file_info(id)
        debug(c1 = c1)
        c2 = None
        c3 = None
        if not isinstance(c1, dict):
            return False
        #debug(check1 = (c1.get('msg') == 'OK' and c1.get('status') == 200 and c1.get('name')))
        logger.debug('prepare try get direct link')
        logger.debug('msg: {}'.format(c1.get('msg')))
        logger.debug('status: {}'.format(c1.get('status')))
        logger.debug('name: {}'.format(c1.get('name')))
        if c1.get('msg') == 'OK' and c1.get('status') == 200 and c1.get('result')[0].get('name'):
            logger.debug('try get direct link')
            c2 = self.file_direct_link(id)
            debug(c2 = c2)
        if not isinstance(c2, dict):
            return False
        if c2.get('msg') == 'no file':
            c3 = self.file_clone(id)
        else:
            c3 = c2
        debug(c3 = c3)
        if not isinstance(c3, dict):
            return False
        return self.file_direct_link(c3.get('result').get('filecode'))
    
    @classmethod
    def download2(self, id):
        return self.generate(id)
    @classmethod
    def login(self, username, password, redirect_url = None):
        '''
            still maintenance
        '''
        redirect_url = redirect_url or self.URL
        data = {
                'op':'login',
                'rand':'',
                'redirect': redirect_url,
                'login': username,
                'password': password,

            }

        headers = {
                    'acccept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'accept-encoding': 'gzip, deflate',
                        'content-type' : 'application/x-www-form-urlencoded',
                        'accept-language' : 'en-US,en;q=0.9,id;q=0.8',
                        'cache-control' : 'max-age=0',
                        'content-length' : '86',
                        'origin' : 'https://hxfile.co',
                        'referer' : self.URL + 'login.html',
                        'sec-fetch-dest' : 'document',
                        'sec-fetch-mode' : 'navigate',
                        'sec-fetch-site': 'same-origin',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
                        'cookie': 'lang=english',
                        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                }

        debug(headers = headers)
        debug(data = data)
        #self.SESSION.headers.update(headers)
        #return requests.session().post(self.URL, data = data, headers = headers)
        return self.SESSION.post(self.URL, data = data, headers = headers)
    
    @classmethod
    def my_files(self):
        '''
            still maintenance
        '''
        
        headers = {
                    'acccept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'accept-encoding': 'gzip, deflate',
                        'content-type' : 'application/x-www-form-urlencoded',
                        'accept-language' : 'en-US,en;q=0.9,id;q=0.8',
                        'referer' : self.URL + '?/op=my_files',
                        'sec-fetch-dest' : 'document',
                        'sec-fetch-mode' : 'navigate',
                        'sec-fetch-site': 'same-origin',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
                        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"'
                }
        headers = Parserheader.parserheader("""accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9,id;q=0.8
cookie: lang=english; login=cumulus13; xfss=i5bzueukevnoxlc6
referer: https://hxfile.co/
sec-ch-ua: "Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: same-origin
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36""")

        debug(headers = headers)        
        a = self.SESSION.get(self.URL, params = {'op': 'my_files',})
        debug(url = a.url)
        debug(content = a.content)
        print(a.content.decode('utf-8'))
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'my_files.html'), 'wb') as f:
            f.write(a.content)
            
    @classmethod
    def delete1(self, id, session = None):
        '''
            Not Impletement
        '''
        session = session or self.SESSION
        
        data = {'op':'my_files', 
                'token':'b79d7ef83803fb0c8d7da00280685a43',
                'fld_id':'0',
                'key': self.API_KEY, 
                'create_new_folder':'',
                'to_folder':'--',
                'file_id':id,
                'file_public':'on',
                'del_selected':'Delete selected',}
        debug(data = data)
        result = requests.session().post(self.URL, data = data)
        print(result.content.decode('utf-8'))
        
    @classmethod
    def delete(self, id):
        '''
            Not Implement
        '''
        if not isinstance(id, list): id = [id]
        return self.get('file/remove', id = ",".join(id))                
    
    @classmethod
    def downloader(self, url, download_path = None, saveas = None, confirm = False, copyurl_only = False, nodownload = False):
        print(make_colors("DOWNLOAD LINK:", 'b', 'lc') + " " + make_colors(url, 'b', 'ly'))
        debug(copyurl_only = copyurl_only)
        if copyurl_only:
            clipboard.copy(url)
            self.logger("downloader: {} --> clipboard".format(url), "debug")
            return url
        
        debug(download_path = download_path)
        debug(saveas = saveas)
        
        try:
            if not os.path.isdir(download_path) and not copyurl_only:
                download_path = None
        except:
            pass
        if not download_path and not copyurl_only and not nodownload:
            if os.getenv('DOWNLOAD_PATH'):
                download_path = os.getenv('DOWNLOAD_PATH')
            if self.CONFIG.get_config('DOWNLOAD', 'path', os.getcwd()):
                download_path = self.CONFIG.get_config('DOWNLOAD', 'path')
                debug(download_path_config = download_path)
        debug(download_path0 = download_path)

        #if not copyurl_only and not nodownload:
            #print(make_colors("DOWNLOAD_PATH:", 'lw', 'bl') + " " + make_colors(download_path, 'b', 'ly'))
        # sys.exit()
        if not download_path and not copyurl_only and not nodownload:
            download_path = ''
        if 'linux' in sys.platform and download_path and not os.path.isdir(download_path) and not copyurl_only and not nodownload:

            debug(download_path0 = download_path)
            if not os.path.isdir(download_path):
                this_user = getpass.getuser()
                login_user = os.getlogin()
                env_user = os.getenv('USER')
                debug(login_user = login_user)
                debug(env_user = env_user)
                this_uid = os.getuid()
                download_path = r"/home/{0}/Downloads".format(login_user)
                debug(download_path = download_path)

        if download_path and not os.path.isdir(download_path) and not copyurl_only and not nodownload:
            try:
                os.makedirs(download_path)
            except:
                pass

        if download_path and not os.path.isdir(download_path) and not copyurl_only and not nodownload:
            try:
                os.makedirs(download_path)
            except OSError:
                tp, tr, vl = sys.exc_info()
                debug(ERROR_MSG = vl.__class__.__name__)
                if vl.__class__.__name__ == 'OSError':
                    print(make_colors("Permission failed make dir:", 'lw', 'lr', ['blink']) + " " + make_colors(download_path, 'lr', 'lw'))


        if not download_path and not copyurl_only and not nodownload:
            download_path = os.getcwd()
        if download_path and not os.access(download_path, os.W_OK|os.R_OK|os.X_OK) and not copyurl_only:
            print(make_colors("You not have Permission save to dir:", 'lw', 'lr' + " " + make_colors(download_path, 'lr', 'lw')))
            download_path = os.getcwd()
        if not copyurl_only and not nodownload:
            print(make_colors("DOWNLOAD PATH:", 'lw', 'bl') + " " + make_colors(download_path, 'lw', 'lr'))
        debug(download_path = download_path)
        debug(url = url)
        try:
            from idm import IDMan
            d = IDMan()
        except:
            try:
                from pywget import wget as d
            except:
                logger.error("Can't download not module `idm` (win only) or `pywget`")
                return False

        debug(saveas = saveas)
        if sys.platform == 'win32':
            self.logger("downloader [win32]: downloading: {} --> {} --> {}".format(url, download_path, saveas))
            d.download(url, download_path, saveas, confirm = confirm)
            self.logger("downloader [win32]: finish: {} --> {} --> {}".format(url, download_path, saveas))
            
        else:
            self.logger("downloader [linux]: downloading: {} --> {} --> {}".format(unidecode(url), unidecode(url_download), unidecode(saveas)))
            debug(saveas = saveas)
            #pause()
            self.download_linux(url, download_path, saveas)
            self.logger("downloader [linux]: finish: {} --> {} --> {}".format(unidecode(url), download_path, unidecode(saveas)))
            
        icon = None
        if os.path.isfile(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logo.png')):
            icon = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logo.png')

        notify.send('HXFILE: download', url, 'hxfile', 'download', icon = icon)
        
        return url

    @classmethod
    def download_linux(self, url, download_path=os.getcwd(), saveas=None, cookies = {}, downloader = 'wget', check_file = True):
        '''
            downloader: aria2c, wget, uget, persepolis
        '''
        if saveas:
            saveas = re.sub("\.\.", ".", saveas)
        if not download_path or not os.path.isdir(download_path):
            if self.CONFIG.get_config('DOWNLOAD', 'path', os.getcwd()):
                download_path = self.CONFIG.get_config('DOWNLOAD', 'path')
        print(make_colors("DOWNLOAD_PATH (linux):", 'lw', 'bl') + " " + make_colors(download_path, 'b', 'ly'))
        print(make_colors("DOWNLOAD LINK [direct]:", 'b', 'lc') + " " + make_colors(url, 'b', 'ly'))
        if sys.version_info.major == 3:
            aria2c = os.popen("aria2c")
            wget = os.popen("wget")
            persepolis = os.popen("persepolis --help")
        else:
            aria2c = os.popen3("aria2c")
            wget = os.popen3("wget")
            persepolis = os.popen3("persepolis --help")

        if downloader == 'aria2c' and not re.findall("not found\n", aria2c[2].readlines()[0]):
            if saveas:
                saveas = '-o "{0}"'.format(saveas.encode('utf-8', errors = 'ignore'))
            cmd = 'aria2c -c -d "{0}" "{1}" {2} --file-allocation=none'.format(os.path.abspath(download_path), url, saveas)
            os.system(cmd)
            self.logger(cmd)
        elif downloader == 'wget':
            if sys.version_info.major == 2:
                if re.findall("not found\n", wget[2].readlines()[0]):
                    print(make_colors("Download Failed !", 'lw', 'r'))
                    return False
            filename = ''
            if saveas:
                if sys.version_info.major == 3:
                    filename = os.path.join(os.path.abspath(download_path), saveas)
                    saveas = ' -O "{}"'.format(os.path.join(os.path.abspath(download_path), saveas))
                else:
                    filename = os.path.join(os.path.abspath(download_path), saveas.decode('utf-8', errors = 'ignore'))
                    saveas = ' -O "{}"'.format(os.path.join(os.path.abspath(download_path), saveas.decode('utf-8', errors = 'ignore')))
            else:
                saveas = '-P "{0}"'.format(os.path.abspath(download_path))
                filename = os.path.join(os.path.abspath(download_path), os.path.basename(url))
            headers = ''
            header = ""
            if cookies:
                for i in cookies: header +=str(i) + "= " + cookies.get(i) + "; "
                headers = ' --header="Cookie: ' + header[:-2] + '"' + ' --header="User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36" ' + '--header="Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9" --header="Sec-Fetch-Site: same-origin" --header="Accept-Encoding: gzip, deflate, br" --header="Connection: keep-alive" --header="Upgrade-Insecure-Requests: 1" --header="Sec-Fetch-Mode: navigate" --header="Sec-Fetch-User: ?1" --header="Sec-Fetch-Dest: document"'
            cmd = 'wget -c "' + url + '" {}'.format(unidecode(saveas)) + headers
            if 'racaty' in url:
                cmd+= ' --no-check-certificate'
            print(make_colors("CMD:", 'lw', 'lr') + " " + make_colors(cmd, 'lw', 'r'))
            a = os.system(cmd)
            self.logger(cmd)
            if a:
                self.logger("It's seem error while downloading: {}".format(url), 'error')
            if self.CONFIG.get_config('policy', 'size'):
                size = ''
                try:
                    size = bitmath.parse_string_unsafe(self.CONFIG.get_config('policy', 'size'))
                except ValueError as e:
                    self.logger(str(e), 'error')
                if check_file:
                    if size and not bitmath.getsize(filename).MB.value > size.value:
                        print(make_colors("REMOVE FILE", 'lw', 'r') + " [" + make_colors(bitmath.getsize(filename).kB) + "]: " + make_colors(filename, 'y') + " ...")
                        os.remove(filename)
                        self.logger("File not qualify of size policy", 'critical')

        elif downloader == 'persepolis'  and not re.findall("not found\n", persepolis[2].readlines()[0]):
            cmd = 'persepolis --link "{0}"'.format(url)
            a = os.system(cmd)
            if a:
                self.logger("It's seem error while downloading: {}".format(url), 'error')
            self.logger(cmd)
        else:
            try:
                from pywget import wget as d
                d.download(url, download_path, saveas.decode('utf-8', errors = 'ignore'))
                self.logger("download: {} --> {}".format(url, os.path.join(download_path, saveas.decode('utf-8', errors = 'ignore'))))
            except Exception as e:
                print(make_colors("Can't Download this file !, no Downloader supported !", 'lw', 'lr', ['blink']))
                clipboard.copy(url)
                self.logger("download: copy '{}' --> clipboard".format(url), "error")
                self.logger(str(e), 'error')
    
    @classmethod
    def usage(self):
        parser = argparse.ArgumentParser('hxfile')
        parser.add_argument('-d', '--download', action = 'store', help = 'Download by given url or id/filecode, you can change use method "1" or "2" with -m/--method, default method is "2"', nargs = '*')
        parser.add_argument('-m', '--method', action = 'store', help = 'Download/Generate method: "2" download/generate url without API_KEY needed, but you must still input API_KEY to config file "hxfile.ini" for other function requirement, "1" download/generate with API_KEY flow check your file --> if not exists --> clone --> generate direct_link',  default = 1, type = int)
        parser.add_argument('-p',  '--download-path', action = 'store', help = 'Save download action file to directory')
        parser.add_argument('-n', '--save-as', action = 'store', help = 'Download save as')
        parser.add_argument('-i', '--info', action = 'store', help = 'Get File info')
        parser.add_argument('-I', '--account-info', action = 'store_true', help = 'Get Account Info')
        parser.add_argument('-S', '--account-stat', action = 'store',  help = 'Get Account Info Statistics')
        parser.add_argument('-u', '--upload', action = 'store', help = "Upload file", type = argparse.FileType('r'))
        parser.add_argument('-l', '--list-file', action = 'store_true', help = 'List all files')
        parser.add_argument('-L', '--list-folder', action = 'store', help = 'List all folder')
        parser.add_argument('-r', '--rename-file', action = 'store', help = 'Rename file', nargs = 2)
        parser.add_argument('-R', '--rename-folder', action = 'store', help = 'Rename folder', nargs = 2)
        parser.add_argument('-c', '--clone', action = 'store', help = 'Clone/Copy file from public link as youre file')
        parser.add_argument('-M', '--move', action = 'store', help = 'Move file to folder', nargs = 2)
        parser.add_argument('-C', '--mkdir', action = 'store', help = 'Create new Folder', nargs = 2)
        parser.add_argument('-sd', '--show-deleted', action = 'store_true', help = 'Show files delete along for x days')
        parser.add_argument('--api-key', action = 'store', help = 'set API_KEY')
        parser.add_argument('--api-key-temp', action = 'store', help = 'set API_KEY as temporary key')
        parser.add_argument('-g', '--generate', help = 'Generate link/id as direct download link', action = 'store', nargs = '*')
        parser.add_argument('--clip', help = 'Copy direct download url to clipboard', action = 'store_true')
        
        if len(sys.argv) == 1:
            parser.print_help()
        else:
            args = parser.parse_args()
            download_path = args.download_path or os.getcwd()
            saveas = args.save_as
            
            if args.api_key:
                self.CONFIG.write_config('api', 'key', args.api_key)
                self.API_KEY = args.api_key
            if args.api_key_temp:
                self.API_KEY = args.api_key_temp
            
            if args.download:
                for d in args.download:
                    if args.method == 1:
                        result = self.download1(args.download).get('result')
                        jprint(result)
                        if isinstance(result, list):
                            for i in result:
                                self.downloader(i.get('url'), download_path, saveas)
                                if args.clip: clipboard.copy(i.get('url'))
                        else:
                            self.downloader(result.get('url'), download_path, saveas)
                            if args.clip: clipboard.copy(result.get('url'))
                    elif args.method == 2:
                        url = self.download2(args.download)
                        if args.clip: clipboard.copy(url)
                        self.downloader(url, download_path, saveas)
            elif args.generate:
                for d in args.generate:
                    if args.method == 1:
                        result = self.download1(args.download).get('result')
                        jprint(result)
                        if isinstance(result, list):
                            for i in result:
                                url = i.get('url')
                                print(make_colors("{} --> {}".format(d, url)))
                                if args.clip: clipboard.copy(url)
                                
                        else:
                            self.downloader(result.get('url'), download_path, saveas)
                            if args.clip: clipboard.copy(result.get('url'))
                    elif args.method == 2:
                        url = self.download2(args.download)
                        self.downloader(url, download_path, saveas)
                        if args.clip: clipboard.copy(url)
                        
            elif args.info:
                jprint(self.file_info(args.info))
            elif args.account_info:
                jprint(self.account_info(self.API_KEY))
            elif args.account_stat:
                jprint(self.account_stats(args.api_ley, args.account_stat))
            elif args.upload:
                jprint(self.upload(args.upload, self.API_KEY))
            elif args.list_file:
                jprint(self.file_list())
            elif args.list_folder:
                jprint(self.folder_list(args.list_folder))
            elif args.rename_file:
                jprint(self.file_rename(args.rename_file[0], args.rename_file[1]))
            elif args.rename_folder:
                jprint(self.folder_rename(args.rename_folder[0], args.rename_foloder[1]))
            elif args.clone:
                jprint(self.file_clone(args.clone))
            elif args.move:
                jprint(self.file_move(args.move[0], args.move[1]))
            elif args.mkdir:
                jprint(self.folder_new(args.mkdir[0], args.mkdir[1]))
            elif args.show_deleted:
                jprint(self.files_delete(args.show_deleted))
        
if __name__ == '__main__':
    c = Hxfile()
    c.usage()
    #c.generate("qauxqrcx6fif")
    #https://hxfile.co/api/account/info?key=4534wit9lvakdohxjdv6
    #'http://hxfile.co/api/account/info?key=4534wit9lvakdohxjdv6
    #c.get1("/api/account/info")
    #print("test 1 " + "-" *100)
    #c.get1("api/account/info")
    #print("test 2 " + "-" *100)
    #c.get1("/account/info")
    #print("test 3 " + "-" *100)
    #c.get1("account/info")
    #print("test 4 " + "-" *100)
    #c.account_info()
    #c.account_stats(last = 7)
    #c.get("/api/account/stats", {'last': '7',})
    #c.get_upload_server()
    #c.upload(sys.argv[1])
    #jprint(c.file_info('https://hxfile.co/m13uao5l10rt'))
    #jprint(c.file_list())
    #jprint(c.file_rename('qauxqrcx6fif', 'data.ini'))
    #jprint(c.file_clone('qauxqrcx6fif'))
    #jprint(c.file_direct_link('gev07vy59qvt'))
    #jprint(c.file_direct_link('qauxqrcx6fif'))
    #jprint(c.folder_new('RAHASIA'))
    #jprint(c.file_list())
    #jprint(c.folder_list())
    #jprint(c.folder_rename('7107', 'test'))
    #jprint(c.folder_list())
    #jprint(c.files_delete(20))
    #jprint(c.files_dmca(20))
    #login = c.login('cumulus13', 'Xxxnuxer13')
    #c.delete('gev07vy59qvt', login)
    #debug(sess_cookies = login.cookies.get_dict())
    #c.my_files()
    #c.download1('m13uao5l10rt')
    #c.download2('m13uao5l10rt')
    #c.file_direct_link('m13uao5l10rt')
    #print(c.delete('orgal7ijydc8'))