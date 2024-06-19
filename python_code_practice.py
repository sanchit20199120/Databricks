# count words in each line

def count_words_in_line(file_path):
  try:
    
    with open(file_path,'r') as file:
      lines = file.readlines()  # will create a list of lines
      print(lines)
      for line in lines:
        word_count = line.split(',')   # split the word in line 1 in list
        print(word_count)
      for index, count in enumerate(word_count):    
        print(f"{index+1},len(count))
  
  except FileNotFoundError:
    print(f" The file at {file_path} was not found.")


count_words_in_line ('File_path')

      
    
                        
      
