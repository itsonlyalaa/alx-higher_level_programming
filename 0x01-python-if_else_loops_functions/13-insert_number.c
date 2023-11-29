#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL.
 * Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nodes = *head, *newn;

	newn = malloc(sizeof(listint_t));
	if (newn == NULL)
		return (NULL);
	newn->n = number;

	if (nodes == NULL || nodes->n >= number)
	{
		newn->next = nodes;
		*head = newn;
		return (newn);
	}

	while (nodes && nodes->next && nodes->next->n < number)
		nodes = nodes->next;

	newn->next = nodes->next;
	nodes->next = newn;

	return (newn);
}
