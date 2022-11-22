import wikipedia
import summarizer
import re
def generate(inputUrl,percent):
  listUrl=inputUrl.split("/")[-1:]
  finalUrl=listUrl[0]
  extractedText = wikipedia.page(finalUrl).content
  cleanText= re.sub("\n","",extractedText)
  finalText = re.split("=+=+",cleanText)
  count=1
  with open('output.txt', 'w',encoding='utf-8') as f:
      f.write('')
      
      for i in finalText:
        if(len(i)>30):
          result=summarizer.summarize(i,percent)
          if(len(result)!=0):
            f.write('\n')
            f.write(result+'\n')
            
          else:
            f.write('\n')
            f.write(i)


        else:
          f.write("\n")
          if(i==' See also '):
            break
          if(len(finalText[count])!=0):
            f.write('\n')
            f.write(i)
            f.write('\n')
            f.write("-"*len(i))
        count+=1
print("file is ready")


    