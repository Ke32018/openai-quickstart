from mygpt.MyTools import Tools
from mygpt.MyVectorstor import VectorStore

from langchain_experimental.autonomous_agents import AutoGPT
from langchain.chat_models import ChatOpenAI

class MyAutoGPT:
    def __init__(self):

        self.tools = Tools().tools
        self.vectorstore = VectorStore().vectorstore
        self.agent = AutoGPT.from_llm_and_tools(
                        ai_name="Jarvis",
                        ai_role="Assistant",
                        tools=self.tools,
                        llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, verbose=True),
                        memory=self.vectorstore.as_retriever(
                            search_type="similarity_score_threshold",
                            search_kwargs={"score_threshold": 0.8})
                    )

    def add_tool(self, tool):
        self.tools.add_tool(tool)


    def run(self, prompt: str):
        self.agent.run(prompt)