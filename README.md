# DOE
utils for design DOE

# Latin Hypercube Sampling
- statistical method for generating a near-random values from a multidimentional distribution
- LHS was designed by McKay in 1979 
    - ![A Comparison of Three Methods for Selecting Values of Input Variables in the Analysis of Output from a Computer Code](https://www.asc.ohio-state.edu/statistics/comp_exp/jour.club/McKayConoverBeckman.pdf)
- Latin Square
    - There is only one sample in each row and each column
- Algorithm overview
    - When sampling a function of N variables
    - the range of each variable is devided into M
        - M is equally probable intervals
    - M sample points are then placed to satisfy the Latin Hypercube requirements
        - this force the number of divisions
        - M is equal for each variables
    - main advantage is "independence"
        - this sampling scheme does not require more points for more dimensions
    - another is that random sampling can be taken one at a time, remembering which samples were taken so far
- ![Latin Hypercube sampling](https://en.wikipedia.org/wiki/Latin_hypercube_sampling)

# pyDOE
- this repository utilize ![pyDOE]([https://pythonhosted.org/pyDOE/randomized.html#randomized) 
