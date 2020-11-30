import os

def disk_usage(path):
    """
    Return the number of bytes used by a file/filder and any descendents
    """
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)
    
    print('{0:<7}'.format(total), path)

    return total

print(disk_usage('/Users/namnguyen/dev/personal/dsa'))

