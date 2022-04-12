# This is a sample Python script.
import language_detect
import en_sum
import de_sum
import nl_sum
import multi_sum


def summarize(long_text: str, lan_code = '') -> str:
    # Detect used language first
    if lan_code == '':
        lan_code = language_detect.detect_language(long_text)
    # English
    if lan_code == 'en':
        return en_sum.summary(long_text)
    # German
    elif lan_code == 'de':
        return de_sum.summary(long_text)
    # Norwegian
    elif lan_code == 'no':
        print('This language not supported yet.')
    # Dutch
    elif lan_code == 'nl':
        return nl_sum.summary(long_text)
    # Japanese
    elif lan_code == 'ja':
        return multi_sum.summary(long_text)
    # Chinese
    elif lan_code == 'zh':
        b = 6
    # Swedish
    elif lan_code == 'sv':
        b = 7
    else:
        print('This language not supported yet.')
        return '0'
    return '0'




