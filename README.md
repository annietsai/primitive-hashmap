Primitive HashMap
=================

What is it?
-----------

The Primitive HashMap is a fixed-size hashmap that, using only primitive types,
associates string keys with arbitrary data object references.

Implementation
--------------

1. The maximum number of items that can be added to the hashmap is fixed by the
constructor, which means the hashmap cannot be resized once created.
2. There is no error handling for overloading, so if the user tries to set more
items than the hashmap size, the set function will return False, but no error
message is displayed.
3. Methods:
	* **PrimitiveHashMap constructor(size)**: takes in an integer and returns an 
	instance of the class with a fixed amount of space.
	* **boolean set(key, value)**: stores the given string key and object value 
	pair in the hashmap. Returns true if there is enough allocated space for the 
	object, false if not.
	* **get(key)**: return the object associated with the given string key, or 
	None if it does not exist.
	* **delete(key)**: deletes the object associated with the given string key, 
	returning the value it maps to on success or None if the key does not exist.
	* **float load()**: returns a float value representing the proportion of 
	items in the hashmap vs. the size of the hashmap. Since the size of the data 
	structure is fixed, this value should never be greater than 1.

Usage
-----

After downloading the file from Github, run the program interactively in the 
directory in which the file is saved using:  
    `$ python -i primitiveHashMap.py`  

Run tests using:
	`$ python -i primitiveHashMapTests.py`

Authors
-------

Annie Tsai

