#include <stdio.h>

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: a variable of struct listint_t
 * Return: returns 0 for no cycle or 1 for cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	if (list == NULL || list->next == NULL)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
