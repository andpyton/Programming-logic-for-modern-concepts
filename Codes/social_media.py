# Building a system that analizes engagement data
# using python dictionaries.

# 1 - Calculate an engagement score for each post.
# The equation for calculate is: 
# engagement_score = likes + (comments × 2) + (shares × 3)

# 2 - Store the results in a new dictionary, where:
# Key -> postID , value -> Engagement score

# 3 - Find the most engaging post
# Identify the post with the highest engagement score
# Prit its ID and score.

posts = {

    "post_001":{"likes": 120, "comments": 30, "shares": 15},
    "post_002":{"likes": 95, "comments": 12, "shares": 8},
    "post_003":{"likes": 1, "comments": 2, "shares": 45},
    "post_004":{"likes": 50, "comments":5, "shares": 200}
}

def calculating_engagement_score(D):  # D is a nested dictionary...

    new_dictionary = {}

    for post, data in D.items():

        engagement_score = data.get("likes") + (2*(data.get("comments"))) + (3*(data.get("shares")))
        
        new_dictionary[post] = engagement_score
    
    return new_dictionary

new_Dict = calculating_engagement_score(posts)
print(f'Dictionary with results is: {new_Dict}')

def most_engagement_post(ND): # ND is new dict...

    highest_score = 0

    for key, value in ND.items():

        if (value>highest_score):
            highest_score = value
            best_post = key  # name of the winner post

    return best_post, highest_score


name_post, score_post = most_engagement_post(new_Dict)
print(f'The winner of post is: {name_post} with {score_post} scores.')








