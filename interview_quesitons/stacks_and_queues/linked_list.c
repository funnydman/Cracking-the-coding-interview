#include "malloc.h"
#include "stdlib.h"
#include "linked_list.h"

void print_list(struct Node *head) {
    struct Node *current = head;
    while (current != NULL) {
        printf("%d\n", current->data);
        current = current->next;
    }
}

struct Node *delete_node(struct Node *head, int value) {
    if (head == NULL) {
        return head;
    }
    if (head->data == value) {
        head = head->next;
        return head;
    }
    struct Node *current = head;

    while (current->next != NULL) {
        if (current->next->data == value) {
            current->next = current->next->next;
            return head;
        }
        current = current->next;
    }

    return head;
}

struct Node *append_node(struct Node *head, int value) {
    // write this down
    struct Node *current = head;


    while (current->next != NULL)
        current = current->next;

    struct Node *node = malloc(sizeof(struct Node *));
    node->next = NULL;
    node->data = value;

    current->next = node;

    return head;
}

struct Node *insert_node(struct Node **head, int value) {
    struct Node *node = malloc(sizeof(struct Node *));

    node->data = value;
    node->next = *head;
    *head = node;

    return node;
}

// remove the first element
int pop(struct Node **head) {
    int retval = -1;
    struct Node *next_node = NULL;
    if (!*head) {
        return -1;
    }
    next_node = (*head)->next;
    retval = (*head)->data;
    free(*head);
    *head = next_node;
    return retval;
}

int remove_last(struct Node *head) {
    int retval = 0;

    if (head->next == NULL) {
        retval = head->data;
        free(head);
        return retval;
    }

    struct Node *c = head;
    while (c->next != NULL) {
        c = c->next;
    }
    retval = c->next->data;
    free(c->next);
    c->next = NULL;
    return retval;
}

