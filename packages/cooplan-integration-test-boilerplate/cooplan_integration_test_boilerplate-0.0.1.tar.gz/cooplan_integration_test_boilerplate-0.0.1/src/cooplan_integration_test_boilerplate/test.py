import sys


def init_request(request):
    arguments_count = len(sys.argv)

    if arguments_count != 2:
        print("error: test requires a token")
        exit(1)

    request["header"]["token"] = sys.argv[1]
