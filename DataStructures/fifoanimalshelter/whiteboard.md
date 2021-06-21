# Code Challenge Whiteboarding
## Problem Domain:

Create a class called AnimalShelter which holds only dogs and cats. The shelter operates using a first-in, first-out approach.
have the following methods:
enqueue(animal): adds animal to the shelter. animal can be either a dog or a cat object.
dequeue(pref): returns either a dog or a cat. If pref is not "dog" or "cat" then return null.


## Edge cases:
differant type of input , input is empty


## Visulization
input [cat1,cat2,cat3]
enqueue(dog)=>[cat1,cat2,cat3,dog]
dequeue(dog)=>return dog
## Big-O:
O(N) linear relation.

## Algortihm:
1.craete class call AnimalShelter
2 .make Queue for cat & dog
3.create method called enqueue that take animal as an argument and add it
4.create method called dequeue take an argument return either dog or cat according to to argument

## Pseudo Code
define AnimalShelter
make Queue for cat & dog
define enqueue function that take the name and the kind of animal
if the animal is cat or dog only will add the animal
define dequeue function if the input cat will retuen cat 
if input dog will return dog

## Code
```
    
    def enqueue(self, name, kind):
        if kind == 'cat':
            self.cat.enqueue(name)

        if kind == 'dog':
            self.dog.enqueue(name)
        
        else:
            return 'its possible for cat or dog only'


    def dequeue(self, kind=None):
        if kind == 'cat':
            return self.cat.dequeue()

        if kind == 'dog':
            return self.dog.dequeue()
       
        else:
            return 'you can just choose dog or cat'
```


## Verification
```


    def enqueue(self, name, kind):      name=sherazi    kind=cat
        if kind == 'cat':    .............this if is true and willl add it
            self.cat.enqueue(name)

        if kind == 'dog':
            self.dog.enqueue(name)
        
        else:
            return 'its possible for cat or dog only'


    def dequeue(self, kind=None): ... ........ kind=dog
        if kind == 'cat':
            return self.cat.dequeue()

        if kind == 'dog':
            return self.dog.dequeue() ..........this true statment
       
        else:
            return 'you can just choose dog or cat'
```