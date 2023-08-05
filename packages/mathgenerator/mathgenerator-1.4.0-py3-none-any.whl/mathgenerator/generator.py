from os import sep as SEP
import traceback
import bisect

genList = []


class Generator:
    def __init__(self, title, id, func, kwargs):
        self.title = title
        self.id = id
        self.func = func
        self.kwargs = kwargs

        # Gets the path to the file the generator is in
        path, _, _, _ = traceback.extract_stack()[-2]
        # Gets the name of the file without the extension
        funcname = path.split(SEP)[-1].strip()[:-3]
        # Gets the name of the subject folder
        subjectname = path.split(SEP)[-2].strip()
        bisect.insort(genList, [id, title, self, funcname, subjectname, kwargs])

    def __str__(self):
        return str(self.id) + " " + self.title

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


def getGenList():
    return genList
