#word frequency counter
text = input("Enter a paragraph:\n")
text = text.lower()
for ch in ".,!?":
    text = text.replace(ch, "")
words = text.split()
counts = {}
for w in words:
    if w in counts:
        counts[w] = counts[w] + 1
    else:
        counts[w] = 1
sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_counts:
  print(word, "=", count)
    