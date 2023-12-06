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

RS_IN = $(wildcard *.rs)
RS_OUT = $(RS_IN:.rs=)

$(RS_OUT): %: %.rs
	rustc -o a.out --crate-type=bin --crate-name=aoc $<
	RUST_BACKTRACE=1 ./a.out

.PHONY:: $(RS_OUT)
all:: $(RS_OUT)

KT_IN = $(wildcard *.kt)
KT_OUT = $(KT_IN:.kt=)

$(KT_OUT): %: %.kt
	kotlinc $< -include-runtime -d a.jar
	java -jar a.jar

.PHONY:: $(KT_OUT)
all:: $(KT_OUT)

HS_IN = $(wildcard *.hs)
HS_OUT = $(HS_IN:.hs=)

$(HS_OUT): %: %.hs
	ghc -o a.out -dynamic $<
	rm *.hi *.o
	./a.out