# All 16 binary truth functions:
# http://en.wikipedia.org/wiki/Truth_function#Table_of_binary_truth_functions

# Degenerate cases - only depend on one variable:
def is_contradiction(p,q):
    print(False)

def is_tautology(p,q):
    print("TODO - NOT IMPLEMENTED")

def is_proposition_p(p,q):
    print(p)

def is_negation_of_p(p,q):
    print("TODO - NOT IMPLEMENTED")

def is_proposition_q(p,q):
    print(q)

def is_negation_of_q(p,q):
    print(not(q))


# Non-degenerate cases - depend on both p and q:
def is_conjunction(p,q):
    print("TODO - NOT IMPLEMENTED")

def is_alternative_denial(p,q):
    print(not(p and q))

def is_disjunction(p,q):
    print(p or q)

def is_joint_denial(p,q):
    print("TODO - NOT IMPLEMENTED")

def is_material_nonimplication(p,q):
    print(p and not(q))

def is_material_implication(p,q):
    print("TODO - NOT IMPLEMENTED")

def is_converse_nonimplication(p,q):
    print(not(p) and q)

def is_converse_implication(p,q):
    print(p or not(q))

def is_exclusive_disjunction(p,q):
    print("TODO - NOT IMPLEMENTED")

def is_biconditional(p,q):
    print(p == q)
