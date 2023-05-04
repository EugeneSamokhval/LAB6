from random import shuffle
import copy


class KeyContent:
    def __init__(self, key, content):
        self.key = key
        self.content = content

    def get_content(self):
        return self.content

    def get_key(self):
        return self.key


class HashRealisation:
    max_size = 256

    def hash_function(self, key):
        current_hash = len(key) % self.max_size
        for letter in key:
            current_hash = self.table_of_shuffles[(current_hash+ord(letter))%self.max_size]
        return current_hash

    def __init__(self, elements, content, max_size=256):
        self.max_size = max_size
        self.table_of_shuffles = [number for number in range(0, 256)]
        shuffle(self.table_of_shuffles)
        self.table_of_content = []
        temp_elements_content_connection = [[elements[index], content[index]] for index in range(len(elements))]
        for index in range(self.max_size):
            self.table_of_content.append([])
        for connected in temp_elements_content_connection:
            self.table_of_content[self.hash_function(connected[0])].append(KeyContent(connected[0], connected[1]))

    def get(self, key):
        hased = self.hash_function(key)
        if len(self.table_of_content[hased]) == 0:
            return None
        elif len(self.table_of_content[hased]) == 1:
            return self.table_of_content[hased][0].get_content()
        else:
            for pair in self.table_of_content[hased]:
                if pair.get_key() == key:
                    return pair.get_content()
            return None

    def add(self, key, content):
        hashed = self.hash_function(key)
        if len(self.table_of_content[hashed]) == 0:
            self.table_of_content[hashed].append(KeyContent(key, content))
        else:
            self.table_of_content[hashed].append(KeyContent(key, content))

    def remove(self, key):
        hashed = self.hash_function(key)
        if len(self.table_of_content[hashed]) == 0:
            return None
        else:
            for pair in self.table_of_content[hashed]:
                if pair.get_key() == key:
                    pair_copy = copy.deepcopy(pair)
                    self.table_of_content[hashed].remove(pair)
                    return pair_copy
            return None

