from function import func


def forward(x, c, dx):
    return (func(x + dx, c) - func(x, c)) / dx


def backward(x, c, dx):
    return (func(x, c) - func(x - dx, c)) / dx


def central(x, c, dx):
    return (func(x + dx, c) - func(x - dx, c)) / 2*dx
