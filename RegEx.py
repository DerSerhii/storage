a1 = "(x+1)^125 Serhii chrome@intel.com  ss@ukr.net"

import re

''' 
    \d      Any Digit [0-9]
    \D      Any NON Digit [^0-9]
    \w      Any Alphabet and Digit and _ [a-zA-Z0-9_]
    \W      Any NON Alphabet and Digit and _
    \s      spase
    \S      NON spase 
    \.      dot
     
    [0-9]{3}                    --> ['123'] 
    [A-Z][a-z]+                 --> ['Serhii'] 
    [\w+\.\w+]                  --> ['google.com']   
    [\w._-]+@[\w._-]+\.[\w.]+   --> all email
    [\w._-]+@(?!intel\.com)[\w._-]+\.[\w.]+   --> all email (?! without intel.com)
'''

res = re.findall(r'[\w._-]+@(?!intel\.com)[\w._-]+\.[\w.]+', a1)

print(res)
