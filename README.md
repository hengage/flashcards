# flashcards

Traditional Django web app to aid study with flashcards, using the [spaced repetition system](https://en.wikipedia.org/wiki/Spaced_repetition)

### Clone the repo 
`git clone https://github.com/hengage/flashcards.git`

### Create and activate virtual environment 

To create: `python -m venv venv`

Activate it:
```
cd virualenv/scripts

activate 
```

Install dependencies/packages \
`pip install -r requirements.txt`

Features
- Create and edit cards
- Card moves to next box if solved, or previous box if not solved
- Archive card
- Custom template tags
