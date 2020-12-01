#include "stack.h"
#include "malloc.h"
#include "stdlib.h"

void push(Stack **top, int elem) {
    Stack *node = malloc(sizeof(Stack));
    node->data = elem;

    node->next = (*top);
    (*top) = node;
}

int getLength(Stack *top) {
    int length = 0;
    while (top != NULL) {
        length += 1;
        top = top->next;
    }
    return length;

}

int peek(Stack *top) {
    if (top == NULL) {
        printf("Stack is empty");
        exit(1);
    }
    return top->data;
}

_Bool isEmpty(Stack *top) {
    return !top;
}

int pop(Stack **top) {
    if (isEmpty(*top)) {
        printf("Stack is empty");
        exit(1);
    }
    Stack *temp = *top;
    *top = (*top)->next;
    int hopped = temp->data;
    free(temp);
    return hopped;
}
