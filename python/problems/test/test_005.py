'''
find how many flurries does n-snowflake contain
1-snowflake has 1 flurry
2-snowflake is 1-snowflake with flurries to the right, left, top and bottom of it
e.g.
     *     - 1-snowflake

     *   
   * * *   - 2-snowflake
     *

     *
   * * *
 * * * * * - 3-snowflake
   * * *
     *
'''
from p005_n_snowflake_r import n_snowflake

def test_1():
    assert n_snowflake(1) == 1

def test_2():
    assert n_snowflake(2) == 5

def test_3():
    assert n_snowflake(3) == 13
