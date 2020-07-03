# Statistics Calculator
IS 601850 - Team Project 2 - Stats Calculator Group

## Calculator Diagram
* Calculator Object
    * Properties
        * Result
    * Methods
        * Add -> Calls Addition static method from math operations
        * Subtract -> Calls Subtraction static method from math operations
        * Multiply -> Calls Multiply static method from math operations
        * Divide -> Calls Divide static method from math operations
        * Squaring -> Calls Square static method from math operations
        * Squarerooting -> Calls Squareroot static method from math operations
    * Math Operations Static Class
        * Methods
            * Addition -> Calls addition class method of sum
            * Subtraction -> Calls subtraction class method of difference
            * Multiplication -> Calls multiplication class method of product
            * Division -> Calls division class method of quotient
            * Squaring -> Calls squaring class method of square
            * Squarerooting -> Calls squarerooting class method of square root
    * Operation Class(es)
        * Addition
            * Methods
                * Add two numbers to each other
                * Add list of numbers to each other
        * Subtraction
            * Methods
                * Subtract one number from another
        * Multiplication
            * Methods
                * Multiply two numbers by each other
        * Division
            * Methods
                * Divide one number by another
        * Squaring
            * Methods
                * Multiply one number by itself
        * Squarerooting
            * Methods
                * Use .sqrt function to find the square root of a number
* Statistics Object 
	* Properties	
		* Result
	* Methods 
	    * get_mean
	        * calls mean static method
	    * get_median
	        * calls median static method
	    * get_mode
	        * calls mode static method
	    * get_simple sample
	        * call sample static method
	    * get_confidence_interval
	        * calls confidence interval
* Task breakdown

    The starting point will be the orignal Calculator. This will be extended to create the Statistics class object.
    
* Create statistics methods
    * get_mean
        * get_mean method takes a sample data and return the mean
        * formula : _sum of terms / number of terms_
        * usage: get_mean(data) 
        * sample result:
        
        ![mean](/images/mean.PNG)  
    * get_median 
       * get_median method takes a sample data set and returns the median
       * formula: 
       * data is ordered
       * for an odd amount of values it is the middle value
       * For a data set with an even amount of values it is the average of the middle tow numbers
       * usage get_median(data)
       * sample result:
       
       ![median](/images/median.PNG) 
        
	       
	                
	
 
### To Do List
| | To Do | In Progress | Review | Done |
|---|---|---|---|---|
| DOUG | | | | Upload original calculator files |
| DOUG | Develop methods/tests for Median | | |
| DOUG | Develop methods/tests for Mode | | |
| DOUG | Develop methods/tests for Variance | | |
| DOUG | Develop methods/tests for Standard Deviation | | |
| DOUG | Develop methods/tests for Z-Score | | |
| DOUG | | | Mean Method |
| DOUG | | | Mean Unit Test
| MIKE | | | Random Number Generator |
| MIKE | | | Random Gen Unit Test |
| MIKE | | | Simple Random Sampling|
| MIKE | | |Confidence Interval |
| MIKE |Margin of Error | | |
| MIKE |Cochran’s Sample Size Formula | | |
| MIKE |Find a Sample Size Given a Confidence Interval and Width | | |


