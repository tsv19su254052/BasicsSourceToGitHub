# Interpreter 3.7 -> 3.11


# правки по оформлению
import asyncio
import aiohttp
import aiofiles
import socket
import platform
import os


# ветка Developers на GitHub-е - правка tsv19su 11
myhostname = socket.gethostname()
print(myhostname)
myfqdn = socket.getfqdn(myhostname)
print(myfqdn)
print(platform.node())
#hostname = os.uname()[1]
hostname = platform.uname()
print(hostname)
