from lxml import etree
from selenium import webdriver
from optparse import OptionParser


# https://www.bing.com/search?q=site%3adouban.com&first=11
def bing():
    parse = OptionParser()
    parse.add_option('-d', '--domain', type='string', dest='domain', help='要爬取的主域名', default='jd.com')
    parse.add_option('-p', '--page_num', type='int', dest='page_num', help='要爬取的bing页数', default='3')

    values, args = parse.parse_args()
    print("传入参数：{}".format(values))
    print("多余参数：{}".format(args))

    # 根据 dest 获取参数
    domain = values.domain
    page = values.page_num

    print("目标域名：{}".format(domain))
    print("并发量：{}".format(page))

    page_urls = get_page_urls(page, domain)
    subdomain_urls = get_subdomain_urls(page_urls, domain)
    return subdomain_urls

def get_page_urls(page, domain):
    page_urls = []
    offsets = [(offset-1)*10+1 for offset in range(1, page+1)]
    for offset in offsets:
        url = 'https://www.bing.com/search?q=site%3a{}&first={}'.format(domain, offset)
        page_urls.append(url)
    return page_urls

def get_subdomain_urls(page_urls, domain):
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    driver = webdriver.Firefox(options=options)

    urls_set = []
    for page_url in page_urls:
        driver.get(page_url)
        result = driver.page_source
        html = etree.HTML(result)
        urls = html.xpath('//div[@class="b_attribution"]/cite/text()')
        for url in urls:
            if 'http' in url:
                urls_set.append(url + domain)
    return set(urls_set)

if __name__ == '__main__':
    result = bing()
    print(result)