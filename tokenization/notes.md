Tokenization

- Tokenization = text ko chhote units (tokens) mein todna
- Word tokenization vs Sentence tokenization
- spaCy ka nlp(paragraph) call karte hi automatic tokenization ho jati hai
- doc ek special spaCy object hai, plain list nahi

- Key observation

- spaCy sirf apostrophe pe depend nahi karta split karne ke liye
- "dont" aur "don't" dono "do" + "nt"/"n't" mein split hue
- spaCy ke andar English ki common informal spellings ke

- Practice 

- Did a word and sentence tokenization on a different paragraph
- dont vs don't ka farak test kiya