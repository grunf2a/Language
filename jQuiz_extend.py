#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

# uvoz slovarja
from vocab import CATEGORIES

# ANSI barve za konzolo
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

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
    1 = Italijanščina, 2 = Španščina, 3 = Angleščina
    Privzeto 1.
    """
    print("=== Nastavitve ===")
    print("Izberi jezik za učenje:")
    print("  1) Italijanščina (ITA)")
    print("  2) Španščina (ŠPA)")
    print("  3) Angleščina (ENG)")
    choice = read_with_default("Vnos (1/2/3, privzeto 1): ", "1")

    if choice == "2":
        return "SPA"
    elif choice == "3":
        return "ENG"
    else:
        return "ITA"


def choose_question_language():
    """
    1 = vprašanja v slovenščini, 2 = v tujem jeziku
    Privzeto 1.
    """
    print("\nKako naj bodo zastavljena vprašanja?")
    print("  1) V slovenščini (odgovor v tujem jeziku)")
    print("  2) V tujem jeziku (odgovor v slovenščini)")
    choice = read_with_default("Vnos (1/2, privzeto 1): ", "1")

    if choice == "2":
        return 2
    else:
        return 1


def choose_category():
    """
    Izbira vsebinskega sklopa (1–8).
    Skupine so definirane v vocab.CATEGORIES.
    """
    print("\nIzberi vsebinski sklop:")
    for key in sorted(CATEGORIES.keys()):
        name, _ = CATEGORIES[key]
        print(f"  {key}) {name}")

    while True:
        choice = read_with_default("Vnos (številka sklopa, privzeto 1): ", "1")
        if choice.isdigit():
            cat = int(choice)
            if cat in CATEGORIES:
                return cat
        print(RED + "Neveljaven vnos. Poskusi znova." + RESET)


def choose_level():
    """
    Stopnja težavnosti 1–10.
    Vsaka stopnja doda 10 možnih besed (če obstajajo).
    Privzeto 1.
    """
    print("\nIzberi težavnost (1–10):")
    print("  1) prvih 10 besed")
    print("  2) prvih 20 besed")
    print("  ...")
    print(" 10) prvih 100 besed (ali največ, kolikor jih skupina vsebuje)")

    while True:
        choice = read_with_default("Vnos (1–10, privzeto 1): ", "1")
        if choice.isdigit():
            level = int(choice)
            if 1 <= level <= 10:
                return level
        print(RED + "Neveljaven vnos. Poskusi znova (1–10)." + RESET)


def run_game(target_language, question_language_mode, category_key, level):
    """
    target_language: 'ITA', 'SPA' ali 'ENG'
    question_language_mode:
        1 = vprašanje v SLO, odgovor v tujem jeziku
        2 = vprašanje v tujem jeziku, odgovor v SLO
    category_key: ključ iz CATEGORIES (1–8)
    level: 1–10 (koliko besed izbrati iz skupine)
    """
    category_name, word_list = CATEGORIES[category_key]

    # Koliko besed vzamemo glede na stopnjo
    max_words = min(level * 10, len(word_list))
    word_pool = word_list[:max_words]

    print("\n=== Igra se začne! ===")
    print(f"Jezik za učenje: {target_language}")
    print(f"Vsebinski sklop: {category_name}")
    print(f"Število vprašanj: {NUM_QUESTIONS}")
    print(f"Nabor besed: prvih {max_words} od {len(word_list)} v skupini\n")

    score = 0

    for i in range(1, NUM_QUESTIONS + 1):
        slo, ita, spa, eng = random.choice(word_pool)

        # kaj pomeni "tuj jezik" v tej igri
        if target_language == "ITA":
            foreign = ita
        elif target_language == "SPA":
            foreign = spa
        else:  # ENG
            foreign = eng

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
            print(GREEN + "Pravilno! 🎉" + RESET + " Pravilen odgovor je: " + correct_answer)
            print('\a', end='')  # vesel zvok (če ga terminal podpira)
        else:
            print(
                RED + "Napačno. 😢" + RESET +
                " Pravilen odgovor je: " + YELLOW + correct_answer + RESET
            )
            print('\a', end='')  # žalosten zvok – isti beep

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
    category_key = choose_category()
    level = choose_level()

    run_game(target_language, question_language_mode, category_key, level)


if __name__ == "__main__":
    main()

