from math import floor
from re import finditer

def string_format(string, length=50, paragraph_size=0,space_size=1):
    """
    About:
    Shapes a body of text to match within 80%+ of the
    given length. 
    Adds line breaks after every nth time the line length in a string
    has been met,
    provided that part of the string is a space.
    Also makes paragraphs that fit roughly within the specified length. 
    The function does not guarantee a paragraph after every nth sentance,
    but will try to approximate as best as possible.
    """
    string_length = len(string)
    ratio = string_length // length
    index_jump = floor(0.8 * length) 
    composite_string = ''
    nth_snippet = ''
    index_start = 0
    index_end_non_inclusive = 0
    DEFINITE_END = string_length - 1
    rotate = True
    space = False
    while rotate is True:
        for turn, rotation in enumerate(range(ratio)):
            index_start = index_end_non_inclusive
            index_end_non_inclusive += index_jump
            while string[index_end_non_inclusive] != " ":
                index_end_non_inclusive += 1
            if string[index_end_non_inclusive] == " ":
                nth_snippet = string[index_start:index_end_non_inclusive] # initialized nth_snippet
                #print(f"snippet: #{nth_snippet}#")
            try:
                if (turn + 1) % paragraph_size == 0:
                    space = True
            except ZeroDivisionError:
                pass
            if space == True and "." in nth_snippet[0:-1]:  # if its time for a space
                hold_this = ''
                period_index = nth_snippet.find(".")
                hold_this = nth_snippet[1:period_index + 1] + ("\n" * 2) + nth_snippet[period_index + 2:]
                #print(f"Hold:#{hold_this}#")
                nth_snippet = hold_this
                nth_snippet += ("\n") * space_size
                nth_snippet.lstrip()
                #print(f"Hold2:#{hold_this}#")
                composite_string += nth_snippet.lstrip()
                space = False
            else:
                nth_snippet += "\n"
                composite_string += nth_snippet.lstrip()

        # CONDITIONS FOR TAIL END #        
        nth_snippet = string[index_end_non_inclusive:DEFINITE_END + 1]  # end of string established

        length_of_final = len(nth_snippet) // 2
        while nth_snippet[length_of_final] != " ":
            length_of_final +=1
        if nth_snippet[length_of_final] == " ":
            hold_this = nth_snippet[1:length_of_final + 1] + "\n" + nth_snippet[length_of_final + 1:]  # split the last nth and add a breakline
            #print(f" hold final #{hold_this}#")
            nth_snippet = hold_this
            composite_string += nth_snippet.lstrip()
        #remainder = (DEFINITE_END - index_end_non_inclusive) 

        #print(f"nth snippet: {nth_snippet} index end: {index_end_non_inclusive} str length: {string_length}  def end: {DEFINITE_END}") # debug
        rotate = False
        return composite_string
    # TODO
    # the function has to account for spaces




def paragraph_maker(string, paragraph_size=3, space_size=1):
    """
    Info:
    Will write "copyright" style where each sentance is its own line. 
    There is a linebreak after every line.
    
    paragraph_size:
    Will seperate paragraphs after every nth line from paragraph_size.

    space_size:
    Determines the size of the linebreaks and of the space. 
    1 is default, 2 is double-spaced, ect. Must be an int.
    """
    default_pattern = r"\.\s?|\?\s?|!\s?" # space optional
    matches = finditer(default_pattern, string)
    start = 0
    end = 0
    split = False
    composite_string = ''
    for match_number, match in enumerate(matches):
        start = end
        if (match_number + 1) % paragraph_size == 0:  # check if every nth line
            split = True
        else:
            pass
        end = match.span()[1]   
        iter_string = string[start:end] # no need for +1 b/c  .span()[1] is already an overshoot of + 1
        if split == True:
            iter_string += ("\n" * 2) * space_size
            split = False
        else:
            iter_string += "\n" * space_size
        composite_string += iter_string
    return composite_string



