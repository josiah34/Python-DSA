import pytest
from linkedlist import LinkedList
from linkedlist import LinkedList


@pytest.fixture
def linked_list():
    # Create an instance of LinkedList with initial value 1
    return LinkedList(1)


def test_append(linked_list):
    # Append a value to the linked list
    linked_list.append(2)

    # Check if the length is updated correctly
    assert linked_list.length == 2

    # Check if the appended value is at the tail
    assert linked_list.tail.value == 2


def test_pop(linked_list):
    # Pop the last value from the linked list
    popped_node = linked_list.pop()

    # Check if the popped value is correct
    assert popped_node.value == 1

    # Check if the length is updated correctly
    assert linked_list.length == 0

    # Check if the head and tail are None after popping the last value
    assert linked_list.head is None
    assert linked_list.tail is None


def test_prepend(linked_list):
    # Prepend a value to the linked list
    linked_list.prepend(0)

    # Check if the length is updated correctly
    assert linked_list.length == 2

    # Check if the prepended value is at the head
    assert linked_list.head.value == 0


def test_pop_first(linked_list):
    # Pop the first value from the linked list
    linked_list.pop_first()

    # Check if the length is updated correctly
    assert linked_list.length == 0

    # Check if the head and tail are None after popping the first value
    assert linked_list.head is None
    assert linked_list.tail is None


def test_get(linked_list):
    # Get the value at index 0
    test_value = linked_list.get(0)

    # Check if the returned value is correct
    assert test_value.value == 1


def test_set(linked_list):
    # Set the value at index 0 to 2
    test_value = linked_list.set(0, 2)

    # Check if the value at index 0 is updated correctly
    assert test_value.value == 2


def test_insert(linked_list):
    # Insert a value at index 1
    linked_list.insert(1, 2)

    # Check if the length is updated correctly
    assert linked_list.length == 2

    # Check if the value is inserted at the correct position
    assert linked_list.get(1).value == 2


def test_reverse(linked_list):
    # Append a value to the linked list
    linked_list.append(2)

    # Reverse the linked list
    linked_list.reverse()

    # Check if the length is updated correctly
    assert linked_list.length == 2

    # Check if the head and tail are updated correctly
    assert linked_list.head.value == 2
    assert linked_list.tail.value == 1


def test_remove(linked_list):
    # Append a value to the linked list
    linked_list.append(2)

    # Remove the value at index 1
    linked_list.remove(1)

    # Check if the length is updated correctly
    assert linked_list.length == 1

    # Check if the value is removed from the linked list
    assert linked_list.get(1) is None