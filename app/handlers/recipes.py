import logging, json, os

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from app.loader import dp, bot
from app.data.callbacks import base_cb
from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardMarkup)

import logging
import requests.exceptions
import urllib3.exceptions
from aiogram.utils import exceptions

from app.data.states import Menu