def validate_label(label: str):
    if(label is None):
        raise TypeError('label is None')
    if(len(label) < 1):
        raise ValueError('label length is 0')

    return str(label)
