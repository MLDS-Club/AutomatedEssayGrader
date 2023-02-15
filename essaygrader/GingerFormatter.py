# essentially the same code except it uses nltk
# !pip install nltk
# !pip install gingerit
import nltk
# nltk.download('punkt')      # uncomment this if an error is thrown
import gingerit
import math 
from gingerit.gingerit import GingerIt

text = "Dear local newspaper, I think effects computers have on people are great learning skills/affects because they give us time to chat with friends/new people, helps us learn about the globe(astronomy) and keeps us out of troble! Thing about! Dont you think so? How would you feel if your teenager is always on the phone with friends! Do you ever time to chat with your friends or buisness partner about things."
text2 = text + "Above alll wee need to live in peace with the sitizen of megalovania"
text3 = "You @MONTH1 find this hard to beleive, but many people think compters put a negative attitude on people. Now you @MONTH1 be saying thats not true, that everyone has a computer, but the truth is they don't and they believe it puts negative attitude on people. People have many reasons for owning a computer and one is friends. Did you @CAPS5 some people own computers because they want to stay in touch with friends from differnt states who live far away. For example, many people use @CAPS1 or @CAPS2 to connect with friends. I can make a connection because I have both a @CAPS1 and @CAPS2 that I use to stay in contact with family friends from all over. Some people, like myself, even have friends from different countries! I @CAPS5 that many people want to learn about people from differnt countries and this is one way to do it right now I am learning some new things about the @LOCATION1 because I am friends with someone who lives in @LOCATION2. While on this wonderful adventure of learning you @MONTH1 even get yourself into a vacation adventure. A recent test was taking stating that @NUM1 out of @NUM2 people like to travel but don't @CAPS5 where. Some people say that people spend to much time on the computer but not enough enjoying nature.These people are wrong if one is on a computer and they are chating with someone from a differnt state or country then that person might persuade them to take a visit there. For example they would be able to go to the internet type in the place they want to visit and get photographs and information about the place. As a result, people would still get to enjoy nature. Sometimes using the computer could be educational. Many people @MONTH1 disagree with that statement but its true. For example when on the computer many people in their senior year of high school use it to take online college courses to get their degree because going to a regular college @MONTH1 affect their work scheduale. This could also help students in any grade learn more about the topic they are studing. It would also help them on their reports. For example they would be able to get pictures and other information anytime they wanted to. As a result, the students grades would increase. I hope many of you agree with my statement and help spread the word that computers could be positive on the mind. As a result for those who didn't agree with the statement that they are positive not negative I hope that you will redecide on your opion."
parser = GingerIt()
class GingerFormatter:
  def __init__(self, text):
    self.text = text 

  def supplementaryParser(self):
    maxWordCount = 300
    Corrections = []
    if len(self.text) > maxWordCount:
      split_sent = nltk.tokenize.sent_tokenize(self.text)
      split_text = []
      # editText = ""
      # for i in split_sent:

      #   if len(editText) > maxWordCount:
      #     if len(editText) + len(split_sent[i]) < maxWordCount:
      #       editText.append(text[i])
      #     elif len(editText) <= maxWordCount:
      #       split_text.append(editText)
      #       editText = ""
      #       i-=1



      for i in range(len(split_sent)):
        phrase = split_sent[i]
        parsed_l = parser.parse(phrase)
        Corrections.extend(parsed_l['corrections'])

      return Corrections

    else:
      x = parser.parse(text)
      return x

  def formatter(self, correct):
    self.correct = correct
    numErrors = len(self.correct)
    results = f"There are {numErrors} errors in your essay \n The corrections have been listed below \n"
    for i in range(len(self.correct)):
      resultSpecific = self.correct[i]
      results += f"{i+1}. \n"
      results += f"the mistake was: {resultSpecific['text']} \n"
      results += f"the correction way to have written this is: {resultSpecific['correct']}\n"
      results += "\n"
      if resultSpecific['definition'] != None:
        if resultSpecific['definition'] == 'Accept space':
          results += f"Reason: Add a space \n"
          results += "\n"
        elif resultSpecific['definition'] == 'Accept comma addition':
          results += f"Reason: A comma is missing (punctuation error) \n"
          results += "\n"
        else:
          results += f"Definition/ Reason: {resultSpecific['definition']} \n"
        results+= "\n"
    return results 


  
