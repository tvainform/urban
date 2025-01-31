# Задача "Найдёт везде":
import re

class WordsFinder:
    def __init__(self, *names):
        self.file_names = list(names)

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.replace(' - ', ' ')
                    line = re.sub('[,.!?=;:]', '', line)
                    words.extend(line.lower().split())
            all_words[name] = words
        return all_words

    def find(self, word):
        result = {}
        for key, value in self.get_all_words().items():
             if word.lower() in value:
                result[key] = value.index(word.lower()) + 1
                result.update()
             else:
                continue
        return result

    def count(self, word):
        result = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                result[key] = value.count(word.lower())
                result.update()
            else:
                continue
        return result




finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего