import src.keyboards as kb
from src.keyboards import builder

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile

import asyncio
import yt_dlp as ytd
import wget
import os
import shutil
import re

rt = Router()

YOUTUBELINK = r'^(https?\:\/\/)?(www\.youtube\.com|youtu\.be)\/.+$'


@rt.message(F.text)
async def getLink(message: Message):
    if re.match(YOUTUBELINK, message.text):
        global link
        link = message.text

        await message.answer(message.text, reply_markup=builder.adjust(3, 2).as_markup())
        await message.delete()
    else:
        await message.reply("Это не ссылка youtube")


@rt.callback_query(F.data == "720")
async def dw_720(callback: CallbackQuery):
    await callback.message.answer("Идёт установка")

    options = {
        'skip-download': True,
        'format_sort': ['res:720', 'ext:mp4:m4a'],
        'outtmpl': 'output/video/%(title)s.%(ext)s'
    }

    try:
        with ytd.YoutubeDL(options) as ytdl:
            ytdl.download([link])
            result = ytdl.extract_info("{}".format(link))
            name = result.get("title")
            title = ytdl.prepare_filename(result)
            video = open(f'{title}', 'rb')

        await callback.message.answer("Отправляю файл...")
        await callback.message.answer_video(FSInputFile(path=video.name), caption=name)

        folder = 'output/video/'

        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)

            except Exception as e:
                print('Error %s. Reason: %s' % (file_path, e))
    except:
        await callback.message.answer("Не удалось отправить файл")

        folder = 'output/video/'
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)

            except Exception as e:
                print('Error %s. Reason: %s' % (file_path, e))


@rt.callback_query(F.data == "360")
async def dw_360(callback: CallbackQuery):
    await callback.message.answer("Идёт установка")

    options = {
        'skip-download': True,
        'format_sort': ['res:360', 'ext:mp4:m4a'],
        'outtmpl': 'output/video/%(title)s.%(ext)s'
    }

    try:
        with ytd.YoutubeDL(options) as ytdl:
            ytdl.download([link])
            result = ytdl.extract_info("{}".format(link))
            name = result.get("title")
            title = ytdl.prepare_filename(result)
            video = open(f"{title}", 'rb')

        await callback.message.answer("Отправляю файл...")
        await callback.message.answer_video(FSInputFile(path=video.name), caption=name)

        folder = 'output/video/'

        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)

            except Exception as e:
                print('Error %s. Reason: %s' % (file_path, e))
    except:
        await callback.message.answer("Не удалось отправить файл")
        folder = 'output/video/'

        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)

            except Exception as e:
                print('Error %s. Reason: %s' % (file_path, e))


@rt.callback_query(F.data == "240")
async def dw_360(callback: CallbackQuery):
    await callback.message.answer("Идёт установка")

    options = {
        'skip-download': True,
        'format_sort': ['res:240', 'ext:mp4:m4a'],
        'outtmpl': 'output/video/%(title)s.%(ext)s'
    }

    try:
        with ytd.YoutubeDL(options) as ytdl:
            ytdl.download([link])
            result = ytdl.extract_info("{}".format(link))
            name = result.get("title")
            title = ytdl.prepare_filename(result)
            video = open(f"{title}", 'rb')

        await callback.message.answer("Отправляю файл...")
        await callback.message.answer_video(FSInputFile(path=video.name), caption=name)

        folder = 'output/video/'

        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)

            except Exception as e:
                print('Error %s. Reason: %s' % (file_path, e))
    except:
        await callback.message.answer("Не удалось отправить файл")
        folder = 'output/video/'

        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)

            except Exception as e:
                print('Error %s. Reason: %s' % (file_path, e))


@rt.callback_query(F.data == "144")
async def dw_360(callback: CallbackQuery):
    await callback.message.answer("Идёт установка")

    options = {
        'skip-download': True,
        'format_sort': ['res:144', 'ext:mp4:m4a'],
        'outtmpl': 'output/video/%(title)s.%(ext)s'
    }

    try:
        with ytd.YoutubeDL(options) as ytdl:
            ytdl.download([link])
            result = ytdl.extract_info("{}".format(link))
            name = result.get("title")
            title = ytdl.prepare_filename(result)
            video = open(f"{title}", 'rb')

        await callback.message.answer("Отправляю файл...")
        await callback.message.answer_video(FSInputFile(path=video.name), caption=name)

        folder = 'output/video/'

        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)

            except Exception as e:
                print('Error %s. Reason: %s' % (file_path, e))
    except:
        await callback.message.answer("Не удалось отправить файл")
        folder = 'output/video/'

        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)

            except Exception as e:
                print('Error %s. Reason: %s' % (file_path, e))


@rt.callback_query(F.data == "mp3")
async def dw_mp3(callback: CallbackQuery):
    await callback.message.answer("Идёт установка")

    options = {
        'skip-download': True,
        'format': 'bestaudio/best',
        'outtmpl': 'output/mp3/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:
        with ytd.YoutubeDL(options) as ytdl:
            ytdl.download([link])
            result = ytdl.extract_info("{}".format(link))
            name = result.get("title")
            title = ytdl.prepare_filename(result)
            clean_title = title.replace(".m4a", "")
            audio = open(f'{clean_title}.mp3', 'rb')

        await callback.message.answer("Отправляю файл...")
        await callback.message.answer_audio(FSInputFile(path=audio.name), caption=name)

        folder = 'output/mp3/'

        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)

            except Exception as e:
                print('Error %s. Reason: %s' % (file_path, e))
    except:
        await callback.message.answer("Не удалось отправить файл")
        folder = 'output/video/'

        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)

            except Exception as e:
                print('Error %s. Reason: %s' % (file_path, e))


@rt.callback_query(F.data == "jpg")
async def dw_jpg(callback: CallbackQuery):
    await callback.message.answer("Идёт установка")

    with ytd.YoutubeDL({}) as ytdl:
        info_dict = ytdl.extract_info(link, download=False)
        get_id = info_dict.get('id', None)

    thumbnail = f'https://img.youtube.com/vi/{get_id}/maxresdefault.jpg'

    wget.download(thumbnail, out="output/jpg/thumb.jpg")

    await callback.message.answer("Отправляю файл...")
    await callback.message.answer_document(FSInputFile(path="output/jpg/thumb.jpg"))

    folder = 'output/jpg/'

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

        except Exception as e:
            print('Error %s. Reason: %s' % (file_path, e))
