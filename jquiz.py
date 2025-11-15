#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

# ANSI barve za konzolo
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Seznam 50 najpogostejših glagolov (primer)
# oblika: (slovensko, italijansko, špansko)
VERBS = [
    ("biti", "essere", "ser"),
    ("imeti", "avere", "tener"),
    ("delati", "lavorare", "trabajar"),
    ("iti", "andare", "ir"),
    ("reči", "dire", "decir"),
    ("videti", "vedere", "ver"),
    ("jesti", "mangiare", "comer"),
    ("piti", "bere", "beber"),
    ("hoteti", "volere", "querer"),
    ("dati", "dare", "dar"),
    ("priti", "venire", "venir"),
    ("vedeti", "sapere", "saber"),
    ("misliti", "pensare", "pensar"),
    ("vzeti", "prendere", "tomar"),
    ("najti", "trovare", "encontrar"),
    ("čutiti", "sentire", "sentir"),
    ("uporabljati", "usare", "usar"),
    ("delovati", "funzionare", "funcionar"),
    ("ostati", "restare", "quedar"),
    ("verjeti", "credere", "creer"),
    ("govoriti", "parlare", "hablar"),
    ("slišati", "sentire", "oír"),
    ("živeti", "vivere", "vivir"),
    ("deliti", "condividere", "compartir"),
    ("poskušati", "provare", "intentar"),
    ("odpreti", "aprire", "abrir"),
    ("zapreti", "chiudere", "cerrar"),
    ("začeti", "iniziare", "empezar"),
    ("končati", "finire", "terminar"),
    ("spati", "dormire", "dormir"),
    ("voziti", "guidare", "conducir"),
    ("brati", "leggere", "leer"),
    ("pisati", "scrivere", "escribir"),
    ("kupiti", "comprare", "comprar"),
    ("prodati", "vendere", "vender"),
    ("pomagati", "aiutare", "ayudar"),
    ("igrati", "giocare", "jugar"),
    ("teči", "correre", "correr"),
    ("hoditi", "camminare", "caminar"),
    ("plačati", "pagare", "pagar"),
    ("začeti (comm.)", "cominciare", "comenzar"),
    ("zapomniti si", "ricordare", "recordar"),
    ("pozabiti", "dimenticare", "olvidar"),
    ("poslati", "mandare", "enviar"),
    ("prejeti", "ricevere", "recibir"),
    ("odločiti se", "decidere", "decidir"),
    ("vprašati", "chiedere", "preguntar"),
    ("odgovoriti", "rispondere", "responder"),
    ("čakati", "aspettare", "esperar"),
    ("potrebovati", "bisognare", "necesitar"),
]

NUM_QUESTIONS = 20


def read_with_default(prompt, default_value):
    """
    Prebere uporabnikov vnos.
    Če uporabnik pritisne samo Enter, vrne default_value.
    """
    user_input = input(prompt).strip()
    if user_input == "":
        return default_value
    return user_input


def choose_language():
    """
    1 = Italijanščina, 2 = Španščina
    Privzeto 1.
    """
    print("=== Nastavitve ===")
    print("Izberi jezik za učenje:")
    print("  1) Italijanščina (ITA)")
    print("  2) Španščina (ŠPA)")
    choice = read_with_default("Vnos (1/2, privzeto 1): ", "1")

    if choice == "2":
        return "SPA"
    else:
        return "ITA"


def choose_question_language():
    """
    1 = vprašanja v slovenščini, 2 = v tujem jeziku
    Privzeto 1.
    """
    print("\nKako naj bodo zastavljena vprašanja?")
    print("  1) V slovenščini")
    print("  2) V tujem jeziku")
    choice = read_with_default("Vnos (1/2, privzeto 1): ", "1")

    if choice == "2":
        return 2
    else:
        return 1


def choose_level():
    """
    Stopnja težavnosti 1–5.
    1 = prvih 10 glagolov, 2 = prvih 20, ..., 5 = vseh 50.
    Privzeto 1.
    """
    print("\nIzberi težavnost (1–5):")
    print("  1) prvih 10 glagolov")
    print("  2) prvih 20 glagolov")
    print("  3) prvih 30 glagolov")
    print("  4) prvih 40 glagolov")
    print("  5) vseh 50 glagolov")

    while True:
        choice = read_with_default("Vnos (1–5, privzeto 1): ", "1")
        if choice.isdigit():
            level = int(choice)
            if 1 <= level <= 5:
                return level
        print(RED + "Neveljaven vnos. Poskusi znova (1–5)." + RESET)


def run_game(target_language, question_language_mode, level):
    """
    target_language: 'ITA' ali 'SPA'
    question_language_mode: 1 = vprašanje v SLO, odgovor v tujem;
                            2 = vprašanje v tujem, odgovor v SLO.
    level: 1–5 (koliko glagolov je v naboru).
    """
    max_verbs = min(level * 10, len(VERBS))
    verb_pool = VERBS[:max_verbs]

    print("\n=== Igra se začne! ===")
    print(f"Število vprašanj: {NUM_QUESTIONS}")
    print(f"Nabor glagolov: prvih {max_verbs} od 50\n")

    score = 0

    for i in range(1, NUM_QUESTIONS + 1):
        slo, ita, spa = random.choice(verb_pool)

        if target_language == "ITA":
            foreign = ita
        else:
            foreign = spa

        if question_language_mode == 1:
            # Vprašanje v slovenščini, odgovor v tujem jeziku
            question_word = slo
            correct_answer = foreign
        else:
            # Vprašanje v tujem jeziku, odgovor v slovenščini
            question_word = foreign
            correct_answer = slo

        print(f"Vprašanje {i}/{NUM_QUESTIONS}:")
        print(f"  Prevedi: '{question_word}'")
        user_answer = input("Tvoj odgovor: ").strip()

        if user_answer.lower() == correct_answer.lower():
            score += 1
            print(GREEN + "Pravilno! 🎉" + RESET)
            print('\a', end='')  # vesel zvok (če ga terminal podpira)
        else:
            print(RED + "Napačno. 😢" + " Pravilen odgovor je: " + YELLOW + correct_answer + RESET)
            print('\a', end='')  # žalosten zvok – isti beep, a dovolj za povratno informacijo

        print("-" * 40)

    print("\n=== Rezultat ===")
    print(f"Pravilnih odgovorov: {score} / {NUM_QUESTIONS}")
    percentage = score * 100 / NUM_QUESTIONS
    print(f"Uspešnost: {percentage:.1f}%")

    if percentage >= 80:
        print(GREEN + "Odlično, nadaljuj tako! 💪" + RESET)
    elif percentage >= 50:
        print(YELLOW + "Solidno, a je prostor za napredek. 😉" + RESET)
    else:
        print(RED + "Ni panike – vaja dela mojstra. Poskusi še enkrat! 🔁" + RESET)


def main():
    target_language = choose_language()
    question_language_mode = choose_question_language()
    level = choose_level()

    run_game(target_language, question_language_mode, level)


if __name__ == "__main__":
    main()
