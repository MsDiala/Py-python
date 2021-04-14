# Serialization
Data serialization is the concept of converting structured data into a format that allows it to be shared or stored in such a way that its original structure to be recovered. In some cases, the secondary intention of data serialization is to minimize the size of the serialized data which then minimizes disk space or bandwidth requirements.

## Pickle
The native data serialization module for Python is called `Pickle`.
```python
import pickle

#Here's an example dict
grades = { 'Alice': 89, 'Bob': 72, 'Charles': 87 }

#Use dumps to convert the object to a serialized string
serial_grades = pickle.dumps( grades )

#Use loads to de-serialize an object
received_grades = pickle.loads( serial_grades )
print received_grades
```
output
```python
{'Bob': 72, 'Charles': 87, 'Alice': 89}
```
