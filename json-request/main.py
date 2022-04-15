import uvicorn
from fastapi import FastAPI
from models import Event, VerdictResponse, Verdict

app = FastAPI()


@app.post('/scan_file', response_model=VerdictResponse)
async def scan_file(item: Event):
    file = Verdict(hash=item.file.file_hash, risk_level=-1)
    process = Verdict(hash=item.last_access.hash, risk_level=-1)
    response = VerdictResponse(file=file, process=process)

    return response


if __name__ == '__main__':
    uvicorn.run(app)
