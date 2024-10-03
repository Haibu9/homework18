import module_3_4
from time import sleep

class UrTube:

    users = []
    videos = []

    def __init__(self, current_user = None):
        self.current_user = current_user


    def log_in(self, nickname, password):
        for u in UrTube.users:
            if u.nickname == nickname and u.password == hash(password):
                self.current_user = u

    def register(self, nickname, password, age):
        prov = False
        for u in UrTube.users:
            if u.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                prov = True
                break
        if prov == 0:
            nickname = User(nickname, password, age)
            self.current_user = nickname

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            prov = False
            for vi in self.videos:
                if vi.title == i.title:
                    prov = True
                    break
            if prov == 0:
                self.videos.append(i)

    def get_videos(self, word):
        vids = []
        for v in self.videos:
            vids.append(v.title)
        x = module_3_4.single_root_words(word, *vids)
        return x

    def watch_video(self, title):
        if self.current_user == None:
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            vids = []
            watch = False
            for v in self.videos:
                vids.append(v.title)
                if v.title == title:
                    watch = True
                    break
            if watch == 1:
                Tvideo = self.videos[len(vids) - 1]
                if self.current_user.age < 18 and Tvideo.adult_mode == True:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:
                    while Tvideo.time_now < Tvideo.duration:
                        Tvideo.time_now += 1
                        print(Tvideo.time_now, end=' ')
                        sleep(1)
                    print("Конец видео")

class User:

    def __init__(self, nickname, password, age):

        self.nickname = nickname
        self.password = hash(password)
        self.age = age

        UrTube.users.append(self)

    def __str__(self):
        return self.nickname

class Video:

    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
