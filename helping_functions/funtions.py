import datetime
import random
import re


def randomEmail():
    email = "qaselenium"
    rand = random.randint(10000, 99999)
    domena = "@gmail.com"
    email = email + str(rand) + domena
    print(email)
    return email


def randomPhone():
    phone = random.randint(1000000000, 9999999999)
    print(phone)
    return phone


def urlify(s):
    # Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s]", '', s)
    # Replace all runs of whitespace with a single dash
    s = re.sub(r"\s+", '-', s)
    return s


def datetime_now(prefix):
    symbols = str(datetime.datetime.now())
    return prefix + "-" + "".join(symbols)


def screenShotsFolder():
    path = os.getcwd()
    dl = len(path)
    final = path[0:dl - 6]
    final = str(final) + "/Screenshots/"
    return final

