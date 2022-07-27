#CasJobs functions

import SciServer
from SciServer import CasJobs     # Communicate between SciServer Compute and CasJobs
print('Imported SciServer modules')

import pandas                                # data analysis tools
import numpy as np                           # numerical tools
from datetime import datetime, timedelta     # date and timestamp tools
from pprint import pprint                    # print human-readable output
print('Imported other needed modules')


# PYTHON CONVENIENCE FUNCTIONS USEFUL FOR WORKING WITH CASJOBS

def tables_formatted(tables):   # better formatted printing of a tables dictionary (output of get_tables)
# Returns the following information about the tables in your MyDB (as a Python dictionary object):
### Size: size of the table (in kB)
### Name: the name of the table
### Rows: the number of rows the table contains
### Date: the date of the table's creation, as the number of 10-microsecond intervals elapsed 1 AD

    import pandas
    from datetime import datetime
    
    tables = sorted(tables, key=lambda k: k['Name']) # alphabetize by table name
    
    for thistable in tables:
        print('Table name:\t',thistable['Name'])
        print('Rows:\t\t {:,.0f}'.format(thistable['Rows']))
        print('Size (kB):\t {:,.0f} '.format(thistable['Size']))

        cjCreateDate = thistable['Date']
        createsec = cjCreateDate / 10000000  # Divide by 10 million to get seconds elapsed since 1 AD
        firstday = datetime(1, 1, 1, 0, 0)   # Save 1 AD as "firstday"
        created = firstday + timedelta(seconds=createsec)  # Get calendar date on which table was created     
        print('Created time:\t',created.strftime('%Y-%m-%d %H:%M:%S'))
        print('\n')
        

def jobDescriber(jobDescription):
    # Prints the results of the CasJobs job status functions in a human-readable manner
    # Input: the python dictionary returned by getJobStatus(jobId) or waitForJob(jobId)
    # Output: prints the dictionary to screen with readable formatting
    import pandas
    
    if (jobDescription["Status"] == 0):
        status_word = 'Ready'
    elif (jobDescription["Status"] == 1):
        status_word = 'Started'
    elif (jobDescription["Status"] == 2):
        status_word = 'Cancelling'
    elif (jobDescription["Status"] == 3):
        status_word = 'Cancelled'
    elif (jobDescription["Status"] == 4):
        status_word = 'Failed'
    elif (jobDescription["Status"] == 5):
        status_word = 'Finished'
    else:
        status_word = 'Status not found!!!!!!!!!'

    print('JobID: ', jobDescription['JobID'])
    print('Status: ', status_word, ' (', jobDescription["Status"],')')
    print('Target (context being searched): ', jobDescription['Target'])
    print('Message: ', jobDescription['Message'])
    print('Created_Table: ', jobDescription['Created_Table'])
    print('Rows: ', jobDescription['Rows'])
    wait = pandas.to_datetime(jobDescription['TimeStart']) - pandas.to_datetime(jobDescription['TimeSubmit'])
    duration = pandas.to_datetime(jobDescription['TimeEnd']) - pandas.to_datetime(jobDescription['TimeStart'])
    print('Wait time: ',wait.seconds,' seconds')
    print('Query duration: ',duration.seconds, 'seconds')
        
print('Created functions')