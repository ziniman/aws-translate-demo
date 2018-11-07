#!/usr/local/bin/python2.7
# coding: utf-8

import boto3
import argparse

# command line arguments
parser = argparse.ArgumentParser(description='Translate text to all possible languages supported by Amazon Translate')
parser.add_argument('text_to_translate', default='Hello, World', nargs='?', help='Text to translate (default=\"Hello, World\")')
args = parser.parse_args()
#print(args)

translate = boto3.client("translate")
lang_flag_pairs = [("fr", "🇫🇷"), ("de", "🇩🇪"),
                   ("es", "🇪🇸"), ("pt", "🇵🇹"),
                   ("zh", "🇨🇳"), ("ar", "🕌"),
                   ("ja", "🇯🇵"), ("ru", "🇷🇺"),
                   ("it", "🇮🇹"), ("zh-TW", "🇹🇼"),
                   ("tr", "🇹🇷"), ("cs", "🇨🇿")]
for lang, flag in lang_flag_pairs:
    print(flag)
    print(translate.translate_text(
        Text=args.text_to_translate,
        SourceLanguageCode="en",
        TargetLanguageCode=lang
    )['TranslatedText'])
