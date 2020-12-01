/*
FIFO structure,

operations:
add(item): Add an item to the end of the list.
remove(): Remove the first item in the list.
peek() : Return the top of the queue.
isEmpty() : Return true if and only if the queue is empty.
 */

#ifndef C_TEST_QUEUE_H
#define C_TEST_QUEUE_H
typedef struct {
    int data;
    struct QueueNode *next;
} QueueNode;

typedef struct {
    QueueNode *first;
    QueueNode *last;
} Queue;

extern void add(Queue *, int);

extern int remove_elem(Queue *);

extern int peek(Queue *);

extern _Bool isEmpty(Queue *);

#endif //C_TEST_QUEUE_H
