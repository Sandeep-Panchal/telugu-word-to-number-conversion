# call the module/class
from telugu_words_numbers import telugu_word_to_number as twn
from typing import List

# list of input texts
texts = [
        "నూట పదమూడు మామిడి పండ్లలో ఒక వ్యక్తి డెబ్బై ఏడు మామిడి పండ్లను కొన్నాడు.",
        "వెయ్యి యాభై ఐదు రూపాయలలో ఒక వ్యక్తి తొమ్మిది వందల తొంభై రూపాయలు మాత్రమే ఖర్చు చేశాడు."
    ]

# Function for multiple texts inference ie list of text
def multiple_text_inference(texts: List[str]) -> None:
    for text in texts:
        number, converted_text = converter.word_number_conversion(text)
        print("Number: ", number)
        print("Original Text: ", text)
        print("Converted Text: ", converted_text)
        print("-" * 20, "\n")

    return None


if __name__ == "__main__":

    # creating and object of the class TeluguWordsToNum
    converter = twn.TeluguWordsToNumber()

    # comment/uncomment for single text inference
    text = """
            చేతిలో పదివేల ఐదువందల రూపాయలతో ఐదుగురు స్నేహితులున్నారు.
            వారు హోటల్‌కి వెళ్లి ఏడు వందల ఎనభై తొమ్మిది రూపాయలు మాత్రమే ఖర్చు చేశారు.
            మిగిలిన రెండు వందల పదకొండు వారు తిరిగి ఇంటికి వెళ్లేందుకు ఖర్చు చేశారు.
        """
    
    number, converted_text = converter.word_number_conversion(text)
    print("Number: ", number)
    print("Original Text: ", text)
    print("Converted Text: ", converted_text)

    # comment/uncomment for multiple texts inference
    multiple_text_inference(texts)
    
