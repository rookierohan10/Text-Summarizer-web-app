import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

text = """In 2018, twenty-three days after Thanos erased half of all life in the universe,[a] Carol Danvers rescues Tony Stark and Nebula from deep space and they reunite with the remaining Avengers—Bruce Banner, Steve Rogers, Thor, Natasha Romanoff, and James Rhodes—and Rocket on Earth. Locating Thanos on an uninhabited planet, they plan to use the Infinity Stones to reverse his actions, but discover Thanos has already destroyed them to prevent further use. Enraged, Thor decapitates Thanos.

Five years later, Scott Lang escapes from the Quantum Realm.[b] Reaching the Avengers Compound, he explains that he experienced only five hours while trapped. Theorizing that the Quantum Realm allows time travel, they ask a reluctant Stark to help them retrieve the Stones from the past to reverse the actions of Thanos in the present. Stark, Rocket, and Banner, who has since merged his intelligence with the Hulk's strength, build a time machine. Banner notes that altering the past does not affect their present; any changes create alternate realities. Banner and Rocket travel to Norway, where they visit the Asgardian refugees' settlement New Asgard and recruit an overweight and despondent Thor. In Tokyo, Romanoff recruits Clint Barton, who became a vigilante after his family was erased during the execution of Thanos' plan.[a]

Banner, Lang, Rogers, and Stark time-travel to New York City during Loki's attack in 2012.[c] At the Sanctum Sanctorum, Banner convinces the Ancient One to give him the Time Stone after promising to return the various Stones to their proper points in time. At Stark Tower, Rogers retrieves the Mind Stone from Hydra sleeper agents, but Stark and Lang's attempt to steal the Space Stone fails, allowing 2012-Loki to escape with it. Rogers and Stark travel to Camp Lehigh in 1970, where Stark obtains an earlier version of the Space Stone and encounters his father, Howard. Rogers steals Pym Particles from Hank Pym to return to the present and spies his lost love, Peggy Carter.

Meanwhile, Rocket and Thor travel to Asgard in 2013;[d] Rocket extracts the Reality Stone from Jane Foster, while Thor gets encouragement from his mother, Frigga, and retrieves his old hammer, Mjolnir. Barton, Romanoff, Nebula, and Rhodes travel to 2014; Nebula and Rhodes go to Morag and steal the Power Stone before Peter Quill can,[e] while Barton and Romanoff travel to Vormir. The Soul Stone's keeper, Red Skull, reveals it can only be acquired by sacrificing a loved one. Romanoff sacrifices herself, allowing Barton to get the Stone. Rhodes and Nebula attempt to return to their own time, but Nebula is incapacitated when her cybernetic implants link with her past self, allowing 2014-Thanos to learn of his future self's success and the Avengers' attempt to undo it. 2014-Thanos sends 2014-Nebula forward in time to prepare for his arrival.

Reuniting in the present, the Avengers place the Stones into a gauntlet that Stark, Banner, and Rocket have built. Having the most resistance to their radiation, Banner wields the gauntlet and reverses Thanos's disintegrations. Meanwhile, 2014-Nebula, impersonating her future self, uses the time machine to transport 2014-Thanos and his warship to the present, which he then uses to destroy the Avengers Compound. Present-day Nebula convinces 2014-Gamora to betray Thanos, but is unable to convince 2014-Nebula and kills her. Thanos overpowers Stark, Thor, and a Mjolnir-wielding Rogers and summons his army to retrieve the Stones, intent on using them to destroy the universe and create a new one. A restored Stephen Strange arrives with other sorcerers, the restored Avengers and Guardians of the Galaxy, the Ravagers, and the armies of Wakanda and Asgard to fight Thanos's army. Danvers also arrives and destroys Thanos's warship, but Thanos overpowers her and seizes the gauntlet. Stark steals the Stones and uses them to disintegrate Thanos and his army, at the cost of his life.

Following Stark's funeral, Thor appoints Valkyrie as the new king of New Asgard and joins the Guardians. Rogers returns the Stones and Mjolnir to their proper timelines and remains in the past to live with Carter. In the present, an elderly Rogers passes his shield to Sam Wilson."""

stopwords = list(STOP_WORDS)
print(stopwords)

nlp = spacy.load('en_core_web_sm')
doc = nlp(text)
doc

tokens = [token.text for token in doc]
tokens

word_freq = {}
for word in doc:
  if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
    if word.text not in word_freq.keys():
      word_freq[word.text] = 1
    else:
      word_freq[word.text] += 1

word_freq

max_freq = max(word_freq.values())
max_freq

for word in word_freq.keys():
  word_freq[word] = word_freq[word]/max_freq

word_freq

sent_tokens = [sent for sent in doc.sents]
sent_tokens

sent_scores = {}
for sent in sent_tokens:
  for word in sent:
    if word.text in word_freq.keys():
      if sent not in sent_scores.keys():
        sent_scores[sent] = word_freq[word.text]
      else:
        sent_scores[sent] += word_freq[word.text]

sent_scores

select_len = int(len(sent_tokens) * 0.3)
select_len

summary = nlargest(select_len, sent_scores, key=sent_scores.get)
print(summary)

final_summary = [word.text for word in summary]
summary = ' '.join(final_summary)
summary

print('Length of original text',len(text.split(' ')))
print('Length of summarized text',len(summary.split(' ')))