import streamlit as st
import pandas as pd
import altair as alt

st.write("""
         
# Letter Counter

It will coutn each letter of any article
         """)


article = st.text_input(label="Enter sentense please")
article_cap = article.upper()


# letter counter
def letter_counter(ac):
    lc = dict([
        ('Space', ac.count(' ')),
        ('.', ac.count('.')),
        ('?', ac.count('?')),
        (',', ac.count(',')),
        ("'", ac.count("'")),
        (';', ac.count(';')),
        (':', ac.count(':')),
        ('=', ac.count('=')),
        ('A', ac.count('A')),
        ('B', ac.count('B')),
        ('C', ac.count('C')),
        ('D', ac.count('D')),
        ('E', ac.count('E')),
        ('F', ac.count('F')),
        ('G', ac.count('G')),
        ('H', ac.count('H')),
        ('I', ac.count('I')),
        ('J', ac.count('J')),
        ('K', ac.count('K')),
        ('L', ac.count('L')),
        ('M', ac.count('M')),
        ('N', ac.count('N')),
        ('O', ac.count('O')),
        ('P', ac.count('P')),
        ('Q', ac.count('Q')),
        ('R', ac.count('R')),
        ('S', ac.count('S')),
        ('T', ac.count('T')),
        ('U', ac.count('U')),
        ('V', ac.count('V')),
        ('W', ac.count('W')),
        ('X', ac.count('X')),
        ('Y', ac.count('Y')),
        ('Z', ac.count('Z')),
    ])
    return lc


article_injection = letter_counter(article_cap)


article_injection

st.write("""
## datafreame
""")
dataFrame = pd.DataFrame.from_dict(article_injection, orient='index')
dataFrame = dataFrame.rename({0: 'Count'}, axis='columns')
dataFrame.reset_index(inplace=True)
dataFrame = dataFrame.rename(columns={'index','Letters'})
st.write(dataFrame)
