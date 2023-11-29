#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: the list
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */

int check_cycle(listint_t *list)
{
	listint_t *sw = list;
	listint_t *ft = list;

	if (!list)
		return (0);

	while (sw && ft && ft->next)
	{
		sw = sw->next;
		ft = ft->next->next;
		if (sw == ft)
			return (1);
	}
	return (0);
}
