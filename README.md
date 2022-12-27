# Hampshire-College-Course-Search
Parses HTML to show info about new classes.
This uses Regex and Beautiful Soup.

I wrote this way back in 2020 when I first started learning Python and was annoyed with refreshing Hampshire College's course directory every day to see which new classes were released. There were new classes being released everyday and I didn't want to manually go through all the classes to see which ones were new. I parsed the course directory's HTML to show what was new every day, as well information such as total spots in classes.

To run these, you have to go to Hampshire College's directory of classes webpage first and CTRL-S save the page as an HTML file.

fys.py:
This python script prompts you for the file name of your HTML file and prints out:
- Number of first years in First Year Seminars (FYSs)
- Total number of sign-ups for all classes
- Total number of classes
- Total remaining spaces in classes

classDiff.py:
This asks you to input two HTML files (from two different days or times) and will compare them, printing out any new classes that have been added/deleted/had their titles changed.


