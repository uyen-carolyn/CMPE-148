**General Directions:** 
Run the server. Wait for the notification that says the server is ready (“Server ready!” or “IP Address:  192.168.1.11 Server ready!”)
Run the related client. 
Input your values, separating them with a comma. The values must be an integer that represents a year in the calendar. 
You will either receive a That’s all”, “Received invalid values. Please try again.” , or “Exit” depending on what you will do. 
Once complete, enter “exit” in order to end.  

## TCP Test Cases
### 2000,2019,2020,2021,2022,2024,2100
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
Enter a set of years with a space in between each year. Type exit to close: 2000,2019,2020,2021,2022,2024,2100
Received from server:
That's all
```
### 2002,2007,2015,2011
#### Server Output
```
Received the following: '2002,2007,2015,2011'
Year 2002 is not a leap year!
Year 2007 is not a leap year!
Year 2015 is not a leap year!
Year 2011 is not a leap year!
Success. Send the results back to the client!
```
#### Client Output
```
Enter a set of years with a space in between each year. Type exit to close: 2002,2007,2015,2011
Received from server:
That's all
```
### 2000,2004,2008,2012,2016
#### Server Output
```
Received the following: '2000,2004,2008,2012,2016'
Year 2000 is a leap year!
Year 2004 is a leap year!
Year 2008 is a leap year!
Year 2012 is a leap year!
Year 2016 is a leap year!
Success. Send the results back to the client!
```
#### Client Output
```
Enter a set of years with a space in between each year. Type exit to close: 2000,2004,2008,2012,2016
Received from server:
That's all
```
### a,b,c,d
#### Server Output
```
Received the following: 'a,b,c,d'
```
#### Client Output
```
Enter a set of years with a space in between each year. Type exit to close: a,b,c,d
Received from server:
Received invalid values. Please try again.
```
### 2000,a,2001
#### Server Output
```
Received the following: '2000,a,2001'
```
#### Client Output
```
Enter a set of years with a space in between each year. Type exit to close: 2000,a,2001
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
Enter a set of years with a space in between each year. Type exit to close: exit
Received from server:
Exit
```
## UDP Test Cases
### 2000,2019,2020,2021,2022,2024,2100
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
Enter a set of years with a space in between each year. Type exit to close: 2000,2019,2020,2021,2022,2024,2100
Received from server:
That's all
```
### 2002,2007,2015,2011
#### Server Output
```
Received the following: '2002,2007,2015,2011'
Year 2002 is not a leap year!
Year 2007 is not a leap year!
Year 2015 is not a leap year!
Year 2011 is not a leap year!
Success. Send the results back to the client!
```
#### Client Output
```
Enter a set of years with a space in between each year. Type exit to close: 2002,2007,2015,2011
Received from server:
That's all
```
### 2000,2004,2008,2012,2016,1996,1992
#### Server Output
```
Received the following: '2000,2004,2008,2012,2016,1996,1992'
Year 2000 is a leap year!
Year 2004 is a leap year!
Year 2008 is a leap year!
Year 2012 is a leap year!
Year 2016 is a leap year!
Year 1996 is a leap year!
Year 1992 is a leap year!
Success. Send the results back to the client!
```
#### Client Output
```
Enter a set of years with a space in between each year. Type exit to close: 2000,2004,2008,2012,2016, 1996,1992
Received from server:
That's all
```
### a,b,c,d
#### Server Output
```
Received the following: 'a,b,c,d,e,f,g,h,i,j,k'
```
#### Client Output
```
Enter a set of years with a comma in between each year. Type exit to close: a,b,c,d,e,f,g,h,i,j,k
Received from server:
Invalid values. Please try again.
```
### 2000,a,2001
#### Server Output
```
Received the following: '2000,a,2001'
```
#### Client Output
```
Enter a set of years with a space in between each year. Type exit to close: 2000,a,2001
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
Enter a set of years with a space in between each year. Type exit to close: exit
Received from server:
Exit
```