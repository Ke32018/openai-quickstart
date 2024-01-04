from mygpt import MyAutoGPT

import gradio as gr
import time

def initialize_autogpt():
    global myAutoGPT
    myAutoGPT = MyAutoGPT()

def gpt_run(prompt) -> str:    
    return myAutoGPT.run(prompt)

def predict(prompt):
    gpt_response = myAutoGPT.run(prompt)
    return gpt_response

    

if __name__ == "__main__":
    # 初始化 translator
    initialize_autogpt()
    # 启动 Gradio 服务
    with gr.Blocks() as demo:
        chatbot = gr.Chatbot()
        msg = gr.Textbox()
        clear = gr.ClearButton([msg, chatbot])

        def respond(message, chat_history):
            bot_message = predict(message)
            chat_history.append((message, bot_message))
            return "", chat_history

        msg.submit(respond, [msg, chatbot], [msg, chatbot])
    demo.launch()