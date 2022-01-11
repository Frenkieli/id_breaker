from rarfile import RarFile;
import threading;

letterArr = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T","U", "V", "W", "X", "Y", "Z"];
total = 100000000;
threadNum = 4;
threadHandle = int(total / threadNum);

def checkRar(password):
  try:
    with RarFile('lock.rar', 'r') as myrar:
      myrar.extractall(path="pack/", pwd=password);
      print('成功!!!!!!!!====>'+ password);
      exit();
  except:
    print("fail:" + password);
    return False
def gogoRun(letter, num):
  for i in range(threadHandle):
    id = letter + str(total + i + threadHandle * num);
    if(verifyID(id)):
      if(checkRar(id)):
        return True;
  print(str(num) + "結束: " + letter);
  
def verifyID(id):
  # 英文代號對應數值表（個位數乘以 9 加上十位數）
  alphaTable = {'A': 1, 'B': 10, 'C': 19, 'D': 28, 'E': 37, 'F': 46, 'G': 55, 'H': 64, 'I': 39, 'J': 73, 'K': 82, 'L': 2, 'M': 11, 'N': 20, 'O': 48, 'P': 29, 'Q': 38, 'R': 47, 'S': 56, 'T': 65, 'U': 74, 'V': 83, 'W': 21, 'X': 3, 'Y': 12, 'Z': 30};
  # 計算總和值
  sum = alphaTable[id[0]] + int(id[1]) * 8 + int(id[2]) * 7 + int(id[3]) * 6 + int(id[4]) * 5 + int(id[5]) * 4 + int(id[6]) * 3 + int(id[7]) * 2 + int(id[8]) * 1 + int(id[9])
  # 驗證餘數
  if sum % 10 == 0:
    return True;
  else:
    return False;

if(total % threadNum == 0):
  for j, letter in enumerate(letterArr):
    for i in range(threadNum):
      threading.Thread(target=gogoRun, args=(letter, i)).start();
else:
  print("數字無法整除");


