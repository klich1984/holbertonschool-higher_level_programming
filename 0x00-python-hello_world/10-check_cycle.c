#include "lists.h"
/**
* check_cycle - function that check ciclo
* @list: pointer at linked list
* Return: 0 if there is no cicle and 1 if there is a cicle
*/

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *speed = list;

	if (list == NULL || list->next == NULL)
		return (0);

	/*slow = list->next;*/

	while (slow != NULL && speed != NULL)
	{
		slow = slow->next;
		speed = speed->next->next;

		if (slow == list)
			return (1);
		if (slow == speed)
			return (1);
	}

	return (0);
}
