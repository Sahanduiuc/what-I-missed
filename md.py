from dataclasses import dataclass
import pandas as pd

@dataclass 
class Image():
    src: str
    link: str = ''

def a(text: str, link: str):
    return f'[{text}]({link})'

def image(source: str, link: str):    
    x = f'![]({source})'
    return a(x, link) if link else x 

def md(df: pd.DataFrame): 
    return df.set_index(df.columns[0]).to_markdown()

def dict_to_markdown(d):
    return md(pd.DataFrame(d))

def rows_to_markdown(rows, columns):
    return md(pd.DataFrame(rows, columns=columns))


assert  rows_to_markdown(rows=[[1,2], ['e', 'f']], 
                       columns=['a', 'b']) == \
dict_to_markdown({'a':[1,'e'], 'b':[2, 'f']})

d = {
    'Код для упражнений': 
        [image('https://allendowney.github.io/ElementsOfDataScience/run_on_colab_small.png',
              'https://colab.research.google.com/drive/1kAZEJOak7NZqv8JEIm5p6KatR5zJz1bp')],
     'Репозитарий':
         ['<https://github.com/epogrebnyak/what-I-missed>']
    }

print(dict_to_markdown(d))
