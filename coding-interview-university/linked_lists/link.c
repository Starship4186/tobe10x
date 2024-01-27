// Does not work; segmentation fault :( 
// REVIEW Code review needed
#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int data;
    struct node *next;
}
node;

node *head; // Holds the address of the starting point

int createLinkList(data)
{
    node *newnode, *temp;
    newnode = malloc(sizeof(node)); // Create a newnode in the memory
    newnode->data = data;
    if (head == NULL)
    {
    newnode->next = NULL;
    head->next = newnode;
    }
    else
    {
        temp = head;
        // Loop till the last
        while (temp->next != NULL)
        {
            temp = temp->next;

        }

        temp->next = newnode;
    }
    return 0;
}

void display()
{
    node *temp;

    temp = head;
    
    if (temp == NULL)
    {
        printf("List is empty");

    }
    else
    {
        for(temp=head; temp->next != NULL; temp = temp->next)
        {
            printf("%d ", temp->data);
        }
    }
}

int main(void){

    printf("hello world");

    // Initializing head to NULL to mark it as empty
    head = NULL;

    int data = 2;
    createLinkList(data);

    return 0;
}