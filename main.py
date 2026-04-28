import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from llm import get_llm
from chroma import index_documents, query_documents
from memory import DialogManager

load_dotenv()

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Глобальные объекты (инициализируются при старте)
llm = None
dialog_manager = DialogManager()

# Базовый системный промпт
SYSTEM_PROMPT = (
"You are a web accessibility consultant. Answer questions using the provided context, if any. If the context doesn't provide an answer, use your own knowledge. Give the user an answer in his language"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    user_id = str(update.effective_user.id)
    # Создаём сессию, если её нет
    if not dialog_manager.session_exists(user_id):
        dialog_manager.create_session(user_id)
        await update.message.reply_text(
            "👋Hi! I'm a web accessibility consultant. Ask your question.\n"
            "For a new conversation, use /new"
        )
    else:
        await update.message.reply_text("Welcome back!")

async def new_dialog(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /new – сброс истории"""
    user_id = str(update.effective_user.id)
    # Удаляем старую сессию, если была
    dialog_manager.delete_session(user_id)
    dialog_manager.create_session(user_id)
    await update.message.reply_text("🆕 New dialog is started.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик текстовых сообщений"""
    user_id = str(update.effective_user.id)
    user_input = update.message.text.strip()
    
    # Гарантируем существование сессии (на случай если бот перезапущен, а пользователь уже был)
    if not dialog_manager.session_exists(user_id):
        dialog_manager.create_session(user_id)

    # 1. Поиск контекста в Chroma
    try:
        context_docs = query_documents(user_input)
        context_text = "\n\n".join(context_docs) if context_docs else ""
    except Exception as e:
        logger.error(f"Chroma search error: {e}")
        context_text = ""

    # 2. Формируем сообщение пользователя с возможным контекстом
    if context_text:
        human_message = f"Context:\n{context_text}\n\nQuestion: {user_input}"
    else:
        human_message = user_input

    # 3. Добавляем сообщение пользователя в историю
    dialog_manager.add_message(user_id, "human", human_message)

    # 4. Собираем все сообщения для LLM
    history = dialog_manager.get_history(user_id)
    messages = [("system", SYSTEM_PROMPT)] + history

    # 5. Отправляем запрос в LLM
    try:
        response = llm.invoke(messages)
        answer = response.content
    except Exception as e:
        logger.error(f"LLM responce error: {e}")
        answer = "⚠️ Произошла ошибка при обработке запроса. Попробуйте позже."

    # 6. Сохраняем ответ в историю и отправляем пользователю
    dialog_manager.add_message(user_id, "ai", answer)
    await update.message.reply_text(answer)

def main():
    """Запуск Telegram-бота"""
    # Индексация документов при старте
    logger.info("Индексация документов...")
    cnt = index_documents()
    logger.info(f"Проиндексировано файлов: {cnt}" if cnt else "Папка с документами пуста или не найдена.")

    # Инициализация LLM
    global llm
    llm = get_llm()

    # Создаём Application
    tg_token = os.getenv("TG_API_KEY")
    if not tg_token:
        raise EnvironmentError("Не задан TG_API_KEY в .env")
    app = Application.builder().token(tg_token).build()

    # Регистрируем обработчики
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("new", new_dialog))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запускаем бота
    logger.info("Бот запущен. Ожидаем сообщений...")
    app.run_polling()

if __name__ == "__main__":
    main()