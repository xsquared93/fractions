# add_rat: tuple tuple -> tuple
# this function adds to fractions together.
def add_rat(e1, e2):
    if arity(e1) == 2:
        (n1, op, d1) = e1
        (n2, opx, d2) = e2
        if arity(e2) == 2:
            return (n1 * d2) + (n2 * d1), op, d1 * d2
    else:
        return 0
    
# sub_rat: tuple tuple -> tuple
# this function subtracts fractions
def sub_rat(e1, e2):
    if arity(e1) == 2:
        (n1, op, d1) = e1
        (n2, opx, d2) = e2
        if arity(e2) == 2:
            return (n1 * d2) - (n2 * d1), op, d1 * d2
     else:
         return 0
     
# mul_rat: tuple tuple -> tuple
# this function multiplies fractions
def mul_rat(e1, e2):
    if arity(e1) == 2:
        (n1, op, d1) = e1
        (n2, opx, d2) = e2
        if arity(e2) == 2:
            return n1 * n2, op, d1 * d2
    else:
         return 0
     
#  div_rat: tuple tuple -> tuple
# this function divides fractions
def div_rat(e1, e2):
    if arity(e1) == 2:
        (n1, op, d1) = e1
        (n2, opx, d2) = e2
        if arity(e2) == 2:
            return n1 * d2, op, n2 * d1
    else:
        return 0
        
def arity(exp):
    if isinstance(exp, tuple):
        return len(exp) - 1
    else:
        return 0
    
