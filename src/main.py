import streamlit as st
import matplotlib.pyplot as plt
from fractal import mandelbrot

xmin, xmax, ymin, ymax = -2., 0.47, -1.12, 1.12
xo, yo = (xmin + xmax)/2, (ymin + ymax)/2
r = 200
maxiter = 100
z = 1

if __name__ == "__main__":
    st.title("Mandelbrot Fractal")

    st.sidebar.title("Settings")
    cmap = st.sidebar.radio("Color map", ("plasma", "twilight_shifted", "seismic"), index=1)
    cg = st.sidebar.slider("Color gradient", 0.1, 2., 1., 0.1, "%.1f") # Color gradient
    r = st.sidebar.slider("Resolution", 100, 500, r) # r = st.sidebar.slider("Resolution", 0.001, 0.01, r, 0.001, "%.3f")
    maxiter = st.sidebar.slider("Max Iterations", 10, 200, maxiter)
    z = st.sidebar.slider("Zoom", 0.5, 10., 1., 0.1, "%.1f")
    x0 = st.sidebar.slider("X Center", xmin, xmax, xo)
    y0 = st.sidebar.slider("Y Center", ymin, ymax, yo)

    image = mandelbrot(x0,y0, r, maxiter, z)
    fig = plt.figure()
    plt.imshow(image**cg, cmap=cmap) #plasma, twilight_shifted, seismic
    plt.axis('off')
    st.pyplot(fig)