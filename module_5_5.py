from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __repr__(self):
        return self.nickname

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        if isinstance(other.password, str) and isinstance(other, User):
            return hash(self.password) == hash(other.password)
        return False

    def __lt__(self, other):
        if isinstance(other, int):
            return self.age < other
        return False

class Video:
    time_now = 0
    def __init__(self, *args, **kwargs):
        self.title = args[0]
        self.duration = args[1]
        self.adult_mode = kwargs.get('adult_mode')

    def __eq__(self, other):
        if isinstance(other.title, str) and isinstance(other, Video):
            return self.title.lower() == other.title.lower()
        return False

    def __contains__(self, other):
        if isinstance(other.title, str) and isinstance(other, Video):
            return other.title.lower() in self.title.lower()
        return False

class UrTube:
    users = []
    videos = []
    current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == password:
                self.current_user = user

    def register(self, nickname, password, age):
        checker = False
        for item in self.users:
            checker = nickname == item.nickname
            break

        if checker:
            print(f"Пользователь {nickname} уже существует")
        else:
            self.users.append(User(nickname, password, age))
            self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            if i not in self.videos:
                self.videos.append(i)

    def get_videos(self, string):
        _list = []
        for video in self.videos:
            if Video(string, 0) in video:
                _list.append(video.title)
        return _list

    def watch_video(self, name):
        if self.current_user is not None:
            if self.current_user < 18:
                print("Вам нет 18 лет, пожалуйста покиньте страницу")
            else:
                for i in self.videos:
                    if name == i.title:
                        while i.time_now < i.duration:
                            i.time_now += 1
                            print(i.time_now, end=' ')
                            sleep(1)
                        print('Конец видео')
                        break
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")


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