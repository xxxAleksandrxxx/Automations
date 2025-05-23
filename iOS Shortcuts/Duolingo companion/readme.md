### DEV branch addition
It's an experimental branch that includes an extra feature: building a Flask app on a Gunicorn server with a REST API. From an Apple Shortcut (not shared yet), we send a request to the server with text extracted from a screenshot. The server cleans the text and sends it back to Apple Shortcuts, where the language is recognized and translated (to Spanish or English in my case). Both the original cleaned text and the translation are then sent back to the server, where another Python script concurrently converts the text to speech and sends both audio files back to the Apple Shortcut. Finally, on the iPhone, in the Apple Shortcut, we have the original text, the translation, and both audio files, allowing us to choose and pronounce any of them.


### Link to [RoutineHub (it's original one that works locally on iPhone)](https://routinehub.co/shortcut/16482/)


...  | 1 | 2 | ...
:--:| :--: | :--: | :--:
**Safari** | ![Imgur](https://i.imgur.com/ZuQ6Y6U.png) | ![Imgur](https://i.imgur.com/pQa6NQ2.png) | 
... | **1** | **2** | **3**
**DuoLingo** | ![Imgur](https://i.imgur.com/o3T5uos.png)  | ![Imgur](https://i.imgur.com/c7AtT0T.png) | ![Imgur](https://i.imgur.com/e0UIxrC.png)


I've been studying Spanish using English as my primary language (which technically isn't 😁) for over a year, and I've really enjoy DuoLingo. But there are couple of features I always wished to have:

- Pronunciation of sentences for each exercise.
- Listening to sentences in both Spanish and English.
- The ability to switch from Mexican Spanish to Spanish Spanish pronunciation.

So, I've created an iOS Shortcut companion to expand DuoLingo's functionality!


### How it works

During your Spanish class, you simply need to activate the shortcut (there are two different ways to do it) and select the language in which you'd like the sentence to be pronounced.

Example with Assistive Touch | Example with Back Tap
-- | --
[video](https://i.imgur.com/JuJgssH.mp4) | [video](https://i.imgur.com/9RWQMjA.mp4)


### Setup steps

1) Go to: Settings > Accessibility > Spoken Content > Voices  
2) Download voices you want to use  
3) Download "Duolingo en-es" shortcut and proceed setup steps  
4) Setup the way you want to run this shortcut - Assistive Touch or Back Tap  

**Setup Assistive Touch** | **Setup Back Tap**
-- | --
For the best experience with Assistive Touch, I would recommend downloading <a href='https://routinehub.co/shortcut/16439/'>this shortcut</a> first, as it will take you directly to the Assistive Touch settings. | With Back Tap, you can select either a double or triple tap, and when you need to run the shortcut, simply double or triple tap the back of your iPhone.   
[video](https://i.imgur.com/RaozjKX.mp4) | [video](https://i.imgur.com/pHmrPwO.mp4)

5) Start DuoLingo class and enjoy!   

### Notes

- Personally, I prefer Assistive Touch, as Back Tap may occasionally trigger the shortcut when it's not needed at all.

- Occasionally, the iOS recognition system may make errors and miss some letters. In such cases, you can try running the shortcut once or twice more, or simply move on.

- Certain exercises may contain more than one sentence. In such cases you'll be prompted to choose the correct number of sentences (3 max).

- If you activate the shortcut after you've answered and pressed "CHECK," the script will take the answer provided by DuoLingo and translate it. In certain instances, you might receive slightly different sentences (which is kind of cool feature to me).

- There are some exercises with sentences lacking punctuation marks at the end. In such cases, you may receive a sentence without proper structure. I haven't found a simple and straightforward solution for this, so you can either skip these exercises or modify the script's logic and share it – that would be greatly appreciated.

I hope you will enjoy using this shortcut!
