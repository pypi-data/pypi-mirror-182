#!pip install transformers gradio requests bs4 transformers googletrans==3.1.0a0 gensim==3.6.0 textblob gradio sentencepiece sentence_transformers newspaper3k

def summarize(input_eng):
    try:
        import requests
        from bs4 import  BeautifulSoup
        from googletrans import Translator
        import warnings
        warnings.filterwarnings("ignore")
        import warnings,logging
        warnings.simplefilter('ignore')
        logging.disable(logging.WARNING)
        # from transformers import pipeline
        # caption = pipeline('image-to-text')
        from transformers import pipeline
        #sentiment = pipeline("sentiment-analysis")
        from transformers import PegasusForConditionalGeneration, AutoTokenizer
        # tokenizer = AutoTokenizer.from_pretrained("google/pegasus-xsum")
        from transformers import PegasusForConditionalGeneration, PegasusTokenizer
        from transformers import PegasusForConditionalGeneration, AutoTokenizer
        tokenizer = AutoTokenizer.from_pretrained("google/pegasus-xsum")
        # tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")
        model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")
        from sentence_transformers import SentenceTransformer
        #sbert_model = SentenceTransformer('bert-base-nli-mean-tokens')
        # from transformers import pipeline
        # sentiment = pipeline("sentiment-analysis")
        from transformers import PegasusForConditionalGeneration, AutoTokenizer
        tokenizer = AutoTokenizer.from_pretrained("google/pegasus-xsum")
        warnings.filterwarnings("ignore")
        # from gensim.summarization.summarizer import summarize
        from gensim.summarization import keywords
        from textblob import TextBlob
        translator = Translator()
        # from transformers import pipeline
        # summarizer = pipeline("summarization")
        from transformers import PegasusForConditionalGeneration, PegasusTokenizer
        from transformers import PegasusForConditionalGeneration, AutoTokenizer
        tokenizer = AutoTokenizer.from_pretrained("google/pegasus-xsum")
        # tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")
        model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")
        translation=translator.translate(input_eng, dest = "en")
        tokens = tokenizer(translation.text, truncation=True, padding="longest", return_tensors="pt")
        # Summarize 
        summary = model.generate(**tokens)
        # Decode summary
        text = tokenizer.decode(summary[0]).replace("<pad> ","").replace("</s>","")
       
        return {"Summary":text.strip()}

    except Exception as e:
      raise e 


# input_eng = input()
# summarize(input_eng)
# import gradio as gr   
# interface = gr.Interface(fn=summarize, 
#                          inputs=gr.inputs.Textbox(lines=20, placeholder='Past your  input text...'),outputs=['text',"text","text"])
# interface.launch(share = True, debug = False)
# https://www.voanews.com/
def get_summary_multioutput():
  import warnings
  warnings.filterwarnings("ignore")
  import pandas as pd
  import requests
  import nltk
  nltk.download('punkt')
  from bs4 import BeautifulSoup
  import urllib
  import numpy as np
  # from PIL import Image
  from IPython.display import Image, display
  from transformers import pipeline
  # caption = pipeline('image-to-text')
  import requests
  from bs4 import BeautifulSoup
  # url = "https://www.andhrajyothy.com/andhra-pradesh"
  # req = requests.get(url)
  # soup = BeautifulSoup(req.content,"html.parser")
  from newspaper import Article
  # article = Article(input("Enter article URL :"))
  # article.download()
  # article.parse()
  # article.nlp()
  import shutil
  import os
  try:
    for i in os.listdir("."):
      # print(i.split(".")[-1])
      if i == ".config" or i == "sample_data" or i == "rlms.py" or i == "__pycache__":
          continue
      try:
        os.remove(i)
      except:
            shutil.rmtree("__pycache__")

  except Exception as e:
    pass
    # if i.split(".")[-1] == "png" or i.split(".")[-1] == "jpg":
    #         print(i)
  url = input("Enter article URL :")
  
  im = []
    
  import requests
  from bs4 import BeautifulSoup
  import pandas as pd
    
  req = requests.get(url)
  # print(req)
  soup = BeautifulSoup(req.content,"html.parser")
  text = ""
  for i in soup.findAll("div",{"class":"wsw"}):
      for j in i.findAll("p"):
          text+=j.text.strip()
      # print(text)
  for k in soup.findAll("div",{"class":"img-wrap"}):
      for l in k.findAll("div",{"class":"thumb thumb16_9"}):
          for m in l.findAll("img"):
              im.append(m.get("src"))
      for n in k.findAll("div",{"class":"thumb"}):
          for o in n.findAll("img"):
              im.append(o.get("src"))
  imgs = len(im)
  show = np.random.choice([0,imgs-1])
  def _downloadimages():
    # url = input("enter imags urls with , speprated :")
    for j,i in enumerate(im):
      urllib.request.urlretrieve(i, f"{j}.jpg") 
  _downloadimages()
  # input_eng = input("enter ur input text :")
  # def show_img():
  #    display(Image(f'/content/{show}.jpg',width=500, height=250))
  # {"Caption":caption(f"{show}.jpg")[0]["generated_text"]}
  return summarize(text[:1500].strip()), display(Image(f'{show}.jpg',width=500, height=250))
