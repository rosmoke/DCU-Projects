import urllib.request as url
import urllib.error as urlerror
urlp = 'https://ca117.computing.dcu.ie/einstein/progress'

# Create an OpenerDirector with support for Basic HTTP Authentication...
auth_handler = url.HTTPBasicAuthHandler()
auth_handler.add_password(realm='Connect2Field API',
                          uri=urlp,
                          user='asofied2',
                          passwd='voa9awe9')
opener = url.build_opener(auth_handler)
# ...and install it globally so it can be used with urlopen.
url.install_opener(opener)
f = url.urlopen(urlp)
print (f.read())