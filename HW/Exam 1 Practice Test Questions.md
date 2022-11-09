**Name:** Andy Skabelund  
**1. Define relative and absolute errors and give examples where relative error is a better measure and examples where absolute error may be a better measure of differences.**  
Answer:  
The formula for relative error is: |exact - approx| / |exact|  
An example where relative error is a better measure is when you want to be able to compare things that are measured in different units.  
For example, let’s say you’re measuring height and weight of a dog. The height of the dog is measured as 84 cm with an absolute error of ±3 cm. The weight of the dog is 35 lbs with an absolute error of ± 1 lbs.  

The formula for absolute error is: |exact - approx| An example where absolute error is a better measure is to measure how far 'off' a measurement is from a true value or an indication of the uncertainty in a measurement.  
For example, if you measure the width of a book using a ruler with millimeter marks, the best you can do is measure the width of the book to the nearest millimeter.  
**2. Describe the difference between the concepts of accuracy, efficiency, and robustness in the development of algorithms for the approximation of solutions of mathematical problems.**  
Answer:  
Accuracy: There is a correlation between accuracy and error. The smaller you can get your error, the more accurate your approximation will be.  
Efficiency: Efficiency in coding describes how you should use as little resources as possible and removing redundant code, in order to achieve maximum speed for your program.  
Robustness: Robustness is the ability of the same code to be applicable in multiple problems, while still maintaining relevance.  
**3. Define the rounding unit (or the machine precision) and explain the importance of the rounding unit for computation.**  
Answer:  
Machine precision: Is an upper bound on the relative approximation error due to rounding in floating point arithmetic. The error is small when used in a few calculations, but can add up to a lot of error when used in more calculations.  
**4. What is a nonlinear equation? Compare this to linear equations.**  
Answer:  
A Nonlinear equation can be defined as the equation having the maximum degree of 2 or more than 2. A Linear equation can be defined as the equation having a maximum of only one degree.  
**5. Is the bisection (i) efficient, (ii) accurate, (iii) robust? What smoothness conditions on the function are needed for Bisection to work?**  
Answer:  
Efficiency: Bisection is not very efficient because it converges very slowly.  
Accuracy: Bisection is pretty accurate and the error is guaranteed to be bounded.  
Robustness: Bisection is somewhat robust because it is simple to program, but it might not be the best choice due to its slow speed.  
**6. Does the bisection method provide a robust platform for the development of algorithms for the solution of systems of nonlinear equations?**  
Answer:  
Bisection does not provide a robust platform because although it may find a root in the given interval, it doesn't describe the function near that root very well. It also only finds one root out of many possible roots. I would suggest the secant or newton's method to solve the nonlinear system.  
