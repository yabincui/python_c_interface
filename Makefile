
all: libf2.so

libf1.a : f1.o
	ar rcu libf1.a f1.o

libf2.so : f2.o libf1.a
	g++ -o libf2.so -shared f2.o -L. -lf1

%.o : %.cpp
	g++ -fvisibility=hidden -c -fPIC -o $@ $<

clean:
	rm f1.o f2.o libf1.a libf2.so -f
