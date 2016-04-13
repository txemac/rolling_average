# Rolling average

A rolling average of a data series takes each N data points in a row and averages them, still showing change over time but in a smoothed way. For example the rolling averages (averaging over 3 points) of
 
[10, 10, 13, 16, 13, 13]

are

[11, 13, 14, 14].

Function that takes an array (and the length of the array if that’s useful) and a rolling average size, and returns another array with the rolling averages. For example

get_rolling_averages([10, 10, 13, 16, 13, 13], 3)

would return [11, 13, 14, 14].

If the request is invalid for any reason it can return an empty array or preferably raise some kind of error broadly explaining why.

# Run
To run unit test suite, install 'nose', eg. using 'pip': 

    pip install -r ./requirements.txt
    
Run tests:

    nosetests -v


# Author
Jose Bermudez

[www.josebermudez.co.uk](http://www.josebermudez.co.uk)

[info@josebermudez.co.uk](mailto: info@josebermudez.co.uk)