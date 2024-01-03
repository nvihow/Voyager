from pydantic import BaseModel
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Literal,
    Mapping,
    Optional,
    Sequence,
    Set,
    Tuple,
    Union,
    cast,
)
from langchain_core.pydantic_v1 import BaseModel, Extra, Field, root_validator

class AzureChatModelConfig(BaseModel):
    """AzureChatOpenAI config profile"""
    openai_api_base: str = ''
    openai_api_version: str = ''
    deployment_name: str = ''
    openai_api_type: str = 'azure'
    openai_api_key: str = ''


class AzureOpenAIEmbeddingsConfig(BaseModel):
    """OpenAIEmbeddings config profile"""
    openai_api_base: str = ''
    model: str = ''
    openai_api_type: str = 'azure'
    deployment: str = ''
    openai_api_key: str = ''
    client: Any = Field(default=None, exclude=True)  #: :meta private:
