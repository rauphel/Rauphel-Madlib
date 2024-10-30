# Madlib Assignment
# Rauphel Kenept
# Oct 24, 2024

import random as ra
import streamlit as st

# Choose if they want to make their own or if they want it to be computer generated
choose = st.radio(
    "Do you want to Create a Madlib or have a Computer make it?",
    ["User made", "Computer Generated"])

# Choose which madlib they want to do
madlib = st.selectbox("Which rhyme do you want to make a madlib out?",
    ("The ants go marching", "This little piggy"), help = "Select same option to have the computer select new words for the same madlib")

# User inputs words to make madlib out of The ants go marching and prints it out
# if they chose this option
if madlib == "The ants go marching" and choose == "User made":
    noun_one = st.text_input("Write an animal in plural form")
    verb_one = st.text_input("Write a verb ending in ing")
    noun_two = st.text_input("Write a body part")
    adjective = st.text_input("Write an adjective")
    noun_three = st.text_input("Write a place to go to")
    noun_five = st.text_input("Write an weather event")
    
# User inputs words to make madlib out of This little piggy and prints it out
# if they chose this option
elif madlib == "This little piggy" and choose == "User made":
    adjective = st.text_input("Write an adjective")
    noun_one = st.text_input("Write an animal")
    noun_three = st.text_input("Write a place to go to")
    noun_four = st.text_input("Write a place to stay at")
    noun_six = st.text_input("Write a type of food")
    onomatopoeia = st.text_input("Write an onomatopoeia")
    onomatopoeia = onomatopoeia.rstrip() * 3
    
# Computer picks words from a txt file needed for madlib 1
elif choose == "Computer Generated" and madlib == "The ants go marching":
    rand_num = ra.randint(1, 571)
    rand_num_two = ra.randint(574, 2426)
    rand_num_three = ra.randint(2432, 2476)
    rand_num_four = ra.randint(2480, 2670)
    rand_num_five = ra.randint(2673, 2962)
    rand_num_six = ra.randint(2976, 3004)
    with open('madlib_words.txt', 'r') as f:
        lines = f.readlines()
        noun_one = lines[rand_num]        
        verb_one = lines[rand_num_two]
        noun_two = lines[rand_num_three]
        adjective = lines[rand_num_four]
        noun_three = lines[rand_num_five]
        noun_five = lines[rand_num_six]

# Computer picks words from a txt file needed for madlib 2
elif choose == "Computer Generated" and madlib == "This little piggy":
    rand_num = ra.randint(1, 571)
    rand_num_four = ra.randint(2480, 2670)
    rand_num_five = ra.randint(2673, 2962)
    rand_num_five_two = ra.randint(2673, 2962)
    rand_num_six = ra.randint(2976, 3004)
    rand_num_seven = ra.randint(3007, 3048)
    rand_num_eight = ra.randint(3051, 3227)
    with open('madlib_words.txt', 'r') as f:
        lines = f.readlines()
        noun_one = lines[rand_num]        
        adjective = lines[rand_num_four]
        noun_three = lines[rand_num_five]
        noun_four = lines[rand_num_five_two]
        noun_six = lines[rand_num_seven]
        onomatopoeia = lines[rand_num_eight]
        onomatopoeia = onomatopoeia.rstrip() * 3

# Prints out resulting madlib for either madlib 1 or two and human made or computer made
if madlib == "The ants go marching": 
    st.write(f'''The {noun_one.rstrip()} go {verb_one.rstrip()} one by one, hurrah, hurrah.
    The {noun_one.rstrip()} go {verb_one.rstrip()} one by one, hurrah, hurrah.
    The {noun_one.rstrip()} go {verb_one.rstrip()} one by one,
    The {adjective.rstrip()} one stops to suck his {noun_two.rstrip()}.
    And they all go {verb_one.rstrip()} down,
    To the {noun_three}, to get out, of the {noun_five.rstrip()}.''')

elif madlib == "This little piggy": 
    st.write(f'''This {adjective.rstrip()} {noun_one.rstrip()} went to {noun_three.rstrip()}
    This {adjective.rstrip()} {noun_one.rstrip()} stayed at {noun_four.rstrip()}
    This {adjective.rstrip()} {noun_one.rstrip()} ate a {noun_six.rstrip()}
    This {adjective.rstrip()} {noun_one.rstrip()} had none
    This {adjective.rstrip()} {noun_one.rstrip()} cried
    {onomatopoeia.rstrip()}
    All the way to the {noun_four.rstrip()}''')
