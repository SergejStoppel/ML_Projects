# This is a sample Python script.
import language_detect
import en_sum
import de_sum
import nl_sum
import multi_sum

long_text = 'Woonwinkels deden het extreem goed in coronatijd. Maar momenteel is de winkelstraat vooral in de ban van ' \
            'inflatie en personeelstekort. Leen Bakker werd door Gilde in 2017 voor naar schatting iets minder dan ' \
            '€50 miljoen overgenomen door Gilde van het toen noodlijdende Blokker-imperium overgenomen. De private ' \
            'equityfirma fuseerde Leen Bakker met Kwantum, dat het in 2015 al uit de boedel van het zwalkende ' \
            'Macintosh Retail kocht. De twee ketens, nu opererend onder de holding Homefashion Group, hebben een ' \
            'relatief hoge online-omzet. Leen Bakker werd in 1953 in Rotterdam opgericht, Kwantum in 1976 in ' \
            'Woudenberg. De twee winkels met meubels en woonaccessoires zetten in 2020 nog netto €401 miljoen om, ' \
            'tegenover €363 miljoen in het laatste pre-coronajaar. De groep telt volgens de eigen website 4200 ' \
            'werknemers en 276 winkels, waarvan de meeste in Nederland. Een klein kwart van de omzet komt uit België. ' \
            'Bij het aantal werknemers moet wel bij worden aangetekend dat het grotendeels deeltijdbanen zijn, en dat ' \
            'er maar liefst een kleine 200 vacatures openstaan, onder meer voor it-functies, maar ook voor ' \
            'vrachtwagenchauffeurs en winkelmedewerkers. Problemen ' \
            'Volgens zakenbankiers is de volledige synergie tussen Leen Bakker en Kwantum nog niet verzilverd. ' \
            'Daar is wellicht dus nog winst te behalen. Wel wordt hardop de vraag gesteld wat de nieuwe eigenaar ' \
            'nog meer mag verwachten van de omzet, nu consumenten geconfronteerd worden met torenhoge inflatiecijfers.' \
            'Problemen in de logistieke keten die voor lange levertijden van steeds duurdere containers uit China ' \
            'zorgen, zouden de meubelverkoop en doe-het-zelf-branches wel eens kunnen opbreken, stelde ' \
            'Intergamma-topman Harm Jan Stoter onlangs bijvoorbeeld. „Zo heel vaak koop je bijvoorbeeld geen bed. ' \
            'Mensen gaan wellicht toch de hand op de knip houden voor eenmalige grote uitgaven”, zegt een bankier. ' \
            'Als potentiële kopers voor het discountconcern, dat zichzelf afficheert als top 3 speler in meubels en ' \
            'woonaccessoires in ons land, worden buitenlandse meubelbedrijven genoemd, of nieuwe private ' \
            'equityeigenaren. Een beursgang is geen optie. Op het kantoor van Gilde Equity Management zegt de ' \
            'managementassistente: „Ik zal voor u vragen of we een reactie geven, maar doorgaans geven we geen ' \
            'commentaar op onze portfoliobedrijven.” De partner verantwoordelijk voor het bedrijf wil niet aan de ' \
            'telefoon komen. De assistente verwijst uiteindelijk naar het bedrijf zelf. Een receptioniste bij Leen ' \
            'Bakker laat weten dat het mailadres dat speciaal voor de pers vermeld staat op de website van de ' \
            'Homefashion Group inderdaad niet werkt. Op vragen die via de receptie alsnog zijn verstuurd op ' \
            'maandagmiddag, heeft Homefashion Group niet inhoudelijk gereageerd. Ook kersvers directeur Debora ' \
            'Klein reageerde niet op vragen. Prijskaartje ' \
            'Wat het prijskaartje van de keten moet zijn, is nog niet bekend. De jaarcijfers van 2021, de basis ' \
            'van de verkoopbrochure, zijn nog niet gedeponeerd. Als vuistregel wordt een paar keer de ebitda ' \
            '(bedrijfsresultaat) betaald. In 2019 was die nihil, in 2020 bedroeg die €12,3 miljoen. In 2019 en 2020 ' \
            'keerde Homefashion Group al wel €12 en €18,5 miljoen dividend uit. Het bedrijf had de schuldpositie ' \
            'van €50 miljoen uit 2017 in 2020 al grotendeels afgebouwd.'

jap_text = 'ウクライナ侵攻をめぐる欧米の経済制裁の影響が、ロシア国内でじわりと広がっている。ロシア政府によると、制裁の数は6千以上にのぼる。' \
           '政府や企業は対抗策を模索しているが、食料品の値上げやコピー用紙など思わぬ商品の不足も起きている。政府は国民の不満が高まるのを恐れ、' \
           '企業への監視も強めている。　閉店したはずのマクドナルドの店の前で4月上旬、若者や家族連れが行列をつくっていた。スマホで撮影する人も多い。' \
           'ロシア市民「アップルに感謝する。心から」　SNSに皮肉なジョーク' \
           '　米ファストフード大手マクドナルドは3月、ロシア国内の店舗を一時閉鎖すると発表した。だが、タス通信によると、' \
           'モスクワだけでもフランチャイズの10店以上が営業している。本社に抵抗したとみられ'

print(language_detect.detect_language(jap_text))

print(multi_sum.summary(jap_text))

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




