import pytest
from cyclic_fifo import StaticCyclicFifo, DynamicCyclicFifo


def test_static_can_work_correctly():
    fifo = StaticCyclicFifo(3)
    fifo.push(1)
    fifo.push(2)
    fifo.push(3)
    assert fifo.pop() == 1
    assert fifo.pop() == 2
    assert fifo.pop() == 3


def test_static_raise_overflow_error():
    with pytest.raises(OverflowError):
        fifo = StaticCyclicFifo(2)
        fifo.push(1)
        fifo.push(2)
        fifo.push(3)


def test_dynamic_work_correctly():
    fifo = DynamicCyclicFifo()
    fifo.push(1)
    fifo.push(2)
    fifo.push(3)
    assert fifo.pop() == 1
    assert fifo.pop() == 2
    assert fifo.pop() == 3


def test_dynamic_ensure_cap_correctly():
    fifo = DynamicCyclicFifo()
    fifo.push(1)
    fifo.push(2)
    fifo.push(3)
    assert 4 == fifo.capacity


def test_dynamic_decr_cap_correctly():
    fifo = DynamicCyclicFifo()
    fifo.push(1)
    fifo.push(2)
    fifo.push(3)
    fifo.pop()
    fifo.pop()
    assert 1 == fifo.capacity
