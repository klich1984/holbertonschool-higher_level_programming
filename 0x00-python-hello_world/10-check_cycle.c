#include "lists.h"
/**
* check_cycle - function that check ciclo
* @list: pointer at linked list
* Return: 0 if there is no cicle and 1 if there is a cicle
*/

int check_cycle(listint_t *list)
{
	listint_t *current = NULL;

	if (list == NULL)
		return (0);

	current = list->next;

	while (current != NULL)
	{
		current = current->next;

		if (current == list)
			return (1);
	}

	return (0);
}
