#!/usr/bin/env python

class Pets:
    """
    Class used to manage the pets info.

    Attributes:
        sold_pets (dictionary): The name of every sold pet ordered by its ID
    """

    def __init__(self, sold):
        """
        Initialize the Pets object.

        Args:
            sold (dictionary): A dictionary with all the sold pet names ordered by ID
        """
        self.sold_pets = sold

    def count_repeated_names(self):
        """
        Count how many times each pet name is repeated and print the result.

        Returns: A dictionary with the name of each pet and the times that this name repeated
        """
        repeated_names = {}
        for key in self.sold_pets:
            if self.sold_pets[key] in repeated_names.keys():
                repeated_names[self.sold_pets[key]] = repeated_names[self.sold_pets[key]] + 1
            else:
                repeated_names[self.sold_pets[key]] = 1
        return repeated_names