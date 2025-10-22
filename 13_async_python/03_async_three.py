
# Event loop

# just take and put every thing into the queue so that you can go back and working on our task .Once the task is complete this event loop is responsible to take back of that execution 	and start on the main  thread again other wise you are waiting because no way to check the function .. the event loop is responsible to check who is responsible 

import asyncio

import aiohttp

async  def fetch_url(session,url):
    async with session.get(url) as response:
        print(f"Fetch {url} with status {response.status}")
        
async def main():
    urls = ["https://httpbin.org/delay/3"] *3
    async with aiohttp.ClientSession() as session:
        task = [fetch_url(session,url) for url in urls]
        #task [t1,t2,t3] its all in the array 
        await asyncio.gather(*task)  # its like spread operator it unpacked directly 
        # await asyncio.gather(t1,t3,t3) 
        
        
        
asyncio.run(main())


# all then request come in same time


# blocking and non - blicking  exist 
