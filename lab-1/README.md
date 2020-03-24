**General Directions:** 
1. Run the server. 
2. Wait for the notification that says the server is ready. “The server is ready!” for TCP and “IP Address:  XXX.XXX.X.XX The server is ready!”)
3. Run the related client. 
4. Input the appropriate text file that contains the test cases. The test cases should be separated by commas. 
5. Once complete, enter “exit” in order to end.  
6. You will either receive a That’s all”, “Received invalid values. Please try again.” , or “Exit” depending on what you will do. 

## TCP Test Cases
### From the sample test case given by the assignment. 
#### Server Output
```
Received the following: '2000,2019,2020,2021,2022,2024,2100'
Year 2000 is a leap year!
Year 2019 is not a leap year!
Year 2020 is a leap year!
Year 2021 is not a leap year!
Year 2022 is not a leap year!
Year 2024 is a leap year!
Year 2100 is not a leap year!
Success. Send the results back to the client!
```
#### Client Output
```
Enter a text file containing the test cases. Type exit to close: tc_sample.txt
Received from server:
That's all
```
### Test cases where all the years are non-leap years. 
#### Server Output
```
Received the following: '2002,2007,2015,2011,2017,1997,1995,1847'
Year 2002 is not a leap year!
Year 2007 is not a leap year!
Year 2015 is not a leap year!
Year 2011 is not a leap year!
Year 2017 is not a leap year!
Year 1997 is not a leap year!
Year 1995 is not a leap year!
Year 1847 is not a leap year!
Success. Send the results back to the client!
```
#### Client Output
```
Enter a text file containing the test cases. Type exit to close:  tc_no_leaps.txt
Received from server:
That's all
```
### Test cases where all the years are leap years. 
#### Server Output
```
Received the following: '2000,2004,2008,2012,2016,1996,1992,1904'
Year 2000 is a leap year!
Year 2004 is a leap year!
Year 2008 is a leap year!
Year 2012 is a leap year!
Year 2016 is a leap year!
Year 1996 is a leap year!
Year 1992 is a leap year!
Year 1904 is a leap year!

Success. Send the results back to the client!
```
#### Client Output
```
Enter a text file containing the test cases. Type exit to close: tc_all_leaps.txt
Received from server:
That's all
```
### Test case where all the inputs are letters, not integers. 
#### Server Output
```
Received the following: 'a,b,c,d,e,f,g,h,i,j,k,l'
```
#### Client Output
```
Enter a text file containing the test cases. Type exit to close: tc_all_letters.txt
Received from server:
Received invalid values. Please try again.
```
### Test case where one element is not an integer. 
#### Server Output
```
Received the following: '2000,a,2001,2011,2012,2014'
```
#### Client Output
```
Enter a text file containing the test cases. Type exit to close: tc_hidden_letter.txt
Received from server:
Received invalid values. Please try again.
```
### Exit Time
#### Server Output
```
The client wants to exit
```
#### Client Output
```
Enter a text file containing the test cases. Type exit to close: exit
Received from server:
Exit
```
## UDP Test Cases
### From the sample test case given by the assignment. 
#### Server Output
```
Received the following: '2000,2019,2020,2021,2022,2024,2100'
Year 2000 is a leap year!
Year 2019 is not a leap year!
Year 2020 is a leap year!
Year 2021 is not a leap year!
Year 2022 is not a leap year!
Year 2024 is a leap year!
Year 2100 is not a leap year!
Success. Send the results back to the client!
```
#### Client Output
```
Enter a text file containing the test cases. Type exit to close: tc_sample.txt
Received from server:
That's all
```
### Test cases where all the years are non-leap years. 
#### Server Output
```
Received the following: '2002,2007,2015,2011,2017,1997,1995,1847'
Year 2002 is not a leap year!
Year 2007 is not a leap year!
Year 2015 is not a leap year!
Year 2011 is not a leap year!
Year 2017 is not a leap year!
Year 1997 is not a leap year!
Year 1995 is not a leap year!
Year 1847 is not a leap year!
Success. Send the results back to the client!
```
#### Client Output
```
Enter a text file containing the test cases. Type exit to close:  tc_no_leaps.txt
Received from server:
That's all
```
### Test cases where all the years are leap years. 
#### Server Output
```
Received the following: '2000,2004,2008,2012,2016,1996,1992,1904'
Year 2000 is a leap year!
Year 2004 is a leap year!
Year 2008 is a leap year!
Year 2012 is a leap year!
Year 2016 is a leap year!
Year 1996 is a leap year!
Year 1992 is a leap year!
Year 1904 is a leap year!

Success. Send the results back to the client!
```
#### Client Output
```
Enter a text file containing the test cases. Type exit to close: tc_all_leaps.txt
Received from server:
That's all
```
### Test case where all the inputs are letters, not integers. 
#### Server Output
```
Received the following: 'a,b,c,d,e,f,g,h,i,j,k,l'
```
#### Client Output
```
Enter a text file containing the test cases. Type exit to close: tc_all_letters.txt
Received from server:
Received invalid values. Please try again.
```
### Test case where one element is not an integer. 
#### Server Output
```
Received the following: '2000,a,2001,2011,2012,2014'
```
#### Client Output
```
Enter a text file containing the test cases. Type exit to close: tc_hidden_letter.txt
Received from server:
Received invalid values. Please try again.
```
### Exit Time
#### Server Output
```
The client wants to exit
```
#### Client Output
```
Enter a text file containing the test cases. Type exit to close: exit
Received from server:
Exit
```