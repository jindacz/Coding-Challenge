def rev(s):
    
    return " ".join(s.split(" ")[::-1])

print(rev("The weather is amazing today!") == "today! amazing is weather The")