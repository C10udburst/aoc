.PHONY:: all

PY_IN = $(wildcard *.py)
PY_OUT = $(PY_IN:.py=)

$(PY_OUT): %: %.py
	python3 $<

.PHONY:: $(PY_OUT)
all:: $(PY_OUT)

CPP_IN = $(wildcard *.cpp)
CPP_OUT = $(CPP_IN:.cpp=)

$(CPP_OUT): %: %.cpp
	g++ -std=c++17 -o a.out $<
	./a.out

.PHONY:: $(CPP_OUT)
all:: $(CPP_OUT)