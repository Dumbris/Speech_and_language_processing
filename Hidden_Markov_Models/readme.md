Exercises
9.1 Implement the Forward algorithm and run it with the HMM in Fig. 9.3 to compute
the probability of the observation sequences 331122313 and 331123312.
Which is more likely?
9.2 Implement the Viterbi algorithm and run it with the HMM in Fig. 9.3 to compute
the most likely weather sequences for each of the two observation sequences
above, 331122313 and 331123312.
9.3 Extend the HMM tagger you built in Exercise 10.?? by adding the ability to
make use of some unlabeled data in addition to your labeled training corpus.
First acquire a large unlabeled (i.e., no part-of-speech tags) corpus. Next, implement
the forward-backward training algorithm. Now start with the HMM
parameters you trained on the training corpus in Exercise 10.??; call this
model M0. Run the forward-backward algorithm with these HMM parameters
to label the unsupervised corpus. Now you have a new model M1. Test
the performance of M1 on some held-out labeled data.
9.4 As a generalization of the previous homework, implement Jason Eisner’s HMM
tagging homework available from his webpage. His homework includes a
corpus of weather and ice-cream observations, a corpus of English part-ofspeech
tags, and a very hand spreadsheet with exact numbers for the forwardbackward
algorithm that you can compare against.
