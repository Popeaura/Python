class SecretStash:
    def __init__(self):
        self._chocolates = 10 # private attribute

    def take_chocolate(self):
        if self._chocolates > 0:
            self._chocolates -= 1
            print("One chocolate taken !")
        else:
            print("No chocolates left")

Stash = SecretStash()
Stash.take_chocolate()