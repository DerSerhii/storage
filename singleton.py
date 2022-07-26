class Singleton:
    __instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __del__(self):
        Singleton.__instance = None

    def __call__(self, *args, **kwargs):
        # надо переопределить
        pass

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


pt1 = Singleton(100, 2)
pt2 = Singleton(300, 2)

print()
print(f"pt1: {pt1.__dict__}")
print(f"pt2: {pt2.__dict__}")

print()
print(f"id pt1: {id(pt1)}")
print(f"id pt2: {id(pt2)}")
