import uvicorn
from fastapi import FastAPI, UploadFile

app = FastAPI()


@app.post('/fileItem')
async def create_upload_file(file: UploadFile):
    print('Uploaded file name is: ')
    print(file.filename)


if __name__ == '__main__':
    uvicorn.run(app)
