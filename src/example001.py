# example001.py

def example001(input: str):
    '''
        Detect capitalization word and write new line.
        Detect point and reset tabs counter.
    '''
    result = ''
    left_pad_counts = 0
    for word in input.split(' '):
        if word == word.capitalize() and word not in ['I']:
            if result:
                result += '\n'
            result += ('	' * left_pad_counts) + word
            left_pad_counts += 1
        else:
            if result:
                result += ' '
            result += word

        if word.endswith('.'):
            left_pad_counts = 0

    return result