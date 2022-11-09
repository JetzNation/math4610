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
**7. What are basic conditions for fixed point iteration to converge when searching for the root of a nonlinear function of a single variable. How are these conditions related to the iteration function, $$g(x))$$, defined in terms of the original function, $$f$$, defined as the input of a root finding problem?**  
Answer:  
There are two basic conditions that allow fixed point iteration to converge, they are:  
 |g(x*)| < 1 where f(x*) = 0  
 f(x) has to exist for all x inside of the given interval.  
**8. State two advantages and two disadvantages of Newton's method for finding roots of nonlinear functions.**  
Answer:  
The two advantages for newton's method are:  
 Newton's method converges very rapidly.  
 Newton's method is very simple to program.  
The two disadvantages for newton's method are:  
 Newton's method requires the derivative, and might not be easily obtainable.  
 Newton's method requires the initial guess for the root needs to be pretty close to the actual root.  
**9. Why would a person use the Secant method in place of Newton's method?**  
Answer:  
A person would use the secant method over newton's method because newton's method requires the function's derivative. That required derivative may not be easily obtainable.  
**10. Distinguish between the terms data fitting, interpolation, and polynomial interpolation.**  
Answer:  
data fitting: The act of fitting models to data.  
interpolation: Interpolation is a type of estimation, a method of constructing (finding) new data points based on the range of a discrete set of known data points.  
polynomial interpolation: Polynomial interpolation is the interpolation of a given data set by the polynomial of lowest possible degree that passes through the points of the dataset.  
**11. State one advantage and two disadvantages of using the monomial basis for polynomial interpolation.**  
Answer:  
One advantage is that it is easy to use because the derivatives and integrals are simple.  
The disadvantages are:  
 We have to use the Vandermonde matrix in order to calculate this. This is a disadvantage because it becomes harder to work with as the matrix size increases.  
 It's error can be large because higher degree polynomials can cross the x-axis many times, resulting in many oscillations.  
**12. Define Lagrange polynomials (the cardinal functions) and how are they used in the development of algorithms for numerical integration.**  
Answer:  
The Lagrange polynomial is the unique polynomial of lowest degree that interpolates a given set of data. It is used to approximate complicated integrals by rewriting it as a sum of coefficients that are multiplied by Lagrange polynomials.  
**13. We have bumped into errors in the approximating roots of functions, approximating derivatives using difference quotients, approximations of solutions of differential equations and approximations of definite integrals.
    $$$
      | error | \leq C\ h^p
    $$$
    Write a brief explanation of the formula in terms the increment, $$h$$, the constant, $$C$$, and how to compute these parameters. Use an example like Newton's method for finding roots of functions.**  
Answer:  
C: This variable is dependant on the smoothness of the function. We can find it by using a Taylor series expansion.  
h: As h goes to 0, the error will be order p and will be act like C * h^p.  
These are both found by using the Taylor series on our root. Using this, we can see that the error for Newton's method is bounded by C such that h = ek and p = 2. This means that the error is bounded to the error the iteration before.  
**14. Discuss the pros and cons of using the Trapezoid rule for approximating definite integrals.**  
The advantages are:  
 It is more accurate than the left end point rule and right end point rule.  
 We are able to use its composite rule that can calculate n + 1 iterations.  
The disadvantages are:  
 It's less accurate than Simpson's rule.  
 It is unable to accurately estimate the second derivative.  
**15. Compare the explicit and implicit Euler methods for approximate solution of initial value problems. You can use the logistic equation to illustrate your explanations.**  
Answer:  
The explicit Euler method is able to approximate an ordinary differential equation by using tangent lines which is problematic because it underestimates concave functions and overestimates convex functions. The implicit method is the opposite in that it overestimates concave functions and underestimates convex functions. The implicit method is used over the explicit every once in a while because it is able to approximate ordinary differential equations that have solutions that can change quickly in an interval.
