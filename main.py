from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api.provider import ProviderRequest
from astrbot.api import logger

@register("watchcontext", "Muzimi111", "用于观察每次对话传给大模型的提示词", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    

    @filter.on_llm_response()
    async def debug_llm_context(self, event: AstrMessageEvent, req: ProviderRequest):
        """这是一个全局钩子函数，可以在这里观察每次对话传给大模型的提示词（Prompt）和系统提示词（System Prompt）。"""
        logger.info("🔍 [观察插件] 捕获到一次 LLM 请求！")
        logger.info(f"🔵 【历史对话记录 (Contexts)】:\n{req.contexts}")
        logger.info(f"🔴 【当前用户输入 (叠加了旁白)】:\n{req.prompt}")
        logger.info(f"🟢 【系统人设】:\n{req.system_prompt}")