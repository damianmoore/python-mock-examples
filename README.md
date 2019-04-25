# Python Mock Examples

These are a few examples of my most common uses of Mock while doing TDD. There are many other things that Mock can do, and I will add more examples when I think it's worthwhile. Mainly this is meant to help get the maximum benefit in the minimum amount of time.

You should be able to clone and run any of the scripts beginning `test_` using the Python 3 interpreter and you don't need any dependencies.


## Patching

I focus on patching as I mainly need to prevent a function/method from making a call and it is likely to be hidden behind several other layers of modules/classes etc.

You should first look at [`example_class.py`](example_class.py) as it presents a very simple class that simulates fetching and storing results from an API. It has a `list` instance variable called `results`, has a method `fetch_results()` for calling the API and a method `get_results()` for returning any results that were previously fetched.


### [Test Patch Object Return Value](test_patch_object_return_value.py)

This shows how to make a method of an object return a specific value. This value can be a JSON-formatted string pretending to be the result of an API response etc. Examples in decorator and context manager form are provided.


### [Test Patch Object Method](test_patch_object_method.py)

This shows how to replace a method of object with a new one. This method has access to instance variables through `self`. Examples in decorator and context manager form are provided.
