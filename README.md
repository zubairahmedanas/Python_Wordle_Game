# Python_Wordle_Game
Download this repo first.

You need to install **colorama**. (pip install colorama)

This package used for coloring the word

You need to create your own dataset of word before playing this game. I have downloaded the word set from here https://github.com/first20hours/google-10000-english


next task is to run the **convert_word.py** file. It will generate a file of 5 letter word.


After generating the word file lets play the game by running **play_wordle.py** file. 

Enjoy the game..!!!!!

In this repo there are multiple files Let's discuss about these.

You have already know what this **convert_word.py** file does.

Lets talk about **wordle.py** file. Here you will find multiple function. Each function has differant task. 

**attempt** function will input the letter.

**guess** function will guess the word with the secret word. it macthes letter with letter. 

**is_solved** check if it is solved or not.

**remaining_attempts** will calculate the count that user has left to guess the secret word.


Now lets talk about **play_wordle.py** file


Here **load_word_set** will load the data that was generated earlier.

we will draw a bounding box of the game using this function **draw_border_box** and colored the letter of the input by **convert_result_color**


## Result analysis:

If the letter is **Green** it means it is in the correct position of the word.

If the letter is **Blue** it means it is in the word but in the wrong position.

If the letter is **Red** it means the letter is not present in the word we are guessing.





















 

