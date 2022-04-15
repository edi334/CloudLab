import uvicorn
import aiohttp
from fastapi import FastAPI, UploadFile

app = FastAPI()


@app.post('/scan_file')
async def scan_file(file: UploadFile):
    url = 'https://beta.nimbus.bitdefender.net/liga-ac-labs-cloud/blackbox-scanner/'
    async with aiohttp.ClientSession() as session:
        async with session.post(
            url, data={'file': await file.read()}
        ) as response:
            res = await response.json()
            return res


if __name__ == '__main__':
    uvicorn.run(app, port=3000)
