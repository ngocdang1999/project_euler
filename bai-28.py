def p28(size):
    return 1 if size == 1 else p28(size-2) + 4*size*size - 6*(size-1)


def main(argv):
    try:
        size = int(argv[1])
    except Exception:
        usage()
        return 1
    if size < 1 or size % 2 == 0:
        usage()
        return 1
    print p28(size)
