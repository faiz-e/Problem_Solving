#Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.


def is_valid_IP(string):
    octets = string.split('.')
    if len(octets) != 4 : return False
    for a in octets:
        if not(a.isnumeric()): return False
        if a[0] == '0' and len(a)>1: return False
        if not(int(a) >= 0 and int(a) <=255):
            return False
    return True


# or if you prefer to user regular expression 
# if you love short code

import re
def is_valid_IP(strng):
    return bool(re.match(r'^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])(\.(?!$)|$)){4}(?=$)',strng))
