# Hashtables
<!-- Short summary or background information -->
Hashtables are a data structure that utilize key value pairs.
>This means every Node or Bucket has both a key, and a value.

* The basic idea of a hashtable is the ability to store the key into this data structure,
and quickly retrieve the value. 

* This is done through what we call a hash. A hash is the ability to encode the key that will eventually map to a specific location in the data structure that we can look at directly to retrieve the value.


## Challenge
<!-- Description of the challenge -->
Challenge Type: New Implementation of Hashtable

Features
 1. add 
 2. contains
 3. hash
 4. get
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Time complexity: O(1).
Space complexity: O(n).
## API
<!-- Description of each method publicly available in each of your hashtable -->
* add: This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

* get: Returns a value associated with that key in the table if exist

* contains: Returns a boolean, indicating if the key exists in the table already.

* hash: Returns the Index in the collection for that key