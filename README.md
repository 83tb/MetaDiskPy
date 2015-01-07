This is a full python library for Metadisk API as stated in:
https://github.com/Storj/web-core#api-documentation

Sample usage:

```
from metadisk import *
```

Later you may need to change/setup metadisk_url in the metadisk.py file. Also you obviously don't have to "print" but it will be useful in the begining to see how the library works.

```
print download("bc2371a5592df676f0221bb940790cc389470e12c040e7fa79e1fedd4028f0e1?key=293902e516bce87b276d9f416d27059c6e9ce630ab15c38767ca63f5e2563cb9&token=XeWAT4uiQcBMqt2m")
print upload("test.txt")
print find("bc2371a5592df676f0221bb940790cc389470e12c040e7fa79e1fedd4028f0e1?key=293902e516bce87b276d9f416d27059c6e9ce630ab15c38767ca63f5e2563cb9&token=XeWAT4uiQcBMqt2m")
print status()
print new_token()
print get_prices()
print get_balance(new_token()['token'])
print redeem_code(new_token()['token'],"432234")
```


@ Kuba Kucharski, 2015, twitter.com/83tb
