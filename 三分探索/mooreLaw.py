P = float(input())

def get_compute_time(x):
    return x + P * (2 ** (-2*x/3))

low = 0
high = 1e+14

while high-low > 5e-9:
    c1 = (2*low+high)/3
    c2 = (low+2*high)/3

    if get_compute_time(c1) > get_compute_time(c2):
        low = c1
    else:
        high = c2

print(get_compute_time(high))