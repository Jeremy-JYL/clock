# clock
A simple customise clock

# Config

START: Can be any string.
Example: `Hello World\n {Currentime}\n {END}`

CLOCK_FORMAT: Is just the dateime config code
Example: `Hello World \n Monday\n {END}`

|Code |Description |Example |
| --- | ---| ---|
%Y|	Year with century as a decimal number.|	2024
%m|	Month as a zero-padded decimal number.|	01
%B|	Full month name.|	January
%b|	Abbreviated month name.|	Jan
%d|	Day of the month as a zero-padded decimal number.|	01
%A|	Full weekday name.|	Monday
%a|	Abbreviated weekday name.|	Mon
%H|	Hour (24-hour clock) as a zero-padded decimal number.|	23
%I|	Hour (12-hour clock) as a zero-padded decimal number.|	11
%p|	Locale’s equivalent of either AM or PM.|	PM
%M|	Minute as a zero-padded decimal number.|	59
%S|	Second as a zero-padded decimal number.|	59
%f|	Microsecond as a decimal number, zero-padded on the left.|	000000
%Z|	Time zone name (empty string if the object is naive).|	UTC
%z|	UTC offset in the form ±HHMM[SS[.ffffff]] (empty string if the object is naive).|	+0900

END: Can be any string
Example: `Hello World \n Monday\n Have a good day!`
