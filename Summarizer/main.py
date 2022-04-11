# This is a sample Python script.
import language_detect
import en_sum
#import de_sum


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




