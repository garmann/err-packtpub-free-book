#!/usr/bin/env python3

from errbot import BotPlugin, botcmd
import packtparser

url = 'https://www.packtpub.com/packt/offers/free-learning'

def soup():
    """setup a http conntection only if this funtion is used
    rather than creating when the bots starts. 
    """
    soup = packtparser.soup_object(url)
    return soup


class Packtfree(BotPlugin):
    """displays the current free book from packtpub
    """

    @botcmd()
    def packtfree(self, msg, args):
        """all infos
        """
        return packtparser.parse_title(soup()) + '\n' + \
            packtparser.parse_picture_url(soup()) + '\n' + \
            '\n'.join(packtparser.parse_description(soup(), \
            packtparser.parse_title(soup()))) \
            + '\n' + url


    @botcmd()
    def packtfree_title(self, msg, args):
        """returns the book title
        """
        return packtparser.parse_title(soup())


    @botcmd()
    def packtfree_desc(self, msg, args):
        """returns description lines
        """
        return '\n'.join(packtparser.parse_description(soup(), \
            packtparser.parse_title(soup())))


    @botcmd()
    def packtfree_pic(self, msg, args):
        """returns image url
        """
        return packtparser.parse_picture_url(soup())


    @botcmd()
    def packtfree_url(self, msg, args):
        """ returns the url of the book
        """
        return url

