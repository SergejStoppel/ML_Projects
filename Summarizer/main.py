# This is a sample Python script.
import language_detect
import en_sum
#import de_sum

long_text = 'The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the ' \
            'tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During ' \
            'its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made ' \
            'structure in the world, a title it held for 41 years until the Chrysler Building in New York City was ' \
            'finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a ' \
            'broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 ' \
            'metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure ' \
            'in France after the Millau Viaduct.'

print(language_detect.detect_language(long_text))

print(en_sum.summary(long_text))

def summarize(long_text: str, lan_code = '') -> str:
    # Detect used language first
    if lan_code == '':
        lan_code = language_detect.detect_language(long_text)
    # English
    if lan_code == 'en':
        return en_sum.summary(long_text)
    # German
    elif lan_code == 'de':
        b = 2
    # Norwegian
    elif lan_code == 'no':
        b = 3
    # Dutch
    elif lan_code == 'nl':
        b = 4
    # Japanese
    elif lan_code == 'ja':
        b = 5
    # Chinese
    elif lan_code == 'zh':
        b = 6
    # Swedish
    elif lan_code == 'sv':
        b = 7
    else:
        print('language not supported')
        return 0




