from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# Import the openai api key
config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")

#create assistant agent
assitant = AssistantAgent(name = "assistant", llm_config= { "config_list" : config_list})

#create user proxy agent
user_proxy = UserProxyAgent(
    name = "user_proxy",
    code_execution_config={"work_dir" : "coding"}
)

#start conversation
user_proxy.initiate_chat(assitant, message = "Plot a chart of NVDA and TESLA stock price change YTD.")



