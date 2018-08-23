#!/usr/local/bin/python2.7
# coding: utf-8

import boto3
translate = boto3.client("translate")
lang_flag_pairs = [("fr", "🇫🇷"), ("de", "🇩🇪"),
                   ("es", "🇪🇸"), ("pt", "🇵🇼"),
                   ("zh", "🇨🇳"), ("ar", "🕌"),
                   ("ja", "🇯🇵"), ("ru", "🇷🇺"),
                   ("it", "🇮🇹"), ("zh-TW", "🇹🇼"),
                   ("tr", "🇹🇷"), ("cs", "🇨🇿")]
for lang, flag in lang_flag_pairs:
    print(flag)
    print(translate.translate_text(
        Text="Hello, World",
        SourceLanguageCode="en",
        TargetLanguageCode=lang
    )['TranslatedText'])
