# CAPTAIN WILLIAM'S FORMAT FUNC's

This is a collection of functions used to format string files. 

string_format and paragraph_maker are both built around recieving 
strings without tabs or linebreaks, as from .JSON files or csv files 
and breaking them up to shape paragraphs. 

string_format and paragraph_maker can both make paragraphs. 

The difference between the two is that 
paragraph_maker adds linebreaks after every sentance, and
string_format adds linebreaks roughly at the the end of every nth 
character specified by the length parameter. 

This works well for GUI applications where you may have issues
where the text runs off the page. 
