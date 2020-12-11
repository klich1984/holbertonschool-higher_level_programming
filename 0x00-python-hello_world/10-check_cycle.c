#include "lists.h"
/**
* check_cycle - function that check ciclo
* @list: pointer at linked list
* Return: 0 if there is no cicle and 1 if there is a cicle
*/

int check_cycle(listint_t *list)
{
	listint_t *current = NULL;

	current = list->next;

	if (list == NULL)
		return (0);

	while (current != NULL)
	{
		current = current->next;

		if (current == list)
			return (1);
	}

	if (current == NULL)
		return (0);

	return (0);
}
