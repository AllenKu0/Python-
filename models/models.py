from ast import literal_eval
import datetime
import json
import os
from typing import List, Dict

from sqlalchemy import Boolean, Integer, String, DateTime, LargeBinary, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped
from sqlalchemy.orm import mapped_column, relationship

engine = create_engine(
    os.environ.get(
        "SQL_URL",
        "postgresql://postgres:root@localhost:5432/postgres"
    )
)

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True, index=True)

    @declared_attr.directive
    @classmethod
    def __tablename__(cls):
        return cls.__name__.lower()
    
class EC2(Base):
    instance_Name: Mapped[str] = mapped_column(String)
    instance_family: Mapped[str] = mapped_column(String)
    instance_type: Mapped[str] = mapped_column(String)
    vCPU: Mapped[str] = mapped_column(String)
    memory: Mapped[str] = mapped_column(String)
    network: Mapped[str] = mapped_column(String)
    storage: Mapped[str] = mapped_column(String)
    on_demand_hourly_cost: Mapped[str] = mapped_column(String) 
    current_generation: Mapped[str] = mapped_column(String)
    potential_saving: Mapped[str] = mapped_column(String)
    # last_time: Mapped[datetime.datetime] = mapped_column(DateTime)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "InstanceName": self.instance_Name,
            "InstanceFamily": self.instance_family,
            "InstanceType": self.instance_type,
            "vCPU": self.vCPU,
            "Memory": self.memory,
            "Network": self.network,
            "Storage": self.storage,
            "OnDemandHourlyCost": self.on_demand_hourly_cost,
            "CurrentGeneration": self.network,
            "Potential saving": self.potential_saving,
        }

    def __repr__(self) -> str:
        return json.dumps(self.to_dict())

    def __str__(self) -> str:
        return json.dumps(self.to_dict())