from voyager import Voyager
from voyager.agents import AzureChatModelConfig, AzureOpenAIEmbeddingsConfig
import myapi
import os

# You can also use mc_port instead of azure_login, but azure_login is highly recommended
azure_login = {
    "client_id": "YOUR_CLIENT_ID",
    "redirect_url": "https://127.0.0.1/auth-response",
    "secret_value": "[OPTIONAL] YOUR_SECRET_VALUE",
    "version": "fabric-loader-0.14.18-1.19", # the version Voyager is tested on
}

azure_url = myapi.azure_url
azure_api_key = myapi.azure_key
azure_api_version = myapi.azure_api_version

openai_api_key = azure_api_key

replacement_dict = {
    "text-davinci-003": "test1", # gpt-3.5-turbo
    "text-davinci-002": "test1", # gpt-3.5-turbo
    "text-embedding-ada-002": "deployment-a56b6b39a32e45b18c7e186270b9b310",
    "gpt-4-32k": "gpt-4-32k",
    "gpt-4": "test-gpt-4",
    "gpt-35-turbo": "test1",  # gpt-3.5-turbo
    "gpt-3.5-turbo": "test1", # gpt-3.5-turbo
}

def GetAzureDeploymentName(model):
    return replacement_dict.get(model)

# If you are using OpenAI LLM deployments on Azure, you can config them here
azure_gpt_4_config = AzureChatModelConfig(
    openai_api_base=azure_url,
    openai_api_version=azure_api_version,
    deployment_name=GetAzureDeploymentName('gpt-4'),
    openai_api_type="azure",
    openai_api_key=azure_api_key,	# Not API keys with prefix "sk-"
)
azure_gpt_35_config = AzureChatModelConfig(
    openai_api_base=azure_url,
    openai_api_version=azure_api_version,
    deployment_name=GetAzureDeploymentName('gpt-35-turbo'),
    openai_api_type="azure",
    openai_api_key=azure_api_key,	# Not API keys with prefix "sk-"
)
azure_openai_embeddings_config = AzureOpenAIEmbeddingsConfig(
    openai_api_base=azure_url,
    model=GetAzureDeploymentName('gpt-35-turbo'),
    openai_api_type="azure",
    deployment=GetAzureDeploymentName('gpt-35-turbo'),
    openai_api_key=azure_api_key,	# Not API keys with prefix "sk-"
)

# voyager = Voyager(
#     azure_login=azure_login,
#     openai_api_type="azure",
#     azure_gpt_4_config=azure_gpt_4_config,
#     azure_gpt_35_config=azure_gpt_35_config,
#     azure_openai_embeddings_config=azure_openai_embeddings_config,
# )
voyager = Voyager(
    #azure_login=azure_login,
    mc_port=myapi.my_mc_port,
    openai_api_type="azure",
    azure_gpt_4_config=azure_gpt_4_config,
    azure_gpt_35_config=azure_gpt_35_config,
    azure_openai_embeddings_config=azure_openai_embeddings_config,
    openai_api_key=openai_api_key,
)

print('当前目录路径:', os.getcwd())
print('当前文件路径:', os.path.realpath(__file__))

# start lifelong learning
voyager.learn()