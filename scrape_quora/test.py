from pyquora import Scrape_Quora

user_names = ['Tapasweni-Pathak', 'Richard-Muller-3', 'Jay-Wacker', 'Hansika-Hewamalage', 'Hansika-Hewamalage-1', 'Hansika-Hewamalage-2']

for user_name in user_names:

    print "When the user name is " + user_name + ","

    print "Name of the user: " + Scrape_Quora.get_name(user_name)

    print "URL of the user profile: " + Scrape_Quora.get_url(user_name)

    print "Profile picture link of the profile: " + Scrape_Quora.get_profile_picture_link(user_name)

    print "Number of questions: " + Scrape_Quora.get_no_of_questions(user_name)

    print "Number of answers: " + Scrape_Quora.get_no_of_answers(user_name)

    print "Number of followers: " + Scrape_Quora.get_no_of_followers(user_name)

    print "Number of following: " + Scrape_Quora.get_no_of_following(user_name)

    print "Number of edits: " + Scrape_Quora.get_no_of_edits(user_name)

    print "\n"

