
import re

_flags = re.UNICODE | re.IGNORECASE
ip_middle_octet = r'(\.(1?\d{1,2}|2[0-4]\d|25[0-5]))'
ip_last_octet = r'(\.([1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))'

word_pattern = re.compile(r'\S+', _flags)
word_in_parentheses_pattern = re.compile(r'(?!\()\S+(?=\))', _flags)
url_scheme_pattern = re.compile(r'\S+://', _flags)
twitter_mention_pattern = re.compile(r'^@([a-z_])([a-z\d_]*)$', _flags)
github_mention_pattern = re.compile(r'^@([a-z\d-]+)$', _flags)
email_pattern = re.compile(r'^[^\s@]+@[^\s@]+\.[^\s@]+$', _flags)

hashtag_pattern = re.compile(
    r'^'
    # Start with ＃ or #
    r'[＃#]'
    # Escape start with keypad unicode variations
    r'(?!\uFE0F\u20E3)'
    # Escape start with numbers
    r'(?!\d\d)(?!\d$)'
    # Escape multiple hash symbols
    r'(?![＃#]+$)'
    # Match hashtag
    r'(?:'
    # Match any (unicode) characters exclude symbols
    r'[^\s.,/#!$%^&*;:{\}=`()~@-]+|'
    # Exclude keypad unicode variation
    r'\*\uFE0F\u20E3|'
    r'#\uFE0F\u20E3)'
    r'$',
    _flags
)

# from: https://github.com/kvesteri/validators/blob/master/validators/url.py
url_pattern = re.compile(
    r'^'
    # protocol identifier
    r'((https?|ftp)://)?'
    # user:pass authentication
    r'([-a-z\u00a1-\uffff0-9._~%!$&\'()*+,;=:]+'
    r'(:[-a-z0-9._~%!$&\'()*+,;=:]*)?@)?'
    r'('
    # IP address exclusion
    # private & local networks
    r'((10|127)' + ip_middle_octet + r'{2}' + ip_last_octet + r')|'
    r'((169\.254|192\.168)' + ip_middle_octet + ip_last_octet + r')|'
    r'(172\.(1[6-9]|2\d|3[0-1])' + ip_middle_octet + ip_last_octet + r')'
    r'|'
    # private & local hosts
    r'(localhost)'
    r'|'
    # IP address dotted notation octets
    # excludes loopback network 0.0.0.0
    # excludes reserved space >= 224.0.0.0
    # excludes network & broadcast addresses
    # (first & last IP address of each class)
    r'([1-9]\d?|1\d\d|2[01]\d|22[0-3])'
    r'' + ip_middle_octet + r'{2}'
    r'' + ip_last_octet +
    r'|' 
    # IPv6 RegEx from https://stackoverflow.com/a/17871737
    r'\[(' 
    # 1:2:3:4:5:6:7:8
    r'([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|'
    #  1::                              1:2:3:4:5:6:7::
    r'([0-9a-fA-F]{1,4}:){1,7}:|'
    # 1::8             1:2:3:4:5:6::8  1:2:3:4:5:6::8
    r'([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|'
    # 1::7:8           1:2:3:4:5::7:8  1:2:3:4:5::8
    r'([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|'
    # 1::6:7:8         1:2:3:4::6:7:8  1:2:3:4::8
    r'([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|'
    # 1::5:6:7:8       1:2:3::5:6:7:8  1:2:3::8
    r'([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|'
    # 1::4:5:6:7:8     1:2::4:5:6:7:8  1:2::8
    r'([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|'
    # 1::3:4:5:6:7:8   1::3:4:5:6:7:8  1::8
    r'[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|'
    # ::2:3:4:5:6:7:8  ::2:3:4:5:6:7:8 ::8       ::
    r':((:[0-9a-fA-F]{1,4}){1,7}|:)|'
    # fe80::7:8%eth0   fe80::7:8%1
    # (link-local IPv6 addresses with zone index)
    r'fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]+|'
    r'::(ffff(:0{1,4})?:)?'
    r'((25[0-5]|(2[0-4]|1?[0-9])?[0-9])\.){3}'
    # ::255.255.255.255   ::ffff:255.255.255.255  ::ffff:0:255.255.255.255
    # (IPv4-mapped IPv6 addresses and IPv4-translated addresses)
    r'(25[0-5]|(2[0-4]|1?[0-9])?[0-9])|'
    r'([0-9a-fA-F]{1,4}:){1,4}:'
    r'((25[0-5]|(2[0-4]|1?[0-9])?[0-9])\.){3}'
    # 2001:db8:3:4::192.0.2.33  64:ff9b::192.0.2.33
    # (IPv4-Embedded IPv6 Address)
    r'(25[0-5]|(2[0-4]|1?[0-9])?[0-9])'
    r')\]|'
    # host name
    r'(([a-z\u00a1-\uffff0-9]-?)*[a-z\u00a1-\uffff0-9]+)'
    # domain name
    r'(\.([a-z\u00a1-\uffff0-9]-?)*[a-z\u00a1-\uffff0-9]+)*'
    # TLD identifier
    r'(\.([a-z\u00a1-\uffff]{2,}))'
    r')' 
    # port number
    r'(:\d{2,5})?' 
    # resource path
    r'(/[-a-z\u00a1-\uffff0-9._~%!$&\'()*+,;=:@/]*)??' 
    # query string
    r'(\?\S*)?' 
    # fragment
    r'(#\S*)?' 
    r'$',
    _flags
)
