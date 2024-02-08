#!/usr/bin/env python3

import string, random

def gethostname(email_add):
    atposition = email_add.find("@")
    hostname = email_add[atposition+1:]
    return hostname

def getfirstname(name):
    firstname = name[:name.find(" ")]
    return firstname

def getlastname(name):
    lastname = name[name.find(" "):]
    return lastname.strip()

def pound_to_kilo(pounds):
    kilo = pounds * 0.4535924
    return kilo

def kilo_to_pound(kilos):
    pounds = kilos * 2.204623
    return pounds

def meter_to_inch(meters):
    inch = meters * 39.37008
    return inch

def inch_to_meter(inch):
    meter = inch * 0.0254
    return meter

def currency_conv():
    amount = float(input("What amount do you want to convert? "))
    currency = input("what initial currency is  the amount in? ")
    output_currency = input("What currency should your money be in? ")
    output = 0

    # USD
    usd_to_eur = amount * 0.92514818
    usd_to_gbp = amount * 0.79170384
    usd_to_cad = amount * 1.3464199
    usd_to_aud = amount * 1.5334761
    usd_to_jpy = amount * 148.34598
    usd_to_inr = amount * 82.937407
    usd_to_nzd = amount * 1.6489423
    usd_to_chf = amount * 0.86695172
    usd_to_zar = amount * 18.885183

    if currency.strip().lower() == "usd" and output_currency.strip().lower() == "eur":
        output = usd_to_eur
    elif currency.strip().lower() == "usd" and output_currency.strip().lower() == "gbp":
        output = usd_to_gbp
    elif currency.strip().lower() == "usd" and output_currency.strip().lower() == "cad":
        output = usd_to_cad
    elif currency.strip().lower() == "usd" and output_currency.strip().lower() == "aud":
        output = usd_to_aud
    elif currency.strip().lower() == "usd" and output_currency.strip().lower() == "jpy":
        output = usd_to_jpy
    elif currency.strip().lower() == "usd" and output_currency.strip().lower() == "inr":
        output = usd_to_inr
    elif currency.strip().lower() == "usd" and output_currency.strip().lower() == "nzd":
        output = usd_to_nzd
    elif currency.strip().lower() == "usd" and output_currency.strip().lower() == "chf":
        output = usd_to_chf
    elif currency.strip().lower() == "usd" and output_currency.strip().lower() == "zar":
        output = usd_to_zar

    # EUR
    eur_to_usd = amount * 1.08022
    eur_to_gbp = amount * 0.85488104
    eur_to_cad = amount * 1.4537662
    eur_to_aud = amount * 1.6565243
    eur_to_jpy = amount * 160.18576
    eur_to_inr = amount * 89.549655
    eur_to_nzd = amount * 1.7804445
    eur_to_chf = amount * 0.93608778
    eur_to_zar = amount * 20.399219

    if currency.strip().lower() == "eur" and output_currency.strip().lower() == "usd":
        output = eur_to_usd
    elif currency.strip().lower() == "eur" and output_currency.strip().lower() == "gbp":
        output = eur_to_gbp
    elif currency.strip().lower() == "eur" and output_currency.strip().lower() == "cad":
        output = eur_to_cad
    elif currency.strip().lower() == "eur" and output_currency.strip().lower() == "aud":
        output = eur_to_aud
    elif currency.strip().lower() == "eur" and output_currency.strip().lower() == "jpy":
        output = eur_to_jpy
    elif currency.strip().lower() == "eur" and output_currency.strip().lower() == "inr":
        output = eur_to_inr
    elif currency.strip().lower() == "eur" and output_currency.strip().lower() == "nzd":
        output = eur_to_nzd
    elif currency.strip().lower() == "eur" and output_currency.strip().lower() == "chf":
        output = eur_to_chf
    elif currency.strip().lower() == "eur" and output_currency.strip().lower() == "zar":
        output = eur_to_zar

    # GBP
    gbp_to_usd = amount * 1.263095
    gbp_to_eur = amount * 1.169949
    gbp_to_cad = amount * 1.7006914
    gbp_to_aud = amount * 1.9381377
    gbp_to_jpy = amount * 187.39196
    gbp_to_inr = amount * 104.75221
    gbp_to_nzd = amount * 2.082734
    gbp_to_chf = amount * 1.0950936
    gbp_to_zar = amount * 23.860244

    if currency.strip().lower() == "gbp" and output_currency.strip().lower() == "usd":
        output = gbp_to_usd
    elif currency.strip().lower() == "gbp" and output_currency.strip().lower() == "eur":
        output = gbp_to_eur
    elif currency.strip().lower() == "gbp" and output_currency.strip().lower() == "cad":
        output = gbp_to_cad
    elif currency.strip().lower() == "gbp" and output_currency.strip().lower() == "aud":
        output = gbp_to_aud
    elif currency.strip().lower() == "gbp" and output_currency.strip().lower() == "jpy":
        output = gbp_to_jpy
    elif currency.strip().lower() == "gbp" and output_currency.strip().lower() == "inr":
        output = gbp_to_inr
    elif currency.strip().lower() == "gbp" and output_currency.strip().lower() == "nzd":
        output = gbp_to_nzd
    elif currency.strip().lower() == "gbp" and output_currency.strip().lower() == "chf":
        output = gbp_to_chf
    elif currency.strip().lower() == "gbp" and output_currency.strip().lower() == "zar":
        output = gbp_to_zar

    # CAD
    cad_to_usd = amount * 0.74265378
    cad_to_eur = amount * 0.68761873
    cad_to_gbp = amount * 0.58795779
    cad_to_aud = amount * 1.1388374
    cad_to_jpy = amount * 110.17393
    cad_to_inr = amount * 61.586303
    cad_to_nzd = amount * 1.2245067
    cad_to_chf = amount * 0.64381779
    cad_to_zar = amount * 14.02608

    if currency.strip().lower() == "cad" and output_currency.strip().lower() == "usd":
        output = cad_to_usd
    elif currency.strip().lower() == "cad" and output_currency.strip().lower() == "eur":
        output = cad_to_eur
    elif currency.strip().lower() == "cad" and output_currency.strip().lower() == "gbp":
        output = cad_to_gbp
    elif currency.strip().lower() == "cad" and output_currency.strip().lower() == "aud":
        output = cad_to_aud
    elif currency.strip().lower() == "cad" and output_currency.strip().lower() == "jpy":
        output = cad_to_jpy
    elif currency.strip().lower() == "cad" and output_currency.strip().lower() == "inr":
        output = cad_to_inr
    elif currency.strip().lower() == "cad" and output_currency.strip().lower() == "nzd":
        output = cad_to_nzd
    elif currency.strip().lower() == "cad" and output_currency.strip().lower() == "chf":
        output = cad_to_chf
    elif currency.strip().lower() == "cad" and output_currency.strip().lower() == "zar":
        output = cad_to_zar

    # AUD
    aud_to_usd = amount * 0.65183781
    aud_to_eur = amount * 0.603741
    aud_to_gbp = amount * 0.51605872
    aud_to_cad = amount * 0.87778002
    aud_to_jpy = amount * 96.698644
    aud_to_inr = amount * 54.0547
    aud_to_nzd = amount * 1.0748461
    aud_to_chf = amount * 0.52579205
    aud_to_zar = amount * 11.455825

    if currency.strip().lower() == "aud" and output_currency.strip().lower() == "usd":
        output = aud_to_usd
    elif currency.strip().lower() == "aud" and output_currency.strip().lower() == "eur":
        output = aud_to_eur
    elif currency.strip().lower() == "aud" and output_currency.strip().lower() == "gbp":
        output = aud_to_gbp
    elif currency.strip().lower() == "aud" and output_currency.strip().lower() == "cad":
        output = aud_to_cad
    elif currency.strip().lower() == "aud" and output_currency.strip().lower() == "jpy":
        output = aud_to_jpy
    elif currency.strip().lower() == "aud" and output_currency.strip().lower() == "inr":
        output = aud_to_inr
    elif currency.strip().lower() == "aud" and output_currency.strip().lower() == "nzd":
        output = aud_to_nzd
    elif currency.strip().lower() == "aud" and output_currency.strip().lower() == "chf":
        output = aud_to_chf
    elif currency.strip().lower() == "aud" and output_currency.strip().lower() == "zar":
        output = aud_to_zar

    # JPY
    jpy_to_usd = amount * 0.0067408705
    jpy_to_eur = amount * 0.006238284
    jpy_to_gbp = amount * 0.005336675
    jpy_to_cad = amount * 0.0090770105
    jpy_to_aud = amount * 0.010331098
    jpy_to_inr = amount * 0.55903542
    jpy_to_nzd = amount * 0.011114971
    jpy_to_chf = amount * 0.0058439796
    jpy_to_zar = amount * 0.12725868

    if currency.strip().lower() == "jpy" and output_currency.strip().lower() == "usd":
        output = jpy_to_usd
    elif currency.strip().lower() == "jpy" and output_currency.strip().lower() == "eur":
        output = jpy_to_eur
    elif currency.strip().lower() == "jpy" and output_currency.strip().lower() == "gbp":
        output = jpy_to_gbp
    elif currency.strip().lower() == "jpy" and output_currency.strip().lower() == "cad":
        output = jpy_to_cad
    elif currency.strip().lower() == "jpy" and output_currency.strip().lower() == "aud":
        output = jpy_to_aud
    elif currency.strip().lower() == "jpy" and output_currency.strip().lower() == "inr":
        output = jpy_to_inr
    elif currency.strip().lower() == "jpy" and output_currency.strip().lower() == "nzd":
        output = jpy_to_nzd
    elif currency.strip().lower() == "jpy" and output_currency.strip().lower() == "chf":
        output = jpy_to_chf
    elif currency.strip().lower() == "jpy" and output_currency.strip().lower() == "zar":
        output = jpy_to_zar

    # INR
    inr_to_usd = amount * 0.0120584
    inr_to_eur = amount * 0.011215076
    inr_to_gbp = amount * 0.0095809323
    inr_to_cad = amount * 0.016254256
    inr_to_aud = amount * 0.018582492
    inr_to_jpy = amount * 1.7999245
    inr_to_nzd = amount * 0.019803425
    inr_to_chf = amount * 0.01055115
    inr_to_zar = amount * 0.22871674

    if currency.strip().lower() == "inr" and output_currency.strip().lower() == "usd":
        output = inr_to_usd
    elif currency.strip().lower() == "inr" and output_currency.strip().lower() == "eur":
        output = inr_to_eur
    elif currency.strip().lower() == "inr" and output_currency.strip().lower() == "gbp":
        output = inr_to_gbp
    elif currency.strip().lower() == "inr" and output_currency.strip().lower() == "cad":
        output = inr_to_cad
    elif currency.strip().lower() == "inr" and output_currency.strip().lower() == "aud":
        output = inr_to_aud
    elif currency.strip().lower() == "inr" and output_currency.strip().lower() == "jpy":
        output = inr_to_jpy
    elif currency.strip().lower() == "inr" and output_currency.strip().lower() == "nzd":
        output = inr_to_nzd
    elif currency.strip().lower() == "inr" and output_currency.strip().lower() == "chf":
        output = inr_to_chf
    elif currency.strip().lower() == "inr" and output_currency.strip().lower() == "zar":
        output = inr_to_zar

    # NZD
    nzd_to_usd = amount * 0.60857896
    nzd_to_eur = amount * 0.56624969
    nzd_to_gbp = amount * 0.48356048
    nzd_to_cad = amount * 0.82075703
    nzd_to_aud = amount * 0.9383228
    nzd_to_jpy = amount * 90.906887
    nzd_to_inr = amount * 50.516778
    nzd_to_chf = amount * 0.53302518
    nzd_to_zar = amount * 11.54196

    if currency.strip().lower() == "nzd" and output_currency.strip().lower() == "usd":
        output = nzd_to_usd
    elif currency.strip().lower() == "nzd" and output_currency.strip().lower() == "eur":
        output = nzd_to_eur
    elif currency.strip().lower() == "nzd" and output_currency.strip().lower() == "gbp":
        output = nzd_to_gbp
    elif currency.strip().lower() == "nzd" and output_currency.strip().lower() == "cad":
        output = nzd_to_cad
    elif currency.strip().lower() == "nzd" and output_currency.strip().lower() == "aud":
        output = nzd_to_aud
    elif currency.strip().lower() == "nzd" and output_currency.strip().lower() == "jpy":
        output = nzd_to_jpy
    elif currency.strip().lower() == "nzd" and output_currency.strip().lower() == "inr":
        output = nzd_to_inr
    elif currency.strip().lower() == "nzd" and output_currency.strip().lower() == "chf":
        output = nzd_to_chf
    elif currency.strip().lower() == "nzd" and output_currency.strip().lower() == "zar":
        output = nzd_to_zar

    # CHF
    chf_to_usd = amount * 1.1418472
    chf_to_eur = amount * 1.0624987
    chf_to_gbp = amount * 0.90775311
    chf_to_cad = amount * 1.5394003
    chf_to_aud = amount * 1.7604744
    chf_to_jpy = amount * 170.49724
    chf_to_inr = amount * 94.773584
    chf_to_nzd = amount * 1.8761313
    chf_to_zar = amount * 21.648162

    if currency.strip().lower() == "chf" and output_currency.strip().lower() == "usd":
        output = chf_to_usd
    elif currency.strip().lower() == "chf" and output_currency.strip().lower() == "eur":
        output = chf_to_eur
    elif currency.strip().lower() == "chf" and output_currency.strip().lower() == "gbp":
        output = chf_to_gbp
    elif currency.strip().lower() == "chf" and output_currency.strip().lower() == "cad":
        output = chf_to_cad
    elif currency.strip().lower() == "chf" and output_currency.strip().lower() == "aud":
        output = chf_to_aud
    elif currency.strip().lower() == "chf" and output_currency.strip().lower() == "jpy":
        output = chf_to_jpy
    elif currency.strip().lower() == "chf" and output_currency.strip().lower() == "nzd":
        output = chf_to_nzd
    elif currency.strip().lower() == "chf" and output_currency.strip().lower() == "inr":
        output = chf_to_inr
    elif currency.strip().lower() == "chf" and output_currency.strip().lower() == "zar":
        output = chf_to_zar

    # ZAR
    zar_to_usd = amount * 0.052767345
    zar_to_eur = amount * 0.049083466
    zar_to_gbp = amount * 0.041932187
    zar_to_cad = amount * 0.071105213
    zar_to_aud = amount * 0.081346294
    zar_to_jpy = amount * 7.8789609
    zar_to_inr = amount * 4.3786629
    zar_to_nzd = amount * 0.086679022
    zar_to_chf = amount * 0.046191293

    if currency.strip().lower() == "zar" and output_currency.strip().lower() == "usd":
        output = zar_to_usd
    elif currency.strip().lower() == "zar" and output_currency.strip().lower() == "eur":
        output = zar_to_eur
    elif currency.strip().lower() == "zar" and output_currency.strip().lower() == "gbp":
        output = zar_to_gbp
    elif currency.strip().lower() == "zar" and output_currency.strip().lower() == "cad":
        output = zar_to_cad
    elif currency.strip().lower() == "zar" and output_currency.strip().lower() == "aud":
        output = zar_to_aud
    elif currency.strip().lower() == "zar" and output_currency.strip().lower() == "jpy":
        output = zar_to_jpy
    elif currency.strip().lower() == "zar" and output_currency.strip().lower() == "nzd":
        output = zar_to_nzd
    elif currency.strip().lower() == "zar" and output_currency.strip().lower() == "inr":
        output = zar_to_inr
    elif currency.strip().lower() == "zar" and output_currency.strip().lower() == "chf":
        output = zar_to_chf

    print(output, output_currency.strip().upper())

def rps():
    ropasc = ["rock", "paper", "scissors"]
    text = "This is a game of rock, paper, scissors. To exit press q "
    print(text)
    userchoice = input("Rock, paper or scissors? The choice is yours: ")
    score = 0
    tie = 0
    lose = 0
    pcchoice = random.choice(ropasc)
    while userchoice != "q":
        pcchoice = random.choice(ropasc)
        if userchoice == "rock" and pcchoice == "paper":
           print("You lost!")
           print("The computer chose....", pcchoice + "!")
           userchoice = input("Rock, paper or scissors? The choice is yours: ")
           continue
        elif userchoice == "rock" and pcchoice == "rock":
           print("Tie! Try again.")
           print("The computer chose....", pcchoice + "!")
           userchoice = input("Rock, paper or scissors? The choice is yours: ")
           continue
        elif userchoice == "rock" and pcchoice == "scissors":
           print("You won, congrats!")
           print("The computer chose....", pcchoice + "!")
           score += 1
           userchoice = input("Rock, paper or scissors? The choice is yours: ")
           continue
        elif userchoice == "paper" and pcchoice == "rock":
           print("You won, congrats!")
           print("The computer chose....", pcchoice + "!")
           score += 1
           userchoice = input("Rock, paper or scissors? The choice is yours: ")
           continue
        elif userchoice == "paper" and pcchoice == "paper":
           print("Tie! Try again.")
           print("The computer chose....", pcchoice + "!")
           userchoice = input("Rock, paper or scissors? The choice is yours: ")
           continue
        elif userchoice == "paper" and pcchoice == "scissors":
           print("You lost, how unfortunate :(")
           print("The computer chose....", pcchoice + "!")
           userchoice = input("Rock, paper or scissors? The choice is yours: ")
           continue
        elif userchoice == "scissors" and pcchoice == "paper":
            print("You won, great!")
            print("The computer chose....", pcchoice + "!")
            userchoice = input("Rock, paper or scissors? The choice is yours: ")
            continue
        elif userchoice == "scissors" and pcchoice == "rock":
            print("Damn it, you lost!")
            print("The computer chose....", pcchoice + "!")
            userchoice = input("Rock, paper or scissors? The choice is yours: ")
            continue
        elif userchoice == "scissors" and pcchoice == "scissors":
            print("Tie, try again!")
            print("The computer chose....", pcchoice + "!")
            userchoice = input("Rock, paper or scissors? The choice is yours: ")
            continue

    if userchoice == "q":
        print(f"Your stats:\nScore: {score}\nLosses: {lose}\nTies: {tie}")






rps()
