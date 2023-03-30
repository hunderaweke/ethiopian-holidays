
werat = {'መስከረም': 1, 'ጥቅምት': 2, 'ህዳር': 3, 'ታህሳስ': 4, 'ጥር': 5, 'የካቲት': 6,
         'መጋቢት': 7, 'ሚያዚያ': 8, 'ግንቦት': 9, 'ሰኔ': 10, 'ሐምሌ': 11, 'ነሀሴ': 12, 'ጳጉሜን': 13}


def findMedeb(year) -> int:
    medeb = (year+5500) % 19
    return medeb


def findWenber(medeb) -> int:
    wenber = medeb-1 if medeb > 0 else 18
    return wenber


def findAbekte(wenber) -> int:
    abekte = wenber*11
    if abekte > 30:
        abekte -= 30
    else:
        pass
    return abekte


def findMetk(wenber) -> int:
    abekte = findAbekte(wenber)
    metk = abs(abekte-30)
    return metk


def findBealeMetk(metk) -> str:
    if metk >= 15 and metk <= 30:
        beale_metk = f'መስከረም {metk}'
    elif metk >= 2 and metk <= 14:
        beale_metk = f'ጥቅምት {metk}'
    return beale_metk


def findDay(year, month, date) -> str:
    meskerem1 = findMeskerem1(year)
    tnteYon = {'ረቡዕ': 1, 'ሐሙስ': 2, 'አርብ': 3,
               'ቅዳሜ': 4, 'እሁድ': 5, 'ሰኞ': 6, 'ማግሰኞ': 7}
    tnte_yon = tnteYon[meskerem1]
    astfe_wer = month*2
    day = (date+astfe_wer+tnte_yon) % 7
    Days = {4: 'ረቡዕ', 5: 'ሐሙስ', 6: 'አርብ',
               7: 'ቅዳሜ', 1: 'እሁድ', 2: 'ሰኞ', 3: 'ማግሰኞ'}
    day = Days[day]
    return day


def findMebajaHamer(beale_metk, year):
    Tewsak = {'ቅዳሜ': 8, 'እሁድ': 7, 'ሰኞ': 6,
              'ማግሰኞ': 5, 'ረቡዕ': 4, 'ሐሙስ': 3, 'አርብ': 2}
    Months = {'መስከረም': 1, 'ጥቅምት': 2}
    beale_metk = [i for i in beale_metk.split()]
    month = Months[beale_metk[0]]
    day = findDay(year, month, int(beale_metk[1]))
    tewsak = Tewsak[day]
    mebaja_hamer = tewsak+metk if tewsak + metk < 30 else tewsak
    return mebaja_hamer


def findAmeteWengelawe(year):
    keri = (year+5500) % 4
    match keri:
        case 1:
            wengelawe = "ማቴዎስ"
        case 2:
            wengelawe = "ማርቆስ"
        case 3:
            wengelawe = "ሉቃስ"
        case 0:
            wengelawe = "ዮሐንስ"
    return wengelawe


def findMeskerem1(year):
    tnte_kemer = (((year+5500)//4)+(year+5500)) % 7
    tnteKemer = {2: 'ረቡዕ', 3: 'ሐሙስ', 4: 'አርብ',
                 5: 'ቅዳሜ', 6: 'እሁድ', 0: 'ሰኞ', 1: 'ማግሰኞ'}
    day = tnteKemer[tnte_kemer]
    return day


def findNeneweh(mebaja_hamer):
    if 15 <= mebaja_hamer <= 30:
        wer = 'ጥር'
    else:
        wer = 'የካቲት'
    neneweh = f'{wer} {mebaja_hamer}'
    return neneweh


def findAbiyTsome(neneweh):
    wer = [i for i in neneweh.split()]
    mebaja_hamer = int(wer[1])
    wer = wer[0]
    abiy_tsome_tewsak = 14+mebaja_hamer
    if abiy_tsome_tewsak > 30:
        abiy_tsome_tewsak -= 30
    abiy_tsome_wer = 'የካቲት'
    abiy_tsome = f'{abiy_tsome_wer} {abiy_tsome_tewsak}'
    return abiy_tsome


if '__main__' == __name__:
    year = int(input("Year: "))
    medeb = findMedeb(year)
    wenber = findWenber(medeb)
    metk = findMetk(wenber)
    beale_metk = findBealeMetk(metk)
    mebaja_hamer = findMebajaHamer(beale_metk, year)
    neneweh = findNeneweh(mebaja_hamer)
    abiytsome = findAbiyTsome(neneweh)
    print(abiytsome)