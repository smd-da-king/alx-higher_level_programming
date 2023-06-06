#include "lists.h"

/**
 * check_cycle - check if there is a cycle in a linked list
 * @list: the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *sl, *ft;

	if (list == NULL || list->next == NULL)
		return (0);

	sl = list->next;
	ft = (list->next)->next;

	while (sl && ft && ft->next && ft->next->next)
	{
		if (sl == ft)
			return (1);

		sl = sl->next;
		ft = (ft->next)->next;
	}

	return (0);
}
