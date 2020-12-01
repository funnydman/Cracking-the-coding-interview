// LIFO data structure;
/* operations:
pop(): Remove the top item from the stack.
push(item): Add an item to the top of the stack.
peek(): Return the top of the stack.
isEmpty(): Return true if and only if the stack is empty.
*/

#ifndef C_TEST_STACK_H
#define C_TEST_STACK_H
typedef struct {
    int data;
    struct Stack *next;
} Stack;


extern void push(Stack **, int);
extern int pop(Stack **);
extern int getLength(Stack *);
extern int peek(Stack *);
extern _Bool isEmpty(Stack *);

#endif //C_TEST_STACK_H
