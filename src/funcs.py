'''
Created on Mon Oct 10 11:39:37 AM CEST 2022

@file: funcs.py

@author: Alvaro Viejo Alonso
'''
from numpy import ndarray
from typing import Tuple
import matplotlib.pyplot as plt


def plotGPRresults(y_mean: ndarray, y_std: ndarray, y_test: ndarray,
                   title: str = "Predictions vs Real observations",
                   xlabel: str = "Observation Index", ylabel: str = "Value",
                   xlim: Tuple[int, int] = None, mean_color="blue",
                   mean_label="GP mean", std_color="pink",
                   std_label="1 std", fill_alpha=0.2, std_linestyle="--",
                   real_marker="x", real_color="olive",
                   real_label="Real observations"
                   ) -> None:
    """
    Function that plots the result of a gaussian process prediction
    compared to the real value of the test observations.
    """
    # Get the number of predictions done
    pred_length = len(y_mean)

    # If xlim range has not been specified
    if xlim is None:
        xlim = (0, pred_length)

    # Create a common x axis
    x_range = range(pred_length)

    # plot the information
    plt.plot(x_range, y_mean, color=mean_color, label=mean_label)
    plt.plot(x_range, y_mean-y_std, color=std_color,
             linestyle=std_linestyle, label=std_label)
    plt.plot(x_range, y_mean+y_std, color=std_color,
             linestyle=std_linestyle)
    plt.scatter(x_range, y_test, color=real_color, marker=real_marker,
                label=real_label)
    plt.fill_between(x_range, y1=y_mean-y_std, y2=y_mean + y_std,
                     color=std_color, alpha=fill_alpha)

    # plot labels
    plt.xlim(xlim)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    plt.legend()
    plt.grid()
    plt.show()