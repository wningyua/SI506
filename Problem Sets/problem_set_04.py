# PROBLEM SET 04

# PROBLEM 1 (10 points)
# Encode the following key-value pairs containing information about William Shakespeare
# into a dictionary object. Name the dictionary <shakespeare>.

# KEY       VALUE
# "name"    "William Shakespeare"
# "born"    1564
# "died"    1616
# "age"     <make this the difference between the death and birth years, but you MUST
#                do this programmatically (i.e. using math operators), not just writing
#                in one number>

# BEGIN CODING

shakespeare = {"name": "William Shakespeare", "born": 1564,"died": 1616, "age": 1616 - 1564 }

# END CODING

print(f"\nProblem 1: shakespeare = {shakespeare}")


# PROBLEM 2 (10 points)
# Use the <golds> dictionary which contains all of the nations that obtained at least 5
# gold medals in the 2016 Summer Olympics. You will sum up the counts of all of the
# medals and save that value to the variable <medal_count>.

# SETUP
golds = {
    "USA" : 46,
    "GBR" : 27,
    "CHN" : 26,
    "RUS" : 19,
    "GER" : 17,
    "JPN" : 12,
    "FRA" : 10,
    "KOR" : 9,
    "ITA" : 8,
    "AUS" : 8,
    "NED" : 8,
    "HUN" : 8,
    "BRA" : 7,
    "ESP" : 7,
    "KEN" : 6,
    "JAM" : 6,
    "CRO" : 5,
    "CUB" : 5
}
# END SETUP

# BEGIN CODING

medal_count = 0
for val in golds.values():
    medal_count = medal_count + val
# END CODING

print(f"\nProblem 2: medal_count = {medal_count}")


# PROBLEMS 3, 4, 5, and 6:
# In the next four problems, you will work with the poem "won't you celebrate with me"
# by Lucille Clifton in 1991. The text of this poem has been saved as the variable <celebrate>.
# Build functions from the function stubs provided for Problems 3 and 4, and then create the
# main() function as described in Problem 5. Be sure to test all of your functions regularly
# by calling them and using print statements.

# SETUP
celebrate = """
Won't you celebrate with me
what i have shaped into
a kind of life? I had no model.
Born in babylon
both nonwhite and woman
what did i see to be except myself?
I made it up
here on this bridge between
starshine and clay
my one hand holding tight
my other hand, come celebrate
with me that everyday
something has tried to kill me
and has failed.
"""
# END SETUP

# BEGIN CODING
# PROBLEM 3: (20 points)
punctuation = ["'",",",".","?"]
def process_string(string): # <- Don't forget to update the parameters!
    string = string.lower()
    for pun in punctuation:
        string = string.replace(pun, "")
    # print(string)
    words = string.split()
    # print(words)
    return words

words = process_string(celebrate)

"""
    <process_string> will take any <string> passed as a parameter and perform three
    operations on it, in this order:
    1. Make the entire <string> lower-case.
    2. Remove all punctuation (i.e. replace all punctuation with an empty string like this: "")
    3. Create a list of all of the words in <string>.
    Then, <process_string> will return the list of words.

    Parameters:
        - string (str): The string that will be operated upon.

    Returns:
        - (list): A list of the processed words in <string>

    NOTE: For convenience, we have provided a list of the punctuation that you
    need to remove.
"""

  


# PROBLEM 4: (20 points)
def word_frequency(list_of_words): # <- Don't forget to update the parameters!
    freqs = []
    for word in list_of_words:
        freq = list_of_words.count(word)
        freqs.append(freq)
    # print(freqs)
    dictionary = dict(zip(list_of_words, freqs))
    # print(dictionary)
    return dictionary
    

freqs = word_frequency(words)
"""
    <word_frequency> will take a list of word strings and return a dictionary with
    the words as keys and the number of occurances of the word in <list_of_words> as
    the values.

    Example: word_frequency(["to", "be", "or", "not", "to", "be"]) would return
            {"to" : 2, "be" : 2, "or" : 1, "not" : 1}

    Parameters:
        - list_of_words (list): A list of words from which to calculate word frequency.
                For the purposes of this assignment, the returned object from <process_string>
                should work here.

    Returns:
        - (dict): A dictionary of the form {<word (str)> : <number of occurances of word (int)>}
"""

# PROBLEM 5: (20 points)
def find_common_words(frequency_dict, cutoff): # <- Don't forget to update the parameters!
    new_dict = {}
    for key, value in  frequency_dict.items():
        if value >= cutoff:
            new_dict[key] = value
    # print(new_dict)
    common = list(new_dict.keys())
    return(common)

            
#test = find_common_words(freqs, 3)
#print(test)


"""
    <find_common_words> will take a frequency dictionary that describes how many times
    a word has occurred in a sting, and return a list of the words that have occurred
    more than or equal to <cutoff> times.

    Parameters:
        - frequency_dict (dict): A dictionary of the form {<word (str)> :
                <number of occurances of word (int)>}. The returned object from <word_frequency>
                should work here.
        - cutoff (int): The minimum number of occurances of a word in order for it to be included
                in the returned list.

    Returns:
        - (list): A list of the words that occured more than or equal to <cutoff> times.
 """

    


# PROBLEM 6: (20 points)
def main(poem):
    """
    This is the main operator of this script. You will call <process_string>,
    <word_frequency>, and <find_common_words> in order to create a list of the words
    that occur in <poem> at least 3 times. Return that list of common words. Note that
    <main> is being called for you at the end of the script, so you won't need to call
    <main> on your own. If you have coded the utility functions from Problems 3, 4, and
    5 correctly, <main> should only be 4-5 lines of code.

    Parameters:
        - poem (str): Any string. All of the words that occur in <poem> at least 3 times
                will be included in the returned list.

    Returns:
        - (list): A list of all of the words in <poem> that occured at least 3 times.
    """
    words = process_string(poem)
    freqs = word_frequency(words)
    out = find_common_words(freqs, 3)
    return(out)



    

# END CODING

if __name__ == "__main__":

    result = main(celebrate)
    print(f"\nThe final result of problems 3, 4, 5, and 6 (should be a list of 'me', 'and', and 'i'): {result}")

# END PROBLEM SET 04
