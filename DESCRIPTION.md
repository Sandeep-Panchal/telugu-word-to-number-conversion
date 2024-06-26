## Telugu Number-Words To Numbers Conversion
### Overview
- The Telugu Number-Words to Numbers Conversion package is a Python library that enables developers to convert numerical representations written in Telugu language text (using words) into their equivalent numerical values.
### Features
- Convert Telugu number-words to numerical values.
- Supports a wide range of Telugu numerical representations.
### Create a virtual environment if require with the python version 3.8 or more
```
conda create -n telugu_num_env python=3.8
# Replace "telugu_num_env" with other name according to you
```
### Supporting packages to be installed (Additional packages can be installed if require)
```
text2digits
numpy
```
### Installation with `pip'
```
# From CMD terminal
pip install telugu-words-numbers
# From IPYNB notebook
!pip install telugu-words-numbers
```
### Usage for single text conversion
```
# Import and create an instance of the class TeluguWordsToNumber
from telugu_words_numbers import TeluguWordsToNumber
converter = TeluguWordsToNumber()
text = """
        చేతిలో పదివేల ఐదువందల రూపాయలతో ఐదుగురు స్నేహితులున్నారు.
        వారు హోటల్‌కి వెళ్లి ఏడు వందల ఎనభై తొమ్మిది రూపాయలు మాత్రమే ఖర్చు చేశారు.
        మిగిలిన రెండు వందల పదకొండు వారు తిరిగి ఇంటికి వెళ్లేందుకు ఖర్చు చేశారు.
    """
number, converted_text = converter.word_number_conversion(text)
print('Number: ', number)
print('Original Text: ', text)
print('Converted Text: ', converted_text)
```
### Out of single text conversion
```
Number:  ['10500', '789', '211']
Original Text:
            చేతిలో పదివేల ఐదువందల రూపాయలతో ఐదుగురు స్నేహితులున్నారు.
            వారు హోటల్‌కి వెళ్లి ఏడు వందల ఎనభై తొమ్మిది రూపాయలు మాత్రమే ఖర్చు చేశారు.
            మిగిలిన రెండు వందల పదకొండు వారు తిరిగి ఇంటికి వెళ్లేందుకు ఖర్చు చేశారు.  
Converted Text:
            చేతిలో 10500 రూపాయలతో ఐదుగురు స్నేహితులున్నారు.
            వారు హోటల్‌కి వెళ్లి 789 రూపాయలు మాత్రమే ఖర్చు చేశారు.
            మిగిలిన 211 వారు తిరిగి ఇంటికి వెళ్లేందుకు ఖర్చు చేశారు.
```
### Usage for multiple text conversion
```
# Import and create an instance of the class TeluguWordsToNumber
from telugu_words_numbers import TeluguWordsToNumber
converter = TeluguWordsToNumber()
texts = [
        "నూట పదమూడు మామిడి పండ్లలో ఒక వ్యక్తి డెబ్బై ఏడు మామిడి పండ్లను కొన్నాడు.",
        "వెయ్యి యాభై ఐదు రూపాయలలో ఒక వ్యక్తి తొమ్మిది వందల తొంభై రూపాయలు మాత్రమే ఖర్చు చేశాడు."
    ]
for text in texts:
    number, converted_text = converter.word_number_conversion(text)
    print('Number: ', number)
    print('Original Text: ', text)
    print('Converted Text: ', converted_text)
    print('-'*20, '\n')
```
### Output of multiple text conversion
```
Number:  ['113', '1', '77']
Original Text:  నూట పదమూడు మామిడి పండ్లలో ఒక వ్యక్తి డెబ్బై ఏడు మామిడి పండ్లను కొన్నాడు.
Converted Text:  113 మామిడి పండ్లలో 1 వ్యక్తి 77 మామిడి పండ్లను కొన్నాడు.
--------------------
Number:  ['1055', '1', '990']
Original Text:  వెయ్యి యాభై ఐదు రూపాయలలో ఒక వ్యక్తి తొమ్మిది వందల తొంభై రూపాయలు మాత్రమే ఖర్చు చేశాడు.
Converted Text:  1055 రూపాయలలో 1 వ్యక్తి 990 రూపాయలు మాత్రమే ఖర్చు చేశాడు.
--------------------
```