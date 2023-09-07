# Description
Duolingo companion iOS Shortcut designed for assistance during classes. The idea is to extract sentence from screen, translate it and provide possibility to listen both languages.  
To do so we need:
- take screenshot
- recognise text
- clean text from "trash"

First two steps are easy but the last one is tricky in iOS Shortcuts. I played around the logic and came across that the best way is to use ReGex in two steps:  
1. delete trash before the text  
2. delete trash after the text  

For both cases I found useful to use dictionary with words for ReGex. Keys are for searching in text and if the key exists in text ReGex Match applied for text to clean it.  
There are three ways how to manage trash words dictionaries:  
1. keep it inside Shortcut
	\+ all in one place  
	\+ simple for user  
	\+ it's possible to arrange key-value sequence  
	\- iOS Shortcuts application freezes when it has many boxes and, what is weird when dictionary has more then 30 items so it's really painful to add one more pair of key and value  
2. keep in locally on iPhone in text file using json structure  
	\+ no freezes during updating dictionary  
	\- tricky to share the dictionary with others  
	\- it's not possible to arrange key-value sequence  
	\- potentially could works slower because of we need to read the file and then sort keys  
3. keep it on the cloud (GitHub)  
	\+ no freezes during updating dictionary  
	\+ easy to share with others  
	\- the speed depends on internet connection  
	\- it's not possible to arrange key-value sequence  
	\- potentially could works slower because we need to get it from internet and then sort keys 

I tested all three variants, but in the end, I chose the third option primarily due to the buggy iOS Shortcuts app and its simplicity when it comes to sharing the dictionaries.

- dict_before.json  
	It has keys and values in style "_Translate this sentence " : "Translate this sentence "  
- dict_after.json  
	It has keys and values in style "_ JNEXT" : " JNEXT"  

Both dictionaries have "\_" as the first symbol in the key to ensure correct sorting. For example, keys like " F " and "F " remain in the same position after sorting in iOS Shortcuts like if there is no first space in " F. " However, with "_ F " and "\_F ," the first space is counted during sorting which is why both keys end up in different positions.