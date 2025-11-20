# mini_phish.py — minimal phishing detector
import sys, os
from urllib.parse import urlparse
from sklearn.tree import DecisionTreeClassifier

# tiny training data: [length, has_https, has_at], label:1=legit,0=phish
X = [[20,1,0],[60,0,1],[30,1,0],[80,0,1],[25,1,0],[90,0,1]]
y = [1,0,1,0,1,0]
clf = DecisionTreeClassifier().fit(X,y)

def feat(u):
    p = urlparse(u if '://' in u else 'http://'+u)
    return [len(u), int(p.scheme=='https'), int('@' in u)]

def classify_file(path):
    with open(path,encoding='utf-8',errors='ignore') as f:
        for line in f:
            u=line.strip()
            if not u: continue
            r = clf.predict([feat(u)])[0]
            print(f"{path}\t{r}\t{u}")

if __name__=='__main__':
    if len(sys.argv)<2:
        print("usage: python mini_phish.py <file_or_folder>")
        sys.exit(1)
    p=sys.argv[1]
    if os.path.isdir(p):
        for root,_,files in os.walk(p):
            for fn in files:
                if fn.lower().endswith('.txt'):
                    classify_file(os.path.join(root,fn))
    else:
        classify_file(p)


# This script is a tiny, self-contained phishing URL detector: it trains a Decision Tree on a handful of example records
# (each record encodes three simple features — URL length, whether the scheme is https, and whether the URL contains an
#  @ symbol — with labels 1 = legitimate, 0 = phishing), then accepts a file or folder path on the command line and classifies 
# every URL it finds in .txt files (one URL per line). For each URL it builds the same three-feature vector by parsing the URL 
# with urlparse, asks the trained classifier for a prediction, and prints lines of the form source_path <tab> label <tab> url where 
# label is 1 (legit) or 0 (phish). To run it you need scikit-learn installed, save the code as mini_phish.py, make a text file of URLs,
# and run python mini_phish.py urls.txt (or pass a folder to process all .txt files inside). Note this is an educational toy — the 
# model uses very simple features and a tiny dataset, so it can demonstrate the idea but will not be reliable in real-world deployment 
# without many more examples and richer features (domain age, WHOIS, content analysis, etc.).