from fabric import Connection

c = Connection('qnbaasshell1.juniper.net', user='rlai', connect_kwargs={'password': 'Louise1217!!'})
result = c.run('uname -s')
print(result)
print(result.stdout.strip())