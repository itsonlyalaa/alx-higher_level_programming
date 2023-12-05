#include "lists.h"

/**
 *  pali_check - Check for palindrome
 *  @lft: Go left
 *  @ryt: Go right
 *
 *  Return: Integer
 */

int pali_check(listint_t **lft, listint_t *ryt)
{
	int is_pali = 0;

	if (ryt)
	{
		is_pali = pali_check(lft, ryt->next);
	}
	else
	{
		return (1);
	}

	if (is_pali == 1)
	{
		if ((*lft)->n == ryt->n)
		{
			(*lft) = (*lft)->next;
			return (1);
		}
	}
	return (0);
}

/**
 * is_palindrome - Check if is palindrome
 * @head: Head of Linked List
 *
 * Return: 0 if not palindrome, 1 if is palindrome
 */

int is_palindrome(listint_t **head)
{

	if (!*head || !(*head))
	{
		return (1);
	}

	if (pali_check(head, *head))
	{
		return (1);
	}
	return (0);
}
