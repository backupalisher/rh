from requests_html import HTMLSession


ip = "http://192.168.1.72"
url_list = ["/js/jssrc/model/dvcinfo/dvccounter/DvcInfo_Counter_ScanCounter.model.htm",
            "/js/jssrc/model/dvcinfo/dvccounter/DvcInfo_Counter_PrnCounter.model.htm",
            "/js/jssrc/model/startwlm/Hme_DvcSts.model.htm",
            "/js/jssrc/model/dvcinfo/dvcconfig/DvcConfig_Config.model.htm",
            "/js/jssrc/model/startwlm/Hme_Toner.model.htm"]

if __name__ == '__main__':
    session = HTMLSession(verify=False)
    with open('model.gz', 'wt') as html_data:
        for url in url_list:
            r = session.get(ip + url)
            r.html.render()
            html_data.write(f'\r' + ip + url + f'\r')
            html_data.write(r.html.html)
