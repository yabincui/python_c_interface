#include <stdio.h>

void f1();

extern "C" {

#define EXPORT __attribute__((visibility("default")))

void f2() EXPORT;
int incValue(int) EXPORT;
double incDoubleValue(double) EXPORT;
void incInlineValue(int*) EXPORT;
int* retPointer() EXPORT;
void printString(const char*) EXPORT;
const char* retString() EXPORT;
void incArray(int* s, int n) EXPORT;
int* retArray() EXPORT;

struct MyStruct {
	int count;
	int* s;
};

void printStruct(struct MyStruct) EXPORT;
void printStructP(struct MyStruct*) EXPORT;
struct MyStruct retStruct() EXPORT;
struct MyStruct* retStructP() EXPORT;

void callCallback(int (*)()) EXPORT;
}

void f2() {
  printf("this is f2\n");
  f1();
}

int incValue(int value) {
  return value + 1;
}

double incDoubleValue(double value) {
  return value + 0.1;
}

void incInlineValue(int* value) {
  *value += 1;
}

int* retPointer() {
	static int i = 0;
	return &i;
}

void printString(const char* s) {
	printf("%s\n", s);
}

const char* retString() {
	return "Hello, world";
}

void incArray(int* s, int n) {
	for (int i = 0; i < n; ++i) {
		s[i] = i + 1;
	}
}

int* retArray() {
	static int s[10];
	for (int i = 0; i < 10; ++i) {
		s[i] = i + 1;
	}
	return s;
}

void printStruct(MyStruct myStru) {
	for (int i = 0; i < myStru.count; ++i) {
		printf("%d ", myStru.s[i]);
	}
	printf("\n");
}

void printStructP(MyStruct* p) {
	for (int i = 0; i < p->count; ++i) {
		printf("%d ", p->s[i]);
	}
	printf("\n");
}

MyStruct retStruct() {
	MyStruct myStru;
	myStru.count = 10;
	static int s[10];
	myStru.s = s;
	for (int i = 0; i < 10; ++i) {
		s[i] = i + 1;
	}
	return myStru;
}

MyStruct* retStructP() {
	static MyStruct myStru;
	myStru.count = 10;
	static int s[10];
	myStru.s = s;
	for (int i = 0; i < 10; ++i) {
		s[i] = i + 1;
	}
	return &myStru;
}

void callCallback(int (*callback)()) {
	for (int i = 0; i < 10; ++i) {
		printf("%d ", callback());
	}
	printf("\n");
}
