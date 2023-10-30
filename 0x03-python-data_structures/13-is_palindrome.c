#include <stdio.h>
#include <stdlib.h>
#include "lists.h"


/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int i, j, n = 0;

	if (!(*head))
		return (1);
	temp = *head;
	while (temp != NULL)
	{
		temp = temp->next;
		n++;
	temp = *head;
	int arr[n];

	j = n;
	n = 0;
	while (temp != NULL)
	{
		arr[n] = temp->n;
		temp = temp->next;
	n++;
	}
	n--;
	for (i = 0; i < j; i++)
	{
		if (arr[i] != arr[n])
			return (0);
		n--;
	}
	return (1);
}
