import tkinter.filedialog
import os
import json

adofaiMapDir = ""

def AdofaiMapFinder():
    global adofaiMapDir
    adofaiMapDir = tkinter.filedialog.askopenfilename(initialdir="/", title="얼불춤 맵을 선택해주세요.", filetypes=(("Adofai file", "*.adofai"),))
    
    if adofaiMapDir != "" or adofaiMapDir.split(".")[-1] != "adofai":
        print(f"\"{adofaiMapDir}\" 파일이 입력되었습니다.")
    else:
        AdofaiMapFinder()

AdofaiMapFinder()

fileDir, fileName = os.path.split(adofaiMapDir) # 디렉토리, 파일명 분리
fileName, fileExt = os.path.splitext(fileName) # 파일명, 파일 확장자 분리

with open(adofaiMapDir, "r", encoding="utf-8-sig") as fr:
    data: dict = json.loads(fr.read()
                            .replace(", }", " }")
                            .replace(",  }", " }")
                            
                            .replace('false', '"Disabled"')
                            .replace('true', '"Enabled"')
                            
                            .replace('"legacyFlash": "Disabled"', '"legacyFlash":  false')
                            .replace('"legacyCamRelativeTo": "Disabled"', '"legacyCamRelativeTo":  false')
                            .replace('"legacySpriteTiles": "Disabled"', '"legacySpriteTiles": false')
                            
                            .replace('"legacyFlash": "Enabled"',' "legacyFlash":  true')
                            .replace('"legacyCamRelativeTo": "Enabled"', '"legacyCamRelativeTo":  true')
                            .replace('"legacySpriteTiles": "Enabled"', '"legacySpriteTiles": true')
    )
    
    print("변환 완료")
    
    with open(f"{fileDir}/{fileName}_Full{fileExt}", "w", encoding="utf-8-sig") as fw:
        json.dump(data, fw, indent=4, ensure_ascii=False)