# Quorum Challenge

### Deliverables

You will be provided with a list of legislators, bills, votes, and vote results as specified above. You’ll be asked to answer the following questions:
1. For every legislator in the dataset,how many bills did the legislator support(voted for the bill)? How many bills did the legislator oppose?
2. For every bill in the data set,how many legislators supported the bill?How many legislators opposed the bill? Who was the primary sponsor of the bill?


### Questions

1. Discuss your solution’s time complexity. What tradeoffs did you make?

Answer: In this solution I've used the dictionary as my main data structure to search and combine data to create my responses. Using dictionary the time complexity 
is O(i), once I have the key. But of course I needed to transform my list in dictionary which changed the time complexity to O(n) (linear). I prefered to transform csv data in list instead mapping directly in dictionary in the csv_reader, to me gain more flexibility and transform in dict on demand.


2. How would you change your solution to account for future columns that might be requested, such as “Bill Voted On Date” or “Co-Sponsors”?

Answer: Just adding a new property in the correct domain model class, the Csv_Reader has the logic using generic approach (TypeVar) to identify the object class
and map to the correct type.

```
Type = TypeVar("Type")

....
obj = type(*row)
data_obj.append(obj)

```

3. How would you change your solution if instead of receiving CSVs of data, you were given a list of legislators or bills that you should generate a CSV for?

Answer: It will be easier by the way, it was not necessary to transform csv in list as I did, just working with this list and following the same business logic.

4. How long did you spend working on the assignment?
Answer: 2 hours


### Usage

To run this project is pretty simple. Navigate to root path and run the following command


```
python main.py
```
