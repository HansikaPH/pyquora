import urllib2
from lxml import etree

####################################################################
# API
####################################################################

class Scrape_Quora:

    regexpNS = "http://exslt.org/regular-expressions"

    @staticmethod
    def get_name(user_name):
        url = 'https://www.quora.com/profile/' + user_name
        response = urllib2.urlopen(url)
        htmlparser = etree.HTMLParser()
        tree = etree.parse(response, htmlparser)
        name = tree.xpath('//*[re:test(@id, "ld_[a-z]+_\\d+", g)]/div/h1/span/text()', namespaces={'re':Scrape_Quora.regexpNS})[0]
        return name

    @staticmethod
    def get_url(user_name):
        url = 'https://www.quora.com/profile/' + user_name
        response = urllib2.urlopen(url)
        URL = response.geturl()
        return URL

    @staticmethod
    def get_profile_picture_link(user_name):
        url = 'https://www.quora.com/profile/' + user_name
        response = urllib2.urlopen(url)
        htmlparser = etree.HTMLParser()
        tree = etree.parse(response, htmlparser)
        profile_picture_link = tree.xpath('//*[re:test(@id, "ld_[a-z]+_\\d+", g)]/div/img/@data-src', namespaces={'re':Scrape_Quora.regexpNS})[0]
        return profile_picture_link

    @staticmethod
    def get_no_of_questions(user_name):
        url = 'https://www.quora.com/profile/' + user_name
        response = urllib2.urlopen(url)
        htmlparser = etree.HTMLParser()
        tree = etree.parse(response, htmlparser)
        no_of_questions = tree.xpath('//*[re:test(@id, "ld_[a-z]+_\\d+", g)]/li/a[text()="Questions"]/span/text()', namespaces={'re':Scrape_Quora.regexpNS})[0]
        return no_of_questions

    @staticmethod
    def get_no_of_answers(user_name):
        url = 'https://www.quora.com/profile/' + user_name
        response = urllib2.urlopen(url)
        htmlparser = etree.HTMLParser()
        tree = etree.parse(response, htmlparser)
        no_of_answers = tree.xpath('//*[re:test(@id, "ld_[a-z]+_\\d+", g)]/li/a[text()="Answers"]/span/text()', namespaces={'re':Scrape_Quora.regexpNS})[0]
        return no_of_answers

    @staticmethod
    def get_no_of_followers(user_name):
        url = 'https://www.quora.com/profile/' + user_name
        response = urllib2.urlopen(url)
        htmlparser = etree.HTMLParser()
        tree = etree.parse(response, htmlparser)
        no_of_followers = tree.xpath('//*[re:test(@id, "ld_[a-z]+_\\d+", g)]/li/a[text()="Followers "]/span/text()', namespaces={'re':Scrape_Quora.regexpNS})[0]
        return no_of_followers

    @staticmethod
    def get_no_of_following(user_name):
        url = 'https://www.quora.com/profile/' + user_name
        response = urllib2.urlopen(url)
        htmlparser = etree.HTMLParser()
        tree = etree.parse(response, htmlparser)
        no_of_following = tree.xpath('//*[re:test(@id, "ld_[a-z]+_\\d+", g)]/li/a[text()="Following "]/span/text()', namespaces={'re':Scrape_Quora.regexpNS})[0]
        return no_of_following

    @staticmethod
    def get_no_of_edits(user_name):
        url = 'https://www.quora.com/profile/' + user_name
        response = urllib2.urlopen(url)
        htmlparser = etree.HTMLParser()
        tree = etree.parse(response, htmlparser)
        no_of_edits = tree.xpath('//*[re:test(@id, "ld_[a-z]+_\\d+", g)]/li/a[text()="Edits"]/span/text()', namespaces={'re':Scrape_Quora.regexpNS})[0]
        return no_of_edits
