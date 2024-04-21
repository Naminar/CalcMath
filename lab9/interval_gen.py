from numpy.linalg import solve as tridiag 

def generate_interval(frames):
    if frames < 25:
        return 1000
    if frames < 50:
        return 500
    return int(1000*10/frames)

def fast_frames(frames):
    return int(1000*5/frames)