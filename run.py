import myapi
from voyager import Voyager

print(myapi.my_api_key)
print(myapi.my_mc_port)

# You can also use mc_port instead of azure_login, but azure_login is highly recommended
azure_login = {
    "client_id": "YOUR_CLIENT_ID",
    "redirect_url": "https://127.0.0.1/auth-response",
    "secret_value": "[OPTIONAL] YOUR_SECRET_VALUE",
    "version": "fabric-loader-0.14.18-1.19", # the version Voyager is tested on
}
mc_port = myapi.my_mc_port
env_wait_ticks = 100
openai_api_key = myapi.my_api_key

voyager = Voyager(
    #azure_login=azure_login,
    mc_port=mc_port,
    env_wait_ticks=env_wait_ticks,
    openai_api_key=openai_api_key,
)

# start lifelong learning
voyager.learn(reset_env=False)
