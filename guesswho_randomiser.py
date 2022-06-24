import streamlit as st
import pandas as pd
import itertools, random

st.set_page_config(layout="wide")

st.title('Guess Who Randomiser')

default_values = {
  "Ethnicity": {
    "Oriental Asian": 8,
    "Malay-ish": 6,
    "Indian-ish": 6,
    "White": 4
  },
  "Gender": {
    "Male": 10,
    "Female": 10,
    "Ambiguous": 4
  },
  "Eye size": {
    "Small": 8,
    "Average": 8,
    "Big": 8
  },
  "Glasses": {
    "Yes": 12,
    "No": 8,
    "Colour Contacts": 4
  },
  "Hair Colour": {
    "Dark": 10,
    "Medium": 10,
    "Light": 4
  },
  "Hair Length": {
    "Long loose": 4,
    "Long tied": 5,
    "Short": 12,
    "Bald": 3
  },
  "Nose Size": {
    "Small": 8,
    "Average": 8,
    "Big": 8
  },
  "Hat/ Headcovering": {
    "Yes": 16,
    "No": 8
  },
  "Piercings": {
    "Yes": 16,
    "No": 8
  },
  "Style": {
    "Business": 8,
    "Streetwear": 8,
    "Homewear": 8
  },
  "Age": {
    "Teen": 6,
    "Millennial": 6,
    "Boomer": 6,
    "Old": 6
  },
  "Weight": {
    "Thin": 6,
    "Average": 12,
    "Hefty": 6
  },
  "Expression": {
    "Happy": 8,
    "Neutral": 11,
    "Angry": 3,
    "Sad": 2
  }
}

with st.sidebar:
  st.button("Randomise")
  st.markdown("---")
  values = st.slider(
      'Number of cards to generate', 0,50,24)
  st.write('Cards: ', values)

for feature in default_values:
  with st.expander(feature):
    for choice, value in default_values[feature].items():
      feature_choices = st.number_input(choice, key=feature+choice, min_value=0, value=value)


# number = st.number_input('Insert a number', min_value=0, value=0)
# st.write('The current number is ', number)

# def add_newft_input(
#   title:str
# ):
#   return st.number_input(title, min_value=0, value=0)

# new_feature = st.button('Add new feature', on_click=add_newft_input(title='new_feaure'))


st.header('Randomised List')

deck = {}

for feature in default_values:
  deck[feature]=[]
  for choice, value in default_values[feature].items():
    deck[feature].extend(list(itertools.repeat(choice,value)))

for feature in deck:
  random.shuffle(deck[feature])

print(deck)

df = pd.DataFrame(deck)
df.index = range(1, df.shape[0] + 1)
st.dataframe(df, height=750)