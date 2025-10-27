with open('./sql_commands/state_codes.txt') as f:
    for line in f:
        n, *_ = line.split()
        print(f'({n}, \'{" ".join(_)}\'),')

    """for line in f:
        n, *_ = line.split()
        print(n, len(" ".join(_)))"""
