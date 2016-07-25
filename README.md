# errbot-packtpub-free-book

this is a plugin for errbot which returns information about the current free book from packtpub

## install
- setup & use virtualenv
- pip install -r requirements.txt
- install plugin with: !repos install https://github.com/garmann/err-packtpub-free-book
- exmaple:
```
 >>> !repos install https://github.com/garmann/err-packtpub-free-book
Installing https://github.com/garmann/err-packtpub-free-book...
A new plugin repository has been installed correctly from https://github.com/garmann/err-packtpub-free-book. Refreshing the plugins commands...
Plugins reloaded.
```

## usage
- see !help
- !packtfree (all informations, see screenshot)
- !packtfree url (url of daily event)
- !packtfree desc (description)
- !packtfree title (title of book)
- !packtfree pic (image url)
- example:
```
 >>> !packtfree title
Skill Up 2016: Developer Skills Report
```

![alt text](https://github.com/garmann/err-packtpub-free-book/raw/master/example.png "logo")
