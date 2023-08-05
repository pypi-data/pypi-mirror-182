__all__ = ['RedisLock']

import asyncio

from redis import asyncio as aioredis
# from aioredis.client import Client
# from aioredis.lock import Lock
Redis = aioredis.Redis
Lock = aioredis.lock.Lock


class RedisLock:
    '''
    A distributed lock.
    '''
    host: str
    port: int
    username: str | None
    password: str | None
    timeout: int | None
    client: Redis
    lock: Lock


    def __init__(self,
                 host: str,
                 port: int,
                 name: str | bytes,
                 db: str | int = 0,
                 username: str | None = None,
                 password: str | None = None,
                 timeout: int | None = None,
    ):
        # if isinstance(name, str):
        #     name = name.encode()

        self.host = host
        self.port = port
        self.name = name
        self.username = username
        self.password = password
        self.timeout = timeout
        self.client = Redis(host=host, port=port, username=username, password=password, db=db)
        self.lock = self.client.lock(name, timeout=timeout)


    async def __aenter__(self):
        await self.lock.acquire()
        return self


    async def __aexit__(self, exc_type, exc_value, exc_tb):
        if exc_type:
            await self.close()
            return self

        await self.lock.release()
        return self


    async def acquire(self, timeout: float = 10.0) -> bool:
        '''
        Acquire the lock.
        '''
        r: bool = await self.lock.acquire()
        return r


    async def release(self) -> bool:
        '''
        Release the lock.
        '''
        await self.lock.release()
        r: bool = True
        return r


    async def close(self):
        '''
        Close the lock.
        '''
        await self.client.close()


    async def is_acquired(self) -> bool:
        '''
        Check if this lock is currently acquired.
        '''
        is_acquired: bool = await self.lock.locked()
        return is_acquired


"""
async def main():
    HOST = 'etcd-test'
    PORT = 2379

    # lock0
    lock0 = EtcdLock(host=HOST, port=PORT, name='lock-0')
    await lock0.acquire()
    await asyncio.sleep(10.0)
    await lock0.release()
    await lock0.close()

    # lock1
    lock1 = EtcdLock(host=HOST, port=PORT, name='lock-1')
    
    async with lock1:
        await asyncio.sleep(10.0)
    
    await lock1.close()


if __name__ == '__main__':
    asyncio.run(main())
"""
