from datetime import datetime
from pydantic import BaseModel
from ipaddress import IPv4Address
from enum import Enum


class NATEventTypeEnum(int, Enum):
    CREATED = 1
    DELETED = 2
    UPDATED = 3


class NATSessionMapping(BaseModel):
    timestamp: datetime
    host: IPv4Address
    event: NATEventTypeEnum
    vrf_id: int | None
    protocol: int
    src_ip: IPv4Address
    src_port: int
    x_ip: IPv4Address
    x_port: int
    dst_ip: IPv4Address
    dst_port: int


class NATAddressMapping(BaseModel):
    timestamp: datetime
    host: IPv4Address
    event: NATEventTypeEnum
    vrf_id: int | None
    src_ip: IPv4Address
    x_ip: IPv4Address


class NATPortMapping(BaseModel):
    timestamp: datetime
    host: IPv4Address
    event: NATEventTypeEnum
    vrf_id: int | None
    protocol: int
    src_ip: IPv4Address
    src_port: int
    x_ip: IPv4Address
    x_port: int


class NATPortBlockMapping(BaseModel):
    timestamp: datetime
    host: IPv4Address
    event: NATEventTypeEnum
    vrf_id: int | None
    protocol: int
    src_ip: IPv4Address
    x_ip: IPv4Address
    start_port: int
    end_port: int
