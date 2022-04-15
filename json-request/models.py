from pydantic import BaseModel
from uuid import UUID


class Time(BaseModel):
    a: int
    m: int


class Device(BaseModel):
    id: UUID
    os: str


class FileIn(BaseModel):
    file_hash: str
    file_path: str
    time: Time


class AccessEntity(BaseModel):
    hash: str
    path: str
    pid: int


class Verdict(BaseModel):
    hash: str
    risk_level: int


class Event(BaseModel):
    device: Device
    file: FileIn
    last_access: AccessEntity


class VerdictResponse(BaseModel):
    file: Verdict
    process: Verdict
