
def ansible_get_line_kwargs(kwargs):
    assert isinstance(kwargs, dict)
    li = []
    for key, value in kwargs.items():
        li.append("-e {}={}".format(key, value))
    return " ".join(li)
