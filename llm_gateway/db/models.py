# llm-gateway - A proxy service in front of llm models to encourage the
# responsible use of AI.
#
# Copyright 2023 Wealthsimple Technologies
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import enum

from sqlalchemy import JSON, Column, DateTime, Float, Integer, String
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Provider(enum.StrEnum):
    OPENAI = "openai_requests"
    COHERE = "cohere_requests"
    AWSBEDROCK = "awsbedrock_requests"


class ProviderRequest(Base):
    __tablename__ = "requests"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_input = Column(String, nullable=True)
    user_email = Column(String, index=True, nullable=True)
    temperature = Column(Float, nullable=True)
    created_at = Column(DateTime, index=True, nullable=False)
    extras = Column(JSON, nullable=True)
    response = Column(JSON, nullable=True)
    model = Column(String, nullable=True)
    endpoint = Column(String, nullable=False)
    provider = Column(
        ENUM(Provider, name="provider_type", create_type=False), nullable=False
    )
