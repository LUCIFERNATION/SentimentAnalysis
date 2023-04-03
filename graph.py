import matplotlib.pyplot as plt

#polarités des reviews
sentiments = [0.4666666666666666, 0.331060606060606, 0.21507575757575756, 0.1098428731762065, 0.29678030303030295, 0.09909090909090909, -0.4000000000000001, 0.07762923351158649, 0.13690476190476192, 0.2303030303030303]

positive_count = 0
negative_count = 0
neutral_count = 0

for sentiment in sentiments:
    if sentiment > 0.2:
        positive_count += 1
    elif sentiment < -0.2:
        negative_count += 1
    else:
        neutral_count += 1


total_count = len(sentiments)
positive_sent = (positive_count / total_count) * 100
negative_sent = (negative_count / total_count) * 100
neutral_sent = (neutral_count / total_count) * 100

sents = [positive_sent, negative_sent, neutral_sent]
labels = ['Positive', 'Negative', 'Neutral']
plt.bar(labels, sents, color=['green', 'red', 'gray'])

#chaque type de sentiment
for i, sent in enumerate(sents):
    plt.text(i, sent + 1, f"{sent:.1f}%", ha='center')
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment Type")
plt.ylabel("Percentage")

#le graphe
plt.show()