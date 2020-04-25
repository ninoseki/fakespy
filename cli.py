import sys

import fire

from fakespy.client import Client

sys.path = ["."] + sys.path[1:]  # noqa # isort:skip


def make_request(command: str, c2: str, mobile_number: str = "xx"):
    client = Client(c2=c2, mobile_number=mobile_number)
    res = client.query(command)
    print(res)


if __name__ == "__main__":
    fire.Fire(make_request)
