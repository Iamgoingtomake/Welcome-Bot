from telegram import Update
from telegram.ext import Updater , CommandHandler, CallbackQueryHandler, CallbackContext,Filters,MessageHandler
import os

Token =os.environ.get("MT_BOT_TOKEN",None)
updater = Updater( Token ,use_context = True )

def start(updater,context):
 updater.message.reply_text('''ðHi Bro or Sis Iam Welcome Messanger bot\n\nð¤Any Doubt - @Hyetelgram_Bots_Group\nðBot Updates - @HyetelegramBots\n\nð®More Details Clcik /help Button''')

def help(updater,context):
 updater.message.reply_text("ðEnglishð\n\nâï¸Add ME TO YOUR GROUP\nâï¸MAKE ME AS ADMIN ON GROUP\n\nðMalayalamð\n\nâï¸à´à´¦àµà´¯à´ à´à´¨àµà´¨àµ à´¨à´¿à´àµà´à´³àµà´àµ à´àµà´°àµà´ªàµà´ªà´¿àµ½ à´à´¡àµ à´à´àµ\nâï¸à´à´¨àµà´¨àµ à´¨à´¿à´à´³àµà´àµ à´àµà´°àµà´ªàµà´ªà´¿àµ½ à´à´¡àµà´®à´¿àµ» à´à´àµ\n\nð¥ï¸Updates Channelð¥ï¸@HyetelegramBots")
 

def add_group(update: Update, context: CallbackContext):
    for member in update.message.new_chat_members:
        update.message.reply_text(f'â¯ââââãâ­ï¸âï¸M-D-Uâï¸â­ï¸  ãâââââ® 

âï¸âï¸âï¸âï¸âï¸âï¸âï¸âï¸âï¸âï¸âï¸âï¸âï¸

á¼EY I'M áªá´á©áªá­OOáªðð»ð {member.full_name} , á¯á´áªáOá°á´ TO "á°-áª-á"ð½

ðððâ ððâ ðð½ð½ðâðð¸ð ââð¸ââð¼ðð ð»ð½

âð¿ð²ð·ð°ð½ð½ð´ð»'ð- @DC_MARVEL_UPDATES

-[]

âð¿ð²ð·ð°ð½ð½ð´ð»'ð-@DC_MARVEL_COMICSS

-[]

âð¿ð²ð·ð°ð½ð½ð´ð»'ð- @CinemaArcade\n\n')

add_group_handle = MessageHandler(Filters.status_update.new_chat_members, add_group)
updater.dispatcher.add_handler(add_group_handle)

dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(CommandHandler('help',help))

updater.start_polling()
updater.idle()
