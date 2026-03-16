from abc import ABC, abstractmethod
from typing import AsyncGenerator
import openai
import anthropic
import google.generativeai as genai
from config import settings

class AIProvider(ABC):
    @abstractmethod
    async def generate_stream(self, prompt: str) -> AsyncGenerator[str, None]:
        pass

class OpenAIProvider(AIProvider):
    def __init__(self):
        self.client = openai.AsyncOpenAI(api_key=settings.openai_api_key)
    
    async def generate_stream(self, prompt: str) -> AsyncGenerator[str, None]:
        stream = await self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[{"role": "user", "content": prompt}],
            stream=True
        )
        async for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content

class AnthropicProvider(AIProvider):
    def __init__(self):
        self.client = anthropic.AsyncAnthropic(api_key=settings.anthropic_api_key)
    
    async def generate_stream(self, prompt: str) -> AsyncGenerator[str, None]:
        async with self.client.messages.stream(
            model="claude-3-opus-20240229",
            max_tokens=4096,
            messages=[{"role": "user", "content": prompt}]
        ) as stream:
            async for text in stream.text_stream:
                yield text

class GeminiProvider(AIProvider):
    def __init__(self):
        genai.configure(api_key=settings.gemini_api_key)
        self.model = genai.GenerativeModel('gemini-pro')
    
    async def generate_stream(self, prompt: str) -> AsyncGenerator[str, None]:
        response = await self.model.generate_content_async(prompt, stream=True)
        async for chunk in response:
            if chunk.text:
                yield chunk.text

class AIService:
    def __init__(self, provider: str = None):
        provider = provider or settings.default_ai_provider
        
        if provider == "openai":
            self.provider = OpenAIProvider()
        elif provider == "anthropic":
            self.provider = AnthropicProvider()
        elif provider == "gemini":
            self.provider = GeminiProvider()
        else:
            raise ValueError(f"Unknown provider: {provider}")
    
    async def generate_chapter(self, novel_info: dict, chapter_num: int) -> AsyncGenerator[str, None]:
        prompt = f"""请为以下小说生成第{chapter_num}章内容：

标题：{novel_info['title']}
题材：{novel_info['genre']}
风格：{novel_info.get('style', '自然流畅')}
大纲：{novel_info['outline']}

要求：
1. 章节长度约2000-3000字
2. 情节连贯，符合大纲设定
3. 语言生动，符合指定风格
4. 直接输出章节内容，不要额外说明

第{chapter_num}章："""
        
        async for chunk in self.provider.generate_stream(prompt):
            yield chunk
