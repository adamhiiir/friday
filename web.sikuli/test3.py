Settings.OcrTextSearch = True
Settings.OcrTextRead = True
#開啟Chrome
App.open ("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
#等3秒
wait(3)
#貼上網址
paste("http://mall.beta.hiiir-inc.com/salecenter/index?saleNo=S00030785")
#按ENTER
type(Key.ENTER)
#等3秒
wait(3)
#選規格
click("1426234158660.png")
wait(1)
click("1426234273714.png")
click("1426235356381.png")
#畫面往下四格
for i in range(0,4):
 type(Key.DOWN)
#選贈品
click("1426234308351.png")
click("1426234330470.png")
wait(1)
click("1426234369166.png")
click("1426234389744.png")
click("1426234402276.png")
#畫面往下三格
for i in range(0,3):
 type(Key.DOWN)
#放入購物車
click("1426235917780.png")
wait(1)
click("1427170759702.png")
wait(2)
click("1427170822702.png")
wait(1)
click("1427170892201.png")
click(Pattern("1427170920978.png").targetOffset(23,0))
click("1427170982299.png")
#畫面往下6格
for i in range(0,6):
 type(Key.DOWN)
click("1427171026833.png")
wait(2)
click(Pattern("1427171108052.png").targetOffset(-41,-2))
#畫面往下6格
for i in range(0,6):
 type(Key.DOWN)
paste("1427171176282.png", "0912345678")
click("1427171211676.png")
#畫面往下10格
for i in range(0,10):
 type(Key.DOWN)
click("1427171597278.png")

wait(60)

#抓取本機螢幕要選擇範圍
a = find (Screen(0).capture(Region(294,471,240,13)))
#begin抓取上一行範圍的X,Y值當起始點，END抓取中心點
dragDrop(Location(294, 471),a)
#ctrl+C複製
type("c", KeyModifier.CTRL)
#等一秒才不會太快有時會失敗
wait(1)
#取得clipboard的值
b = Env.getClipboard().strip()    


#畫面往下20格
for i in range(0,20):
 type(Key.DOWN)

click("1427171472382.png")
wait(10)

c = find (Screen(0).capture(Region(98,512,222,13)))
dragDrop(Location(98, 512),c)
type("c", KeyModifier.CTRL)
wait(1)
d = Env.getClipboard().strip()    

click("1427275343201.png")


print b
print d

if b==d:
    print "PASS"
else:
    print "Fail"
    wait() 
   