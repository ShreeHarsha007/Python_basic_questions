def count(line):
    words = line.split()
    return  len(words)
    # return count

def main():
    line = input(" Enter the sentence :")
    count1_ = count(line)
    print("the total number of words are :", count1_)
  
if __name__ == "__main__":
    main()