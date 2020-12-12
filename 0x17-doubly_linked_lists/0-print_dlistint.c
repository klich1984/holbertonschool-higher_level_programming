#include "lists.h"

size_t print_dlistint(const dlistint_t *h)
{
	size_t num_nodo = 0;
	int i = 0;

	if (h == NULL)
		return (0);

	if (h->prev != NULL)
	{
		for (i = 0; h->prev == NULL; i++)
			h = h->prev;
	}

	while (h != NULL)
	{
		num_nodo++;
		h = h->next;
	}

	return (num_nodo);
}
