def song():
    print('line 1')
    yield "I'm a lumberjack and I'm OK"
    print('line 2')
    yield 'I sleep all night and I work all day'


lines = song()
print(lines)
print(next(lines))
print(next(lines))
print(next(lines))


