import urllib3
import regex


url= "https://codeforces.com/api/contest.list?gym=false"
conn_pool=urllib3.PoolManager()
resp= conn_pool.request("GET",url)

ret_data=resp.data.decode("utf-8")
print(ret_data)



