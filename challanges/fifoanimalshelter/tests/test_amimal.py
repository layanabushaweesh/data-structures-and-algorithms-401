from DataStructures.fifoanimalshelter.fifo_animal_shelter import  AnimalShelter



def test_enqueue():
    actual = []
    animals = AnimalShelter()
    animals.enqueue('sherazi', 'cat')
    animals.enqueue('pupi', 'dog')
    actual += [animals.dog.peek()]
    actual += [animals.cat.peek()]
    excepted = ['pupi', 'sherazi']
    assert actual == excepted


def test_enqueue_fail():
    animal = AnimalShelter()
    actual = animal.enqueue('white bear', 'bear')
    excepted = 'its possible for cat or dog only'
    assert actual == excepted



def test_dequeue_fail():
    animal = AnimalShelter()
    actual = animal.dequeue('buterflay')
    excepted = 'you can just choose dog or cat'
    assert actual == excepted