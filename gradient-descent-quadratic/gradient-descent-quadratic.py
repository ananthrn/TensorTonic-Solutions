def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    x = x0
    for step in range(steps):
        grad_x = 2 * x * a + b 
        x -= grad_x * lr
    
    return x