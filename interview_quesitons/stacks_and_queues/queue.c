#include "queue.h"
#include "malloc.h"


void add(Queue *queue, int val) {
    QueueNode *q_node = malloc(sizeof(QueueNode *));
    q_node->data = val;

    if (queue->last != NULL) {
        queue->last->next = q_node;
    }
    queue->last = q_node;
    if (queue->first == NULL) {
        queue->first = queue->last;
    }
}

int remove_elem(Queue *queue) {
    if (queue->first == NULL) {
        printf("%s", "no elements");
    }
    int data = queue->first->data;
    QueueNode *temp = queue->first;

    queue->first = queue->first->next;
    if (queue->first == NULL) {
        queue->last = NULL;
    }
    free(temp);
    return data;
}

int peek(Queue *queue) {
    if (queue->first == NULL) {
        printf("%s", "No elements");
    }
    return queue->first->data;
}

_Bool isEmpty(Queue *queue) {
    return queue->first == NULL;
}

