import sys
import os
import gradio as gr

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import ArgumentParser, LOG
from translator import PDFTranslator, TranslationConfig


def translation(input_file, source_language, target_language, style):
    LOG.debug(f"[翻译任务]\n源文件: {input_file.name}\n源语言: {source_language}\n目标语言: {target_language}")

    output_file_path = Translator.translate_pdf(
        input_file.name, source_language=source_language, target_language=target_language, style=style)

    return output_file_path

def launch_gradio():

    iface = gr.Interface(
        fn=translation,
        title="OpenAI-Translator v2.0(PDF 电子书翻译工具)",
        inputs=[
            gr.File(label="上传PDF文件"),
            gr.Textbox(label="源语言（默认：英文）", placeholder="English", value="English"),
            gr.Textbox(label="目标语言（默认：中文）", placeholder="Chinese", value="Chinese"),
            gr.Textbox(label="风格", placeholder="""输入你希望生成文字的翻译风格(以下是一些示例)
# 诗歌 - Poetic Translation
# 戏剧化 - Dramatic Translation
# 小说 - Novelistic Translation
# 新闻稿 - Press Release Translation
# 法律文件 - Legal Document Translation
# 广告营销 - Advertising & Marketing Translation
                       """, value="normal")
        ],
        outputs=[
            gr.File(label="下载翻译文件")
        ],
        allow_flagging="never"
    )

    iface.launch(share=True, server_name="127.0.0.1")

def initialize_translator():
    # 解析命令行
    argument_parser = ArgumentParser()
    args = argument_parser.parse_arguments()

    # 初始化配置单例
    config = TranslationConfig()
    config.initialize(args)    
    # 实例化 PDFTranslator 类，并调用 translate_pdf() 方法
    global Translator
    Translator = PDFTranslator(config.model_name)


if __name__ == "__main__":
    # 初始化 translator
    initialize_translator()
    # 启动 Gradio 服务
    launch_gradio()
