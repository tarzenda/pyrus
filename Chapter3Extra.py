print("starting program")

x=1
y=2
z=3

def foo():
    print("entering foo()")
    x=10
    y=20
    bar()
    print(x)
    print("exiting foo()")

def bar():
    print("entering bar()")
    x = 30
    print(x)
    baz()
    print("exiting bar()")

def baz():
    print("entering baz()")
    print(x)
    print("exiting baz()")

foo()
print("ending program")
