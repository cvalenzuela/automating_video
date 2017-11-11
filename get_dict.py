'''
Get a word count of a transcript
'''

import argparse

def main(args):
  file = open(args.file)

  words = {}

  for line in file:
    split_line = line.split(' ')
    if (len(split_line) == 4):
      word = split_line[0]
      if word in words:
        words[word] = words[word] + 1
      else:
        words[word] = 1

  sorted_words = sorted(words.items(), key=lambda x: x[1])
  if(args.save):
    print(sorted_words)
  else:
    with open('word_count.txt', 'xt') as f:
      f.write(sorted_words)
      f.close()

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Get a word count of a video transcript')
  parser.add_argument('--file', type=str, help='The file to count the words of')
  parser.add_argument('--save', help='save', default=True)
  args = parser.parse_args()
  main(args)

