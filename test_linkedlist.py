from unittest import TestCase, main
from LinkedList import LinkedList

class TestLinked(TestCase):
    
    def test_append(self):
        ll = LinkedList('monday')
        ll.append_node('tuesday')
        tail_node = ll.get_tail()
        tail_value = tail.node.value
        self.assertEqual(tail_value, 'tuesday')
        ll.append_node('wednesday')
        self.assertEqual(ll.get_tail().value, 'wednesday')
        
    def test_get_tail(self):
        pass

if __name__ == '__main__':
    main()