from abc import ABC, abstractmethod


class DuplicateKeyError(Exception):
    pass


class AudioPrintsDB(ABC):

    @abstractmethod
    def insert_one_fingerprint(self, fingerprint):
        pass

    @abstractmethod
    def insert_many_fingerprints(self, fingerprints):
        pass

    @abstractmethod
    def find_one_song(self, song):
        pass

    @abstractmethod
    def get_next_song_id(self):
        pass

    @abstractmethod
    def insert_one_song(self, song):
        pass

    @abstractmethod
    def find_db_fingerprints_with_hash_key(self, fingerprint):
        pass

    @abstractmethod
    def get_db_fingerprint_song_id(self, fingerprint):
        pass

    @abstractmethod
    def get_db_fingerprint_offset(self, fingerprint):
        pass
