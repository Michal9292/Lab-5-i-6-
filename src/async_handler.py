import threading


def run_async(function, *args):
    thread = threading.Thread(
        target=function,
        args=args
    )

    thread.daemon = True
    thread.start()