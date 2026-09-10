# codeAlpha_language-_translation-tool
!pip install translators gTTS
from gtts import gTTS
from IPython.display import Audio, display
import translators as t
languages = {
    '1': ('English', 'en'),
    '2': ('Arabic', 'ar'),
    '3': ('French', 'fr'),
    '4': ('German', 'de'),
    '5': ('Spanish', 'es'),
}


def run_translation_tool():
  print('==================================================')
  print('🌐 AI Language Translation Tool (CodeAlpha Task 1)')
  print('==================================================\n')

  # إدخال النص
  text_to_translate = input('👉 Enter the text you want to translate: ')

  if not text_to_translate.strip():
    print('⚠️ Text cannot be empty!')
    return

  # اختيار اللغة Target
  print('\nSelect Target Language:')
  for key, (name, code) in languages.items():
    print(f'{key}. {name}')

  choice = input('\nEnter option number (default is 1 for English): ')
  target_lang = languages.get(choice, ('English', 'en'))[1]

  print('\n⏳ Translating, please wait...')

  try:
    
        query_text=text_to_translate,
        translator='bing',
        from_language='auto',
        to_language=target_lang,
    )

    print('\n--------------------------------------------------')
    print(f'✅ Translation Result:\n{translated_text}')
    print('--------------------------------------------------')

    # توليد الصوت تلقائياً وتشغيله
    tts = gTTS(text=str(translated_text), lang=target_lang)
    audio_file = 'translated_audio.mp3'
    tts.save(audio_file)

    print('\n🔊 Playing Audio Output:')
    display(Audio(audio_file, autoplay=True))

  except Exception as e:
    print(f'\n❌ Error during translation: {e}')


# تشغيل الأداة
run_translation_tool()
