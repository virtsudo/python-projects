from aiogram import Bot, Dispatcher, F, Router
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, Message, BotCommand
from aiogram.fsm.state import StatesGroup, State, default_state
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.strategy import FSMStrategy
from app.handler import common
from app.handler import game

from os import environ

BOT_TOKEN = environ['BOT_TOKEN']
