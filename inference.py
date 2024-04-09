# call the module/class
from telugu_words_numbers import telugu_word_to_number as twn
from typing import List

# list of input texts
texts = [
    "దీపిక కి అరవై పంపండి",
    "భరత్ కి ఏడు వందలు పంపు",
    "పంతొమ్మిది వందలు సత్య కి పంపియ్యండి",
    "సందీప్‌కి ఇరవై ఐదు వేల నలభై ఏడు రూపాయలు పంపండి",
    "ఇరవై ఎనిమిది వందల ఐదు రూపాయలు పంపండి",
    "సందీప్‌కి యాభై ఐదు రూపాయలు పంపు",
    "సందీప్‌కి ఐదువేల ఎనభై తొమ్మిది రూపాయలు పంపు",
    "కాశ్యప్‌కి ఒక రూపాయి పంపు",
    "కశ్యపునికి ఏడు అరవై తొమ్మిది రూపాయలు పంపు",
    "నలభై ఐదు వేల యాభై మూడు రూపాయలు కాశ్యపుకి పంపు",
    "నలభై ఐదు వందల యాభై మూడు రూపాయలు కాశ్యపుకి పంపు"
    "రాధకు ఇరవై మూడు వేల మూడు వందల ముప్పై మూడు రూపాయలు పంపండి",
    "హర్ష కు తొమ్మిది రూపాయల ఐదు పైసలు అందించు",
    "వినోద్ కి  నాలుగు వందల డెబ్బై రూపాయలు  యూపిఐ చెయ్యండి",
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
    text = "దీపిక కి అరవై పంపండి"
    number, converted_text = converter.word_number_conversion(text)
    print("Number: ", number)
    print("Original Text: ", text)
    print("Converted Text: ", converted_text)

    # comment/uncomment for multiple texts inference
    # multiple_text_inference(texts)
