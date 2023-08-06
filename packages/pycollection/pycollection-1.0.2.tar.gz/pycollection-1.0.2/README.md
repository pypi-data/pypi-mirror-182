# pycollection

pycollection is an amazing library that allows you to iterate through a list, but it returns a transformed item. It has a lot of methods to interact with the collection. It works similar than laravel collections. Current version is 1.0.2. 

## Basic usage
    
    class NumberCollection(Collection):

        def item(self, item):
            return Number(item)


    class Number:

        def __init__(self, item):
            self._item = item

        def value(self):
            return self._item
        
        def squared(self):
            return self._item * self._item


    numbers = NumberCollection([1,2,3,4,5])


    for number in numbers:
        print(number.squared())

    # output
    # > 1
    # > 4
    # > 9
    # > 16
    # > 25

As you can see, it allows for an easy-to-read syntax for navigating between lists and their elements, since you can provide new functionality to both.

## Available methods

| methods   | 
|------------|
| count       |
| json         |
| find         |
| where      |
| item        |
| first       |
| append    |
| items      |
