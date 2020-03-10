

def some_function():
    print('boom')

    import pudb; pu.db  # breakpoint actually

    print('boom')


if __name__ == '__main__':
    some_function()
