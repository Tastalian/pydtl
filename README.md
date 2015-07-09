# PyDTL — Decision Tree Learning in Python

PyDTL is a simple Python library for Decision Tree Learning, Bagging and Random
Forests. I worte it during a research internship at INRIA. It has not been
updated since May 2011.

## Example

The `RandomForest` constructor needs a training set and a target attribute. The
training set is given as a `pydtl.LocalTable` object, which you can read from
an SQLite database or a CSV file. The repository contains an example database
`sample.sqlite` with the following training set:

```
CREATE TABLE events(
    clustering REAL, 
    completion REAL, 
    mean_path_length REAL, 
    cards_per_day REAL, 
    mean_neigh_deg REAL, 
    degree REAL, 
    mean_neigh_act REAL, 
    neigh_act_dev REAL, 
    seen_inrate REAL, 
    activity REAL, 
    base_activity REAL, 
    `player_id` INT NOT NULL)
```

We will create a random forest learning the attribute `activity` from the other
attributes of the training set:

```
import pydtl

db = pydtl.SQLiteDB('sample.sqlite')
table = db.dump_table('events')
forest = pydtl.RandomForest(table, target='activity')
```

To grow the forest, call the `grow_trees()` method. If you have `pygraphviz`
installed you can see the result using draw(), or print it otherwise:

```
forest.grow_trees(42)

try:
    forest.draw()
except ImportError:
    print forest
```

Finally, you can call the forest's `predict()` function to predict the target
attribute from a new instance.  Let us compute the Mean Square Error of the
forest's predictions over a small sample set:

```
square_errors = []
samples = table.sample_rows(42)
for inst in samples:
    y_pred = forest.predict(inst)
    y_real = inst['activity']
    square_errors.append((y_pred - y_real)**2)
mse = sum(square_errors) / len(square_errors)
print "Mean Square Error: %.3f" % mse
```
