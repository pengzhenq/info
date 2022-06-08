from redis import Redis

redis_cli = Redis(host="192.168.139.131",port=6379,db=0)

# redis_cli.set('qqzzq','qqzzq')
# res = redis_cli.get('qqzzq')
# print(res)
redis_cli.delete('qqzzq')

print('helloworld')