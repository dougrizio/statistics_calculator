![Travis CI badge](https://travis-ci.com/dougrizio/statistics_calculator.svg?branch=master)
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
	    *get_variance
	        * calls variance static method
	    *get_standard_deviation
	        * calls standard_deviation static method
	    *get_zscore
	        * calls zscore static method
	    * get_simple sample
	        * call sample static method
	    * get_confidence_interval
	        * calls confidence interval
# Task breakdown

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
       * usage: get_median(data)
       * sample result:
       
        ![median](/images/median.PNG) 
        
    * get_mode
        * get_mode calculates the mode of a data set
        * the mode is the value that appears most often in a given data set
        * usage: get_mode(data)
        * sample result: 
        
        ![mode](/images/mode.PNG) 
        
    * get_variance
        * get_variance calculates the average of the squared differences from the mean of a set
        * calculate the mean of the set
        * calculate the difference between the mean and each number in the set
        * create a list of differences
        * square each difference
        * create a list of squares
        * calculate the mean of those squares
        * sample result:
        
        ![variance](/images/variance.PNG) 
        
    * get_standard_deviation
        * get_variance calculates the amount of variation in a set of values relative to the mean
        * calculate the variance of the set
        * calculate the square root of the variance
        * sample result:
        
        ![standard_deviation](/images/stan_dev.PNG) 
        
    * get_zscore
        * get_zscore calculates the number of standard deviations by which the value of the raw score is above or below the mean value of what is being measured
        * declare the raw score of the set
        * calculate the mean of the set
        * calculate the standard deviation of the set
        * subtract the mean from the raw score
        * divide the standard deviation from the quotient
        * sample result:
        
        ![zscore](/images/zscores.PNG)
        
    * get_simple sample
       * get_simple_sample takes a data set and the amount of choices needed as input
       * it calls the simple_sample utility static method
         * This in turn calls the n_items_no_seed from the RandomGenerators.py module
            THis can be called with or with out a seed value
       * usage: get_sample(data, number_of_choices)
            * example uses a sample data set with 3 choices requested      
       * The returned value is a pseudo-random selection based on the number of choices provided           
       
       ![simple_sample](/images/simple_sample.PNG)
       
    * get_confidence_interval
      * requets the confidence interval for a given data set
        * This assumes the standard deviation is known or calcualted
        * T_score or Z_score is known or calculated.
        * usage: get_confidence_interval(data)
        * sample results assumes a confidence score of .95
        
      ![confidence interval](/images/confidence_interval.PNG)
      
* Create random generator static utility methods
    * RandomGenerators.py
        * random_seed 
            * create a random number based on parameters
                * seed value - can generate a value with wor without a seed
                * decimal - determines whether generated number should be an integer or a float.
                * start - starting value range
                * stop - ending value range
                * step - the interval between numbers 
            * usage: random_seed(seed = None, decimal = 1, start = 0, stop = 100, step = 1)
                * generates a float value with no seed with a range of 0-99
            * result:
            
            ![random_seed](/images/random_seed.PNG)
        
        * list generator
            * creates a list of random values based on parameters
                * seed value - can generate a value with wor without a seed
                * decimal - determines whether generated number should be an integer or a float.
                * start - starting value range
                * stop - ending value range
            * usage: list_generator(seed, decimal = 1, start = 0, stop = 100)
            * result: 
            
            ![list_generator](/images/list_generator.PNG)
            
	    * random_item
	        * chooses a random selected value from a data set.
	        * usage: random_item(data)
	        * return a pseudo-random value
	        * result:
	        
	        ![random item](/images/random_choice.PNG)
	    * n_items_no_seed
	        * returns a number of choices based on passed in attribute from calling function
	        * can be used with or without a seed.
	        * usage: n_items_no_seed(test_list, sample_size, seed = None)
	            * test_list can be passed in or generated 
	            * sample_size is the number of choices requested
	            * seed value is depends on whether or not a seed value is requested or needed
	                * no seed is default value
	        * result:
	        
	        ![n_item_no_seed](/images/n_items_no_seed.PNG)
	    * get_margin_of_error
	        * returns the margin of error given a critical value and standard error
	        * calls wrapped function margin_of_error
	        * margin_of_error calls muliply function from Calculator super class
	        * ME = critical value x standard error
	        * usage get_margin_of_error(crit_value, standard_error)
	        * result:
	        
	        ![margin_of_error](/images/me.PNG)
	    * get_cochrans_sample
	        * returns sample values based on Cochran's sampling formula
	        * Uses population size, confidence level, margin of error, and target proportion
	        * usage get_cochrans_sample(self, poplulation_sample, confidence_level, margin of error, target_proportion)
	        * result:
	        
	        ![Cochran's](/images/cochrans.PNG) 
	    * get_sample_ci_width
	        * returns a sample size when given the confidence level and width
	        * uses confidence interval function 
	        * usage sample_CI_width(confidence_lvl, width)
	        * result: 
	        
	        ![sample ci w/ width](/images/sample_CI_width.PNG)
	        
	        
	        
 	
 
### To Do List
| | To Do | In Progress | Review | Done |
|---|---|---|---|---|
| DOUG | | | | Upload original calculator files |
| DOUG | | | | Mean |
| DOUG | | | | Median |
| DOUG | | | | Mode |
| DOUG | | | | Variance |
| DOUG | | | | Standard Deviation |
| DOUG | | | | Z-Score |
| MIKE | | | | Random Number Generator |
| MIKE | | | | Random Gen Unit Test |
| MIKE | | | | Simple Random Sampling|
| MIKE | | | | Confidence Interval |
| MIKE | | | | Margin of Error |
| MIKE | | | | Cochran’s Sample Size Formula |
| MIKE | |  | | Find a Sample Size Given a Confidence Interval and Width |


