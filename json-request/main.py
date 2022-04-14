import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()


class JsonItem(BaseModel):
    name: str
    email: str
    description: Optional[str] = None
    value: float = Field(..., gt=0, description="Nu poti sa ai valoare 0 (sa n-ai valoare)")


@app.post('/jsonItem')
async def create_item(item: JsonItem):
    print('Json is: ')
    print(item)


if __name__ == '__main__':
    uvicorn.run(app)
