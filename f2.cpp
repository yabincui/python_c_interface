#include <stdio.h>

void f1();

extern "C" {

void __attribute__((visibility ("default"))) f2();
int __attribute__((visibility ("default"))) incValue(int);
double __attribute__((visibility ("default"))) incDoubleValue(double);
void __attribute__((visibility ("default"))) incInlineValue(int*);
}

//void __attribute__((visibility ("default"))) f2() {
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
