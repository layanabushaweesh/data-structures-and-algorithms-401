from DataStructures.StacksAndQueues.sandq.stachandqueue import Stack , Queue

from inspect import stack
import pytest


# stack tests

def test_1(stack_vals):  
    actual = stack_vals.peek()
    expected = 4
    assert actual == expected

def test_multiple_push(stack_vals):  
    stack_vals.push('L')
    actual = stack_vals.peek()
    expected = 'L'
    assert actual == expected

def test_pop(stack_vals):  
    stack_vals.pop()
    actual = stack_vals.peek()
    expected = 3
    assert actual == expected

def test_multiple_pop(stack_vals):  
    stack_vals.pop()
    stack_vals.pop()
    actual = stack_vals.pop()
    expected = 1
    assert actual == expected

def test_pop_raise_empty():  
    stack = Stack()
    actual = stack.pop()
    expected = 'empty stack'
    assert actual == expected

def test_peek_next_item(stack_vals):  
    actual = stack_vals.peek()
    expected = 4
    assert actual == expected

def test_is_empty_stack():  
    stack = Stack()
    actual = stack.is_empty()
    expected = True
    assert actual == expected




@pytest.fixture
def stack_vals():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    return stack


# Queue test

def test_enqueue(queue_valus):  
    assert queue_valus.front.value == 'layan'

def test_enqueue_1(queue_valus):  
    assert queue_valus.rear.value == 'leen'

def test_multiple_enqueue(queue_valus):  
    queue_valus.enqueue('lulu')
    assert queue_valus.rear.value == 'lulu'
   
def test_dequeue(queue_valus): 
    # remove all value 
    actual = queue_valus.dequeue()
    expected = None
    assert actual == expected

def test_queue_peek(queue_valus):  
    actual = queue_valus.peek()
    expected = 'layan'
    assert actual == expected

def test_dequeue_raise_empty(): 
    queue = Queue()
    actual = queue.dequeue()
    expected = 'empty queue'
    assert actual == expected

def test_empty_queue():  
    queue = Queue()
    actual = queue.is_empty()
    expected = True
    assert actual == expected

 



@pytest.fixture
def queue_valus():
    queue = Queue()
    queue.enqueue('layan')
    queue.enqueue('lelian')
    queue.enqueue('leen')
 
    return queue