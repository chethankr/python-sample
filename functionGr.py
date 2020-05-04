
# importing the required modules 
import matplotlib.pyplot as plt 
import numpy as np 


def func1():
    # setting the x - coordinates
    x = np.arange(0, 2*(np.pi), 0.1)
    # setting the corresponding y - coordinates
    y = np.sin(x)

    # potting the points
    plt.plot(x, y)

    # function to show the plot
    plt.show()



def func2():
    # create 1000 equally spaced points between -10 and 10
    x = np.linspace(-10, 10, 1000)

    # calculate the y value for each element of the x vector
    #y = x**2 + 2*x + 2
    y = e ** 2 + 2 * x + 2
    fig, ax = plt.subplots()
    ax.plot(x, y)
    # function to show the plot
    plt.show()

def func3():
    x = np.linspace(0, 10, 10)
    print('x', x)

    y = np.exp(x)
    print('y', y)

    rate = y / x
    print('rate' , rate)


    plt.figure()
    plt.plot(x, y)
    plt.xlabel('$x$')
    plt.ylabel('$\exp(x)$')


    plt.figure()
    plt.plot(x, -np.exp(-x))
    plt.xlabel('$x$')
    plt.ylabel('$-\exp(-x)$')

    plt.show()


#func1()
#func2()
func3()