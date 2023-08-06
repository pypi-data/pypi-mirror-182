def sort(listing: list, reverse=bool(False)) -> list:
    for _ in range(len(listing)):
        for i in range(len(listing)):
            if type(listing[i]) == int or float:
                if i == 0:
                    pass
                else:
                    if not reverse:
                        if listing[i] < listing[i - 1]:
                            x2 = listing[i - 1]
                            listing[i - 1] = listing[i]
                            listing[i] = x2
                    elif reverse:
                        if listing[i] > listing[i - 1]:
                            x2 = listing[i - 1]
                            listing[i - 1] = listing[i]
                            listing[i] = x2
            elif type(listing[i]) == str:
                if i == 0:
                    pass
                else:
                    if not reverse:
                        if len(listing[i]) < len(listing[i - 1]):
                            x2 = listing[i - 1]
                            listing[i - 1] = listing[i]
                            listing[i] = x2
                    elif reverse:
                        if len(listing[i]) > len(listing[i - 1]):
                            x2 = listing[i - 1]
                            listing[i - 1] = listing[i]
                            listing[i] = x2

    return listing


def random_index(listing: list, step=int(1), reverse=bool(False)) -> list:
    from random import randint as r
    listing2 = listing
    for _ in range(step):
        for i in range(len(listing)):
            random = r(0, len(listing) - 1)
            listing.append(listing2[random])
            del listing2[random]
    if reverse:
        listing = listing[::-1]
    return listing


def factorial(factor: int) -> int:
    if factor == 0:
        return 1
    else:
        return factor * factorial(factor - 1)


def asymp_app(asymp: int) -> float:
    from math import log
    total = 0
    for i in range(1, asymp + 1):
        total = total + 1 / i
    return total - log(asymp)


def value_split(value: str or int, connect=int(1), reverse=bool(False)) -> object:
    value_list = []

    for i in value:
        value_list.append(i)

    if connect == 1:
        for i in range(len(value_list)):
            try:
                value_list[i] = int(value_list[i])
            except ValueError:
                try:
                    value_list[i] = str(value_list[i])
                except ValueError:
                    raise ValueError

    elif connect > 1:
        jo = []

        for _ in range(len(value_list) // connect):
            total = ''
            for i in range(connect):
                total += str(value_list[i])
            del value_list[:connect]
            jo.append(total)
        total = ''
        for i in range(len(value_list)):
            total += str(value_list[i])
        jo.append(total)
        value_list = jo
        for i in range(len(value_list)):
            try:
                value_list[i] = int(value_list[i])
            except ValueError:
                pass
    if value_list[-1] == '':
        del value_list[-1]
    if reverse:
        value_list.reverse()
        return value_list
    elif not reverse:
        return value_list


def average(listing: list or str, separation=False, limit=0, integer=bool(False)) -> float:
    if not separation:
        listing2 = listing
        listing = 0
        for i in range(len(listing2)):
            listing += listing2[i]
    elif separation:
        listing2 = []
        for i in listing:
            listing2.append(int(i))
        listing = 0
        for i in range(len(listing2)):
            listing += listing2[i]
    total = listing/len(listing2)
    if limit > 0:
        listr = []
        for i in range(limit+2):
            listr.append(str(total)[i])
        listr = ''.join(listr)
        return float(listr)
    elif limit == 0:
        if integer:
            return int(total)
        else:
            return total
    else:
        raise ValueError
