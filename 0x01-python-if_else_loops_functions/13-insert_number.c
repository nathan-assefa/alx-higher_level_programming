#include "lists.h"
#include <stdlib.h>
#include <stddef.h> 

/**
 * insert_node- Inserting node at any position
 * @head: pointer to the linked list
 * @number: Number to be inserted
 * Return: the updated linked list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *ptr;
	unsigned int i;

	if (*head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->n = number;
	new_node->next = NULL;
	ptr = *head;

	i = 0;
	while (i < 5)
	{
		ptr = ptr->next;
		i++;
	}

	new_node->next = ptr->next;
	ptr->next = new_node;
	return (*head);
}
