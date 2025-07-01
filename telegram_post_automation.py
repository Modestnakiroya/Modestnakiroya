import logging
import asyncio
from telegram import Bot, InputMediaPhoto, InputMediaVideo
from telegram.error import TelegramError
import os
from typing import List, Optional

class TelegramPoster:
    def __init__(self, bot_token: str):
       
        self.bot = Bot(token=bot_token)
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
    async def send_text_post(self, chat_id: str, text: str, disable_web_page_preview: bool = False) -> bool:
    
        try:
            await self.bot.send_message(
                chat_id=chat_id,
                text=text,
                disable_web_page_preview=disable_web_page_preview
            )
            self.logger.info(f"Text post sent to {chat_id}")
            return True
        except TelegramError as e:
            self.logger.error(f"Failed to send text post: {e}")
            return False
            
    async def send_media_post(
        self,
        chat_id: str,
        media_paths: List[str],
        caption: Optional[str] = None,
        is_video: bool = False
    ) -> bool:
       
        if not media_paths:
            self.logger.error("No media files provided")
            return False
            
        try:
            media = []
            for i, path in enumerate(media_paths):
                if not os.path.exists(path):
                    self.logger.error(f"File not found: {path}")
                    return False
                    
                if is_video:
                    media_item = InputMediaVideo(media=open(path, 'rb'))
                else:
                    media_item = InputMediaPhoto(media=open(path, 'rb'))
                    
                # Only add caption to the first media item
                if i == 0 and caption:
                    media_item.caption = caption
                    
                media.append(media_item)
                
            if len(media) == 1:
                # Single media
                if is_video:
                    await self.bot.send_video(chat_id=chat_id, video=media[0].media, caption=media[0].caption)
                else:
                    await self.bot.send_photo(chat_id=chat_id, photo=media[0].media, caption=media[0].caption)
            else:
                # Media group
                await self.bot.send_media_group(chat_id=chat_id, media=media)
                
            self.logger.info(f"Media post sent to {chat_id}")
            return True
            
        except TelegramError as e:
            self.logger.error(f"Failed to send media post: {e}")
            return False
        except Exception as e:
            self.logger.error(f"Unexpected error: {e}")
            return False
            
    async def send_poll(
        self,
        chat_id: str,
        question: str,
        options: List[str],
        is_anonymous: bool = True,
        allows_multiple_answers: bool = False
    ) -> bool:
        
        if len(options) < 2 or len(options) > 10:
            self.logger.error("Poll must have between 2 and 10 options")
            return False
            
        try:
            await self.bot.send_poll(
                chat_id=chat_id,
                question=question,
                options=options,
                is_anonymous=is_anonymous,
                allows_multiple_answers=allows_multiple_answers
            )
            self.logger.info(f"Poll sent to {chat_id}")
            return True
        except TelegramError as e:
            self.logger.error(f"Failed to send poll: {e}")
            return False

async def main():
    BOT_TOKEN = "7537306019:AAEjGr9-Egskiz9mjDW335HQa7pYRF0nG-w"
    CHAT_ID = "-1002465354086" 
    
    poster = TelegramPoster(BOT_TOKEN)
    
    # Example 1: Send text post
    await poster.send_text_post(
        chat_id=CHAT_ID,
        text="Hello from my automated Telegram poster! 🚀\n\nCheck out our website: example.com",
        disable_web_page_preview=False
    )
    # Example 2: Send poll
    await poster.send_poll(
        chat_id=CHAT_ID,
        question="What's your favorite programming language?",
        options=["Python", "JavaScript", "Java", "C++", "Other"],
        is_anonymous=True,
        allows_multiple_answers=False
    )

if __name__ == "__main__":
    asyncio.run(main())