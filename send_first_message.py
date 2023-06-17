import asyncio
import telegram

async def main():
    bot = telegram.Bot(token='6086120952:AAGoSxTW6iFidtqa_-SaP6I8TTZ-aFXN-6A')
    async with bot:
        # get_me = await bot.get_me()
        get_update = (await bot.getUpdates())[0]
        chat_id = get_update.message.from_user.id
        first_name = get_update.message.from_user.first_name
        print(chat_id)
        await bot.send_message(chat_id=chat_id, text=f'Hello {first_name}!') 

        
    
if __name__ == '__main__':
    asyncio.run(main())
    