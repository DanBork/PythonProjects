class UppercaseDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        if isinstance(result, str):     # if result is string, change letters to uppercase
            return result.upper()
        return result       # else return result, without changing anything


@UppercaseDecorator
def read_message():
    with open("message.txt", 'r') as file:
        return file.read()


print(read_message())
