import numpy as np
import pandas as pd
import math
from numpy.random import default_rng
# import plotly.express as px
# from plotly.subplots import make_subplots
# import plotly.graph_objects as go

##########################################################################################################################################################################################################################

#Linear Congruential Number Generator

#Useful Variables for Tests
#a1, b1, M1 = 1597, 51749, 244944
#seed1 = 12345
#sample1 = 10000
#nbins1 = 100

class Linear_Congruential_Random_Number_Generator:
    """Pseudo-random number generator that works based on $N_{i}=(aN_{i-1}+b)modM$, and returns the Uniformely distributed
    pseudo-random numbers.
    Requires numpy and plotly.express"""
    def __init__(self, seed, sample, M, a, b, nbins):
        self.seed = seed
        self.sample = sample
        self.M = M
        self.a = a
        self.b = b
        self.nbins = nbins

    def linear_cong_generator(self):
        """Returns an array of sample size, based on $N_{i}=(aN_{i-1}+b)modM$ pseudo-random number generator"""
        if self.seed<0:
            raise ValueError("The seed must be a positive integer")
        if self.sample<=0:
            raise ValueError("The sample must be a positive integer")
        
        U = np.zeros(self.sample)
        U[0] = self.seed
        for i in range(1, self.sample):
            U[i] = (self.a*U[i-1]+self.b)%self.M
        U = U/self.M
        
        return U
    
    def plot_pdf(self):
        """Returns the histogram plot of the PDF for the Linear Congruential random number generator"""
        x = self.linear_cong_generator()
        fig = px.histogram(x=x, histnorm="probability", nbins=self.nbins, title="Probability Density Function")
        return fig.show()
    
    def plot_2d_scatter_plot(self):
        """Returns the 2D scatter plot of the pseaudo-random points generated by the Linear Congruential random number
        generator"""
        data = self.linear_cong_generator()
        x = data[0: self.sample-1]
        y = data[1: self.sample]
        fig = px.scatter(x=x, y=y, title="2D Scatter Plot")
        return fig.show()
    
    def plot_3d_scatter_plot(self):
        """"Returns the 3D scatter plot of the pseaudo-random points generated by the Linear Congruential random number
        generator"""
        data = self.linear_cong_generator()
        x = data[0: self.sample-2]
        y = data[1: self.sample-1]
        z = data[2: self.sample]
        fig = px.scatter_3d(x=x, y=y, z=z, title="3D Scatter Plot")
        return fig.show()




##########################################################################################################################################################################################################################

#Fibonacci Random Number Generator

#Useful Variables for Tests
#mu, nu = 5, 17
#a2, b2 = 1366, 150889
#M2 = 714025
#seed2 = 12345
#sample2 = 10000
#nbins2 = 100

class Fibonacci_Random_Number_Generator:
    """Pseudo-random number generator that works based on $N_{i}=(N_{i-nu}-N_{}i-mu)modM$, and returns the Uniformely
    distributed pseudo-random numbers.
    Requires numpy and plotly.express"""
    def __init__(self, mu, nu, seed, sample, M, a, b, nbins):
        self.mu = mu
        self.nu = nu
        self.seed = seed
        self.sample = sample
        self.M = M
        self. a = a
        self.b = b
        self.nbins = nbins
    
    def fib_generator(self):
        """Returns an array of sample size, based on $N_{i}=(N_{i-nu}-N_{}i-mu)modM$ pseudo-random number generator"""
        if self.seed<0:
            raise ValueError("The seed must be a positive integer")
        if self.sample<=0:
            raise ValueError("The sample must be a positive integer")
        
        U = np.zeros(self.sample)
        U[0] = self.seed
        for i in range(1, self.sample):
            U[i] = (self.a*U[i-1]+self.b)%self.M
        
        for i in range(self.nu+1, self.sample):
            U[i] = (U[i-self.nu]-U[i-self.mu])%self.M
        U = U/self.M
        
        return U
    
    def plot_pdf(self):
        """Returns the histogram plot of the PDF for the Fibonacci random number generator"""
        x = self.fib_generator()
        fig = px.histogram(x=x, histnorm="probability", nbins=self.nbins, title="Probability Density Function")
        return fig.show()
    
    def plot_2d_scatter_plot(self):
        """Returns the 2D scatter plot of the pseaudo-random points generated by the Fibonacci random number
        generator"""
        data = self.fib_generator()
        x = data[0: self.sample-1]
        y = data[1: self.sample]
        fig = px.scatter(x=x, y=y, title="2D Scatter Plot")
        return fig.show()
    
    def plot_3d_scatter_plot(self):
        """"Returns the 3D scatter plot of the pseaudo-random points generated by the Fibonacci random number
        generator"""
        data = self.fib_generator()
        x = data[0: self.sample-2]
        y = data[1: self.sample-1]
        z = data[2: self.sample]
        fig = px.scatter_3d(x=x, y=y, z=z, title="3D Scatter Plot")
        return fig.show()




##########################################################################################################################################################################################################################

#Accept-Reject Algorithm for Standard Normal Random Number Generator

#Useful Variables for Tests
#sample = 10000
#lap_p = 0.5
#nbins = 100

class Accept_Reject_Method:
    """Pseudo-random number generator that works based on sampling the Laplace distribution, and returns the Standard Normal
    pseudo-random numbers.
    Requires numpy and plotly.express; also requires default_rng() to be defined"""
    def __init__(self, sample, lap_p, nbins):
        self.sample = sample
        self.lap_p = lap_p
        self.nbins = nbins
    
    def accept_reject(self):
        """Returns the sample of the Standard Normal Distribution based on the Accept-Reject Method and the probability of the
        Laplace Distribution lap_p"""
        
        rng = default_rng()
        
        c = np.sqrt(2*np.exp(1)/math.pi)
        U1 = rng.uniform(size=self.sample)
        U2 = rng.uniform(size=self.sample)
        L = np.ones(self.sample)
        N = []
        
        #Laplace distribution sampling
        for i in range(0, self.sample):
            if U1[i]<(1-self.lap_p):
                L[i] = np.log(2*U1[i])
            else:
                L[i] = -np.log(2*(1-U1[i]))
        
        g = 0.5*np.exp(-np.abs(L))
        f = 1/np.sqrt(2*math.pi)*np.exp(-L**2/2)
        for j in range(0, self.sample):
            if (U2[j]*c*g[j])<=f[j]:
                N.append(L[j])
        
        return N
    
    def plot_pdf(self):
        """Returns the histogram plot of the PDF for the Accept-Reject Method Standard Normal Distribution"""
        x = self.accept_reject()
        fig = px.histogram(x=x, histnorm="probability density", nbins=self.nbins, title="Probability Density Function")
        return fig.show()
    
    def plot_2d_scatter_plot(self):
        """Returns the 2D scatter plot of the pseaudo-random points generated by the Accept-Reject Method for Standard Normal
        Distribution"""
        data = self.accept_reject()
        x = data[0: len(data)-1]
        y = data[1: len(data)]
        fig = px.scatter(x=x, y=y, title="2D Scatter Plot")
        return fig.show()
    
    def plot_3d_scatter_plot(self):
        """"Returns the 3D scatter plot of the pseaudo-random points generated by the Accept-Reject Method for Standard Normal
        Distribution"""
        data = self.accept_reject()
        x = data[0: len(data)-2]
        y = data[1: len(data)-1]
        z = data[2: len(data)]
        fig = px.scatter_3d(x=x, y=y, z=z, title="3D Scatter Plot")
        return fig.show()




##########################################################################################################################################################################################################################

#Box-Muller Algorithm for Standard Normal Random Number Generator

#Useful Variables for Tests
#sample = 10000
#nbins = 100

class Box_Muller_Algorithm:
    """Pseudo-random number generator that returns two independent pseudo-random variables from the Standard Normal
    Distribution.
    Requires numpy, math, plotly.express and plotly.graph_objects; also requires default_rng() and make_subplots to be
    defined"""
    def __init__(self, sample, nbins):
        self.sample = sample
        self.nbins = nbins
    
    def box_muller(self):
        """Returns the sample of the Standard Normal Distribution based on the Box-Muller Algorithm"""
        
        rng=default_rng()
        
        U1 = rng.random(self.sample)
        U2 = rng.random(self.sample)
        
        X = np.sqrt(-2*np.log(U1))*np.cos(2*math.pi*U2)
        Y = np.sqrt(-2*np.log(U1))*np.sin(2*math.pi*U2)
        
        return X, Y
    
    def plot_pdfs(self, display_both=False):
        """Returns the histogram plot of the PDFs for the Box-Muller Algorithm-computed Standard Normal Distribution"""
        data = self.box_muller()
        X = data[0]
        if display_both==False:
            fig = px.histogram(x=X, histnorm="probability density", nbins=self.nbins, title="Probability Density Function")
            return fig.show()
        else:
            Y = data[1]
            fig = make_subplots(rows=1, cols=2)
            fig.add_trace(go.Histogram(x=X, histnorm="probability density", nbinsx=self.nbins, name="X"), row=1, col=1)
            fig.add_trace(go.Histogram(x=Y, histnorm="probability density", nbinsx=self.nbins, name="Y"), row=1, col=2)
            fig.update_yaxes(title_text="Probability Density", row=1, col=1)
            fig.update_yaxes(title_text="Probability Density", row=1, col=2)
            fig.update_layout(title_text="PDFs for X and Y")
            return fig.show()
    
    def plot_2d_scatter_plot(self):
        """Returns the 2D scatter plot of the pseaudo-random points generated by the Box-Muller Algorithm"""
        data = self.box_muller()
        X = data[0]
        Y = data[1]
        fig = px.scatter(x=X, y=Y, title="2D Scatter Plot", )
        return fig.show()




##########################################################################################################################################################################################################################

#Marsaglia Algorithm for Standard Normal Random Number Generator

#Useful Variables for Tests
#sample = 10000
#nbinbs = 100

class Marsaglia_Method:
    """Pseudo-random number generator that returns two independent pseudo-random variables from the Standard Normal
    Distribution, with max_i controlling the maximum number of iterations that the while loop will go for.
    Requires numpy, plotly.express and plotly.graph_objects; also requires default_rng() and make_subplots to be defined"""
    def __init__(self, sample, nbins, max_i=1000000):
        self.sample = sample
        self.max_i = max_i
        self.nbins = nbins
    
    def marsaglia(self):
        """Returns the sample of the Standard Normal Distribution based on the Marsaglia Algorithm"""
        
        rng=default_rng()
        
        def get_paired_sample():
            while i<+self.max_i:
                w1 = rng.uniform(-1, 1, 1)
                w2 = rng.uniform(-1, 1, 1)
                s = w1*w1 + w2*w2
                
                if s<1:
                    t = np.sqrt(-2*np.log(s)/s)
                    z1 = w1*t
                    z2 = w2*t
                    return z1, z2
        
        Z1 = np.ones(self.sample)
        Z2 = np.ones(self.sample)
        
        for i in range(0, self.sample):
            Z1[i], Z2[i] = get_paired_sample()
        
        return Z1, Z2
    
    def plot_pdfs(self, display_both=False):
        """Returns the histogram plot of the PDFs for the Marsaglia Algorithm-computed Standard Normal Distribution"""
        data = self.marsaglia()
        X = data[0]
        if display_both==False:
            fig = px.histogram(x=X, histnorm="probability density", nbins=self.nbins, title="Probability Density Function")
            return fig.show()
        else:
            Y = data[1]
            fig = make_subplots(rows=1, cols=2)
            fig.add_trace(go.Histogram(x=X, histnorm="probability density", nbinsx=self.nbins, name="X"), row=1, col=1)
            fig.add_trace(go.Histogram(x=Y, histnorm="probability density", nbinsx=self.nbins, name="Y"), row=1, col=2)
            fig.update_yaxes(title_text="Probability Density", row=1, col=1)
            fig.update_yaxes(title_text="Probability Density", row=1, col=2)
            fig.update_layout(title_text="PDFs for X and Y")
            return fig.show()




##########################################################################################################################################################################################################################

#Ziggurat Algorithm for Standard Normal Random Number Generator

##Useful Variables for Tests
#sample = 10000
#regions = 256
#nbinbs = 100

class Ziggurat_Algorithm:
    """
    Requires numpy, math and plotly.express"""
    def __init__(self, sample, regions, nbins, max_i=1000):
        self.sample = sample
        self.regions = regions
        self.nbins = nbins
        self.max_i = max_i
    
    def ziggurat(self):
        """Returns the sample of pseudo-random numbers based on the characteristic function"""
        
        rng = default_rng()
        
        X_0 = 0
        limit = 6
        rectangle_size = 1/(self.regions)
        X = np.array([])
        dX = 0.001
        current_x = X_0
        current_area, rectangle_length = 0, 0
        Z = np.ones(self.sample)
        
        while current_x < limit:
            rectangle_length = rectangle_length+dX
            current_area = ((1/np.sqrt(2*math.pi))*np.exp(-0.5*(current_x**2))-
                            (1/np.sqrt(2*math.pi))*np.exp(-0.5*(rectangle_length**2)))*rectangle_length
            if current_area > rectangle_size:
                X = np.append(X, rectangle_length)
                current_x = rectangle_length
        
        Y = (1/np.sqrt(2*math.pi))*np.exp(-0.5*(X**2))
        
        for j in range(self.sample):
            num = 0
            while (Z[j]==1) and num<self.max_i:
                i = np.random.randint(0, len(X))
                u0 = rng.uniform(-1,1)
                u1 = rng.uniform()
                x = u0*X[i]
                if abs(x)<X[i-1]:
                    Z[j] = x
                else:
                    y = Y[i]+u1*(Y[i-1]-Y[i])
                    point = (1/np.sqrt(2*math.pi))*np.exp(-0.5*(x**2))
                    if y<point:
                        Z[j] = x
                num = num+1
        
        return Z
    
    def plot_pdf(self):
        data = self.ziggurat()
        fig = px.histogram(x=data, histnorm="probability density", nbins=self.nbins, title="Probability Density Function")
        return fig.show()




##########################################################################################################################################################################################################################

if __name__ == '__main__':
    
    #Linear_Congruential_Random_Number_Generator(12345, 10000, 244944, 1597, 51749, 100).plot_pdf()
    #Fibonacci_Random_Number_Generator(5, 17, 12345, 10000, 714025, 1366, 150889, 100).plot_pdf()
    #Accept_Reject_Method(10000, 0.5, 100).plot_pdf()
    #Box_Muller_Algorithm(10000, 100).plot_pdfs(display_both=True)
    #Marsaglia_Method(10000, 100).plot_pdfs(display_both=True)
    Ziggurat_Algorithm(10000, 256, 100).plot_pdf()
