import random


class CharacterRandomize:
    def generate_random_id(self):
        return random.randint(1, 826)

    def generate_random_page(self):
        return random.randint(2, 41)

    def generate_random_multiple_ids(self):
        multiple_ids = []
        for _ in range(1, random.randint(2, 826)):
            multiple_ids.append(random.randint(1, 826))
        return sorted(list(set(multiple_ids)))


class LocationRandomize:
    def generate_random_id(self):
        return random.randint(1, 126)

    def generate_random_page(self):
        return random.randint(2, 7)

    def generate_random_multiple_ids(self):
        multiple_ids = []
        for _ in range(1, random.randint(2, 126)):
            multiple_ids.append(random.randint(1, 126))
        return sorted(list(set(multiple_ids)))
