from linkedList import LinkedList
from reverse_list import reverse_list
from sort_list import sort_list

ll = LinkedList()

for val in [7, 3, 1, 9, 5, 3, 6, 2]:
    ll.insert_at_end(val)
print("Оригінальний:")
print(ll.print_list())

ll.head = sort_list(ll.head)
print("Відсортований:")
print(ll.print_list())

ll.head = reverse_list(ll.head)
print("Реверсований:")
print(ll.print_list())


