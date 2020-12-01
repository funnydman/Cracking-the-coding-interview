/*
    Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
*/

#include "stdio.h"
#include "stdlib.h"
#include "stack.h"


typedef struct {
    struct Stack *oldest;
    struct Stack *newest;

} MyQueue;

MyQueue *MyQueueBuild() {
    MyQueue *queue = malloc(sizeof(MyQueue *));
    queue->oldest = NULL;
    queue->newest = NULL;
    return queue;
}

void myQueueAdd(MyQueue *queue, int val) {
    push(&queue->newest, val);
}

void myQueueShiftStacks(MyQueue *queue) {
    if (isEmpty(queue->oldest)) {
        while (!isEmpty(queue->newest)) {
            push(&queue->oldest, pop(&queue->newest));
        }
    }
}

int myQueuePeek(MyQueue *queue) {
    myQueueShiftStacks(queue);
    return peek(queue->oldest);
}

int myQueueRemove(MyQueue *queue) {
    myQueueShiftStacks(queue);
    return pop(&queue->oldest);
}

int MyQueuePop(MyQueue *queue) {
    return pop(&queue->newest);
}

int MyQueueSize(MyQueue *queue) {
    return getLength(queue->oldest) + getLength(queue->newest);
}

_Bool isMyQueueEmpty(MyQueue *queue) {
    return queue->newest == NULL && queue->oldest == NULL;
}
int main() {
    MyQueue *queue = MyQueueBuild();
    myQueueAdd(queue, 10);
    myQueueAdd(queue, 20);
    myQueueAdd(queue, 30);

    MyQueuePop(queue);
    MyQueuePop(queue);

    printf("%d", isMyQueueEmpty(queue));

}
