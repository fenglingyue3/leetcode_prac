import requests
import json

# res1 = requests.get('https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=10335871600&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1')
# res2 = res1.content
# # res2.content.decode("utf-8")
# # res3 = json.loads(res2)
# print(res2)
url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=10335871600&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
try:
    r = requests.get(url,headers=headers)
    r.raise_for_status()
except HTTPError as err:
    print("[error]({}):{}".format(r.raise_for_status(),r.text))
    raise
else:
    print("[debug]json.load(r.text):",json.loads(r.text))