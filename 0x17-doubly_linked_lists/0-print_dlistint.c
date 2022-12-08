#include "lists.h"

/**
 * * print_dlistint- To print doubly linked list
 * * @h: pointer to doubly linke list;
 * * Return: The size of the doubly linked list
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t i = 0;
	const dlistint_t *current;

	current = h;
	while (current != NULL)
	{
		printf("%d\n", current->n);
		current = current->next;
		i++;
	}
	return (i);
}
