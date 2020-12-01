/*
Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array) . The stack supports the following operations: push, pop, peek, and isEmpty.
*/

#include "stdio.h"
#include "stdlib.h"
#include "stack.h"

#define N 5

typedef struct {
    Stack *stack;
    Stack *temp;
} ComplexStack;

void pushToStack(ComplexStack *stk, int val) {
    if (!stk->stack) {
        push(&stk->stack, val);
        return;
    }
    int top = peek(stk->stack);

    if (top < val) {
        while (stk->stack && (top = peek(stk->stack)) < val) {
            push(&stk->temp, top);
            pop(&stk->stack);
        }
        push(&stk->temp, val);

        while (stk->temp) {
            push(&stk->stack, pop(&stk->temp));
        }
    } else {
        push(&stk->stack, val);
    }
}


void print_stack(ComplexStack *stk) {
    while (stk->stack) {
        printf("%d\n", stk->stack->data);
        pop(&stk->stack);
    }
}

int main() {
    ComplexStack *compStack = malloc(sizeof(ComplexStack *));

    int arr[N] = {10, 5, 15, 8, 11};

    for (int i = 0; i < N; i++) {
        pushToStack(compStack, arr[i]);
    }
    print_stack(compStack);

}
