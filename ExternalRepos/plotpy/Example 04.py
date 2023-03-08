import numpy as np
from plotpy.widgets.fit import FitParam, guifit


def test():
    x = np.linspace(-10, 10, 1000)
    y = np.cos(1.5 * x) + np.random.rand(x.shape[0]) * .2

    def fit(x, params):
        a, b = params
        return np.cos(b * x) + a

    a = FitParam("Offset", 1., 0., 2.)
    b = FitParam("Frequency", 2., 1., 10., logscale=True)
    params = [a, b]
    values = guifit(x, y, fit, params, xlabel="Time (s)", ylabel="Power (a.u.)")
    print(values)
    print([param.value for param in params])


if __name__ == "__main__":
    test()
    