
class ListManager:
    data = []

    def __init__(self):
        self.data = []

    def print_list(self, **kw_args):
        print(self.data)

    def insert(self, **kw_args):
        args = kw_args.get('args')
        if len(args) != 2:
            print(f'expected 2 arguments but received {args}')
            return
        insert_at = int(args[0])
        value = int(args[1])
        self.data.insert(insert_at, value)
    
    def remove(self, **kw_args):
        args = kw_args.get('args')
        if len(args) != 1:
            print(f'expected 1 arguments but received {args}')
            return
        remove_at = int(args[0])
        self.data.remove(remove_at)

    def append(self, **kw_args):
        args = kw_args.get('args')
        if len(args) != 1:
            print(f'expected 1 arguments but received {args}')
            return
        value = int(args[0])
        self.data.append(value)

    def sort(self, **kw_args):
        self.data.sort()

    def pop(self, **kw_args):
        self.data.pop()

    def reverse(self, **kw_args):
        self.data.reverse()

    def execute(self, command, args):
        # print(f'command: {command} {args}')
        commands = {
            'print': self.print_list,
            'insert': self.insert,
            'remove': self.remove,
            'append': self.append,
            'sort': self.sort,
            'pop': self.pop,
            'reverse': self.reverse
        }

        commands.get(command, lambda **kw_args: print(f'command "{command}" not found'))(command=command, args=args)

if __name__ == '__main__':
    n = int(input())
    lst_manager = ListManager()
    while True:
        try:
            command, *args = input().split()
            if not command:
                break
            lst_manager.execute(command, args)
        except EOFError as error:
            break