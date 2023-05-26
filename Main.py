from flask import Flask, render_template, request, url_for, redirect
import googletrans
from googletrans import Translator


languages = googletrans.LANGUAGES

# keys = languages.keys()
# values = languages.values()


# print(keys)
# print(values)

app = Flask(__name__)
translator = Translator()
# translated_text = translator.detect('memento mori')
# print(translated_text.lang)



@app.route('/')
def home():
    return render_template('index.html',languages = languages)

@app.route('/', methods=["POST", "GET"])
def methodTranslation():
   if request.method == "POST":
      Trnslate = request.form["translating"]
      LangSRC = request.form["LanguageSRC"]
      LangDST = request.form["LanguageDST"]
      if LangSRC == "AUTO":
         Lang = translator.detect(Trnslate)
         Detect = Lang.lang
         Trnslated = translator.translate(Trnslate ,LangDST, Detect)
         T = Trnslated.text
         return render_template('index.html',languages=languages, tralatingtext = Trnslate, keySRC=LangSRC, valueSRC=languages[Detect], keyDST=LangDST, valueDST=languages[LangDST], tralatedtext=T)

      else:
         Trnslated = translator.translate(Trnslate ,LangDST, LangSRC)
         T = Trnslated.text
         return render_template('index.html',languages=languages, tralatingtext = Trnslate, keySRC=LangSRC, valueSRC=languages[LangSRC], keyDST=LangDST, valueDST=languages[LangDST], tralatedtext=T)

      


      
   else :
      return render_template("")


if __name__ == '__main__':
   app.run()