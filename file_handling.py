import os 
import json
import datetime

filename = "savefile.json"

def retrieve_high_scores():
    """Return a dict of names and the highscores. """
    high_scores = []
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            datas = json.load(f)
            for data in datas:
                high_scores.append(data)
    except:
        print("no highscores saved yet")
        return None
    high_scores.sort(key=lambda x: x['score'], reverse=True)
    return high_scores

def save_score(name, score):
    """Save a high score to file. """
    high_scores = [] 
    new_score = dict(name=name, score=score, time=str(datetime.datetime.now(tz=None)))

    if retrieve_high_scores() == None:
        high_scores.append(new_score)
        with open(filename, 'w+', encoding="utf-8") as f:
            json.dump(high_scores, f)
        return
    
    for entry in retrieve_high_scores():
        high_scores.append(entry)
    high_scores.append(new_score)

    with open(filename, 'w+', encoding="utf-8") as f:
        json.dump(high_scores, f)


def main():
    save_score("Taliban", 70)

if __name__ == "__main__":
    main()