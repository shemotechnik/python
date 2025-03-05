# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 13:00:26 2025

@author: nurul
В проекте мы работаем с медиа-файлами (аудио, видео, фото).
Есть некоторый общий набор данных о файле, необходимый для реализации бизнес-логики (имя, размер, дата создания, владелец...).
Для каждого типа медиа-файлов есть свой набор метаданных.
Попробуйте написать классы для работы с медиа-файлами (они будут основой для пользовательского кода остальных команд).
Приведите примеры кода, как можно создать, обновить, удалить или провести какое-нибудь действие (конвертация, извлечение фич) над файлом (можно без реализации деталей).
*Попробуйте дописать классы для работы с файлами, расположенными не на локальном диске (облако, удаленный сервер, s3-like storage).
Попробуйте ответить на вопросы: много ли кода придется дописать / переписать при добавлении новых типов файлов и способов их хранения?
!Суть задания — именно проектирование классовой иерархии, а не реализация самой логики, поэтому достаточно, например, просто объявить метод .save(...) и в комментарии уточнить, что он должен делать, без конкретной реализации.
"""
import datetime

class Mp3AudioFiles():
    def __init__(self, name, path, type_of_load, file_postfix):
        self.name = name
        self.path = path
        self.type_of_load = type_of_load
        self.file_postfix = file_postfix
    
    def load(self):
        print(f'Загрузил {self.file_postfix} файл')
    
    def create(self):
        print(f'Создал {self.file_postfix} файл')
    
    def change(self):
        print(f'Изменил {self.file_postfix} файл')
    
    def delete(self):
        print(f'Удалил {self.file_postfix} файл')
        
class JpgMediaFiles():
    def __init__(self, name, path, type_of_load, file_postfix):
        self.name = name
        self.path = path
        self.type_of_load = type_of_load
        self.file_postfix = file_postfix
    
    def load(self):
        print(f'Загрузил {self.file_postfix} файл')
    
    def create(self):
        print(f'Создал {self.file_postfix} файл')
    
    def change(self):
        print(f'Изменил {self.file_postfix} файл')
    
    def delete(self):
        print(f'Удалил {self.file_postfix} файл')
        
class BmpMediaFiles():
    def __init__(self, name, path, type_of_load, file_postfix):
        self.name = name
        self.path = path
        self.type_of_load = type_of_load
        self.file_postfix = file_postfix
    
    def load(self):
        print(f'Загрузил {self.file_postfix} файл')
    
    def create(self):
        print(f'Создал {self.file_postfix} файл')
    
    def change(self):
        print(f'Изменил {self.file_postfix} файл')
    
    def delete(self):
        print(f'Удалил {self.file_postfix} файл')
        
class AviVideoFiles():
    def __init__(self, name, path, type_of_load, file_postfix):
        self.name = name
        self.path = path
        self.type_of_load = type_of_load
        self.file_postfix = file_postfix
    
    def load(self):
        print(f'Загрузил {self.file_postfix} файл')
    
    def create(self):
        print(f'Создал {self.file_postfix} файл')
    
    def change(self):
        print(f'Изменил {self.file_postfix} файл')
    
    def delete(self):
        print(f'Удалил {self.file_postfix} файл')
        

class LocalFilesMethods():
    def __init__(self, name, path, type_of_load, file_postfix):
        self.name = name
        self.path = path
        self.type_of_load = type_of_load
        self.file_postfix = file_postfix
        self.parent_class = None
        
        print("Инициирую класс LocalFilesMethods для работы с", file_postfix)
        
        if self.file_postfix == "mp3":self.parent_class = Mp3AudioFiles(self.name, self.path, self.type_of_load, self.file_postfix)
        if self.file_postfix == "jpg":self.parent_class = JpgMediaFiles(self.name, self.path, self.type_of_load, self.file_postfix)
        if self.file_postfix == "bmp":self.parent_class = BmpMediaFiles(self.name, self.path, self.type_of_load, self.file_postfix)
        if self.file_postfix == "avi":self.parent_class = AviVideoFiles(self.name, self.path, self.type_of_load, self.file_postfix)
        
    def load(self):
        print("Загружаю. Локальное хранилище.")
        self.parent_class.load()
        
    def create(self):
        print("Создаю. Локальное хранилище.")
        self.parent_class.create()
    
    def change(self):
        print("Изменяю. Локальное хранилище.")
        self.parent_class.change()
    
    def delete(self):
        print("Удаляю. Локальное хранилище.")
        self.parent_class.delete()

class CloudFilesMethods():
    def __init__(self, name, path, type_of_load, file_postfix):
        self.name = name
        self.path = path
        self.type_of_load = type_of_load
        self.file_postfix = file_postfix
        self.parent_class = None
        
        print("Инициирую класс CloudFilesMethods для работы с", file_postfix)
        
        if self.file_postfix == "mp3":self.parent_class = Mp3AudioFiles(self.name, self.path, self.type_of_load, self.file_postfix)
        if self.file_postfix == "jpg":self.parent_class = JpgMediaFiles(self.name, self.path, self.type_of_load, self.file_postfix)
        if self.file_postfix == "bmp":self.parent_class = BmpMediaFiles(self.name, self.path, self.type_of_load, self.file_postfix)
        if self.file_postfix == "avi":self.parent_class = AviVideoFiles(self.name, self.path, self.type_of_load, self.file_postfix)
        
    def load(self):
        print("Загружаю. Облако.")
        self.parent_class.load()
        
    def create(self):
        print("Создаю. Облако.")
        self.parent_class.create()
    
    def change(self):
        print("Изменяю. Облако.")
        self.parent_class.change()
    
    def delete(self):
        print("Удаляю. Облако.")
        self.parent_class.delete()
        
class S3FilesMethods():
    def __init__(self, name, path, type_of_load, file_postfix):
        self.name = name
        self.path = path
        self.type_of_load = type_of_load
        self.file_postfix = file_postfix
        self.parent_class = None
        
        print("Инициирую класс S3FilesMethods для работы с", file_postfix)
        
        if self.file_postfix == "mp3":self.parent_class = Mp3AudioFiles(self.name, self.path, self.type_of_load, self.file_postfix)
        if self.file_postfix == "jpg":self.parent_class = JpgMediaFiles(self.name, self.path, self.type_of_load, self.file_postfix)
        if self.file_postfix == "bmp":self.parent_class = BmpMediaFiles(self.name, self.path, self.type_of_load, self.file_postfix)
        if self.file_postfix == "avi":self.parent_class = AviVideoFiles(self.name, self.path, self.type_of_load, self.file_postfix)
        
    def load(self):
        print("Загружаю. S3.")
        self.parent_class.load()
        
    def create(self):
        print("Создаю. S3.")
        self.parent_class.create()
    
    def change(self):
        print("Изменяю. S3.")
        self.parent_class.change()
    
    def delete(self):
        print("Удаляю. S3.")
        self.parent_class.delete()

class LoadFileByType():
    
    def __init__(self, name, path, type_of_load, file_postfix):
        self.type_of_load = type_of_load
        self.name = name
        self.path = path
        self.file_postfix = file_postfix
        self.type_of_load = type_of_load
        
    def load(self):
        if self.type_of_load == "local":return LocalFilesMethods(self.name, self.path, self.type_of_load, self.file_postfix).load()
        if self.type_of_load == "url":return CloudFilesMethods(self.name, self.path, self.type_of_load, self.file_postfix).load()
        if self.type_of_load == "s3":return S3FilesMethods(self.name, self.path, self.type_of_load, self.file_postfix).load()
    
    def create(self):
        if self.type_of_load == "local":return LocalFilesMethods(self.name, self.path, self.type_of_load, self.file_postfix).create()
        if self.type_of_load == "url":return CloudFilesMethods(self.name, self.path, self.type_of_load, self.file_postfix).create()
        if self.type_of_load == "s3":return S3FilesMethods(self.name, self.path, self.type_of_load, self.file_postfix).create()
    
    def change(self):
        if self.type_of_load == "local":return LocalFilesMethods(self.name, self.path, self.type_of_load, self.file_postfix).change()
        if self.type_of_load == "url":return CloudFilesMethods(self.name, self.path, self.type_of_load, self.file_postfix).change()
        if self.type_of_load == "s3":return S3FilesMethods(self.name, self.path, self.type_of_load, self.file_postfix).change()
    
    def delete(self):
        if self.type_of_load == "local":return LocalFilesMethods(self.name, self.path, self.type_of_load, self.file_postfix).delete()
        if self.type_of_load == "url":return CloudFilesMethods(self.name, self.path, self.type_of_load, self.file_postfix).delete()
        if self.type_of_load == "s3":return S3FilesMethods(self.name, self.path, self.type_of_load, self.file_postfix).delete()

class File():
    def __init__(self, name, size, author, path, type_of_load):
        self.name = name
        self.date_create = datetime.datetime.now()
        self.size = size
        self.author = author
        self.path = path
        self.type_of_load = type_of_load
    
    def load(self):
        print("Загружаем файл")
        return LoadFileByType(self.name, self.path, self.type_of_load, self.name.split(".")[1]).load()
    
    def create(self):
        print("СОздаем файл")
        return LoadFileByType(self.name, self.path, self.type_of_load, self.name.split(".")[1]).create()
    
    def change(self):
        print("Меняем файл")
        return LoadFileByType(self.name, self.path, self.type_of_load, self.name.split(".")[1]).change()
    
    def delete(self):
        print("Удаляем файл")
        return LoadFileByType(self.name, self.path, self.type_of_load, self.name.split(".")[1]).delete()
    
    
    

print("Начало")
mp3_file = File("alice.mp3", 15, "Metallica", "C:/asda/asda/asdas", "local")
mp3_file.load()
mp3_file = File("capture.jpg", 20, "Johny", "/asd/asd/asd", "url")
mp3_file.change()
mp3_file = File("video.avi", 2000000, "Alex", "s3://asdsad/asdasd/asdasd", "s3")
mp3_file.delete()
"""
Чтобы добавить новый способ работы с файлом, надо добавить класс, например FTPFilesMethods и там прописать методы create, load, change, delete
и вызвать FTPFilesMethods в LoadFileByType
Чтобы добавить еще один тип файла надо добавить класс, например PNGMediaFilesи вызвать его во всех классов по работе с файлами вроде LocalFilesMethods и CloudFilesMethods
"""