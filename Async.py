# Interpreter 3.7


# правки по оформлению
# правка 02
import asyncio
import aiohttp
import aiofiles
import socket
import platform
import os


myhostname = socket.gethostname()
print(myhostname)
myfqdn = socket.getfqdn(myhostname)
print(myfqdn)
print(platform.node())
hostname = os.uname()[1]
hostname = platform.uname()
print(hostname)
