
import time
import pyautogui
import random
import os


def writeSleepEnter(typedString):
    pyautogui.write(typedString)
    time.sleep(round(random.uniform(0, 1), 10))
    # pyautogui.press('enter')


def sleepRandom(smallInt, largeInt):
    sleep = round(random.uniform(smallInt, largeInt), 10)
    print(formatHumanTimeString(sleep))
    time.sleep(sleep)


def formatHumanTimeString(seconds):
    timeLeftMin = round((seconds) // 60)
    timeLeftSec = ("0" if ((seconds) % 60) <
                   10 else "") + str(round(seconds % 60, 5))
    return str(timeLeftMin) + ":" + str(timeLeftSec)


wordCount = input("Hover over text box location ")
mainLocation = pyautogui.position()
wordCount = input("Hover over sell button location ")
sellbutton = pyautogui.position()

itemsToSell = ['QXH-9TX7-MDT-GTZ',
'LWY-LQ2J-B4R-ML4',
'V2P-LJPJ-C67-MCR',
'RT6-LRCT-NXP-MKX',
'WC4-Z627-699-CY6',
'W2D-J464-LLK-HNY',
'W7L-BKJ2-NKK-7CP',
'WN9-Y44H-M6N-C9N',
'WWN-6Y4N-MTQ-CHP',
'WBD-MZ4P-4BP-KJT',
'W6B-TGT6-KT6-NLK',
'W2N-NYDP-PBG-9V2',
'WG2-6XRG-TTT-LJB',
'WP9-9RRY-JYR-DT2',
'W4B-LRH9-WKK-CNH',
'WVR-DMR9-4TW-XD4',
'WNR-QHLL-H4M-DLG',
'W9X-W7GX-KYR-7L2',
'WJC-HGWJ-MDG-W4T',
'WGQ-DJB7-QGD-BVT',
'WPR-BDNH-4DK-X2V',
'WCX-WYPW-ZV2-6ZX',
'WZH-PBTH-KV6-9B4',
'WPP-XWKB-JTC-JMT',
'HHW-XZKY-7YV-DX9',
'HXR-7N2X-JTX-TNV',
'PQM-VKQ6-MYN-7MH',
'P4P-CGMB-7NV-V7L',
'PYL-MNK7-CDP-GK4',
'PWB-PR6D-62K-DLR',
'P4Q-6492-DJY-4TN',
'P2Z-PY4J-W7B-6J6',
'RMJ-WJD4-GD7-J2X',
'XQT-YZ29-2DB-KWG',
'42V-MRX6-27D-W6L',
'EW4-7CAB-9LC-8HU',
'6BY-QNYN-JRH-GBM',
'LP2-GYHR-VZX-QYZ',
'MDT-MTD7-VW2-P74',
'KVX-M2RY-KKG-K9R',
'ZLC-T2WC-CZM-QW4',
'KQC-BB9D-9KT-N4G',
'JWM-9J7X-ZYV-RZT',
'HBJ-4WKT-PWB-WT6',
'HKK-7Z6G-KNK-X2M',
'26Y-ZKVD-RCL-4HB',
'2PV-2VZK-GTL-HBW',
'PX6-JJRM-HCQ-C6M',
'PV6-C4LJ-HGX-72T',
'PHN-MNLB-TNC-Z94',
'P4P-YRWK-RZT-JYB',
'PQR-PDN9-LDM-LVK',
'P6N-Z6YG-K94-N9N',
'PKL-9MDD-Y2V-KWL',
'PKN-B6HJ-WH7-ZG2',
'PLG-6BWY-TGH-PL6',
'PTJ-M7P7-4WD-R4B',
'LH7-J67Z-Z69-PD6',
'RGW-QXG2-9QC-PND',
'RJH-2MLJ-Z4B-LNN',
'RDB-7JWB-JR4-V2N',
'7MH-VVHJ-2WL-RVH',
'7RH-M46D-662-BPR',
'TZ2-RQQY-JJK-H4V',
'6LX-NCRC-KDJ-B7X',
'QNQ-9KYY-TW4-WHG',
'QMG-YCKV-HRT-Q9Q',
'QYB-XG2H-9QD-B4W',
'QMB-J4YM-ZWY-TDG',
'LG7-XY7H-X4V-J9D',
'QMR-XLNC-647-LQ2',
'Q4V-69CH-QVX-DPH',
'QZD-XZVC-Q2R-BYL',
'LX4-2QTY-JRK-DT6',
'LG7-CT4Z-DWV-CVN',
'L72-4ZT2-VKM-P49',
'QJK-D4KQ-MMP-H7T',
'QJP-DR4D-7X2-NZN',
'QQJ-WBNV-N99-4LL',
'QTH-VXQR-NHB-KVJ',
'QPV-W2QZ-HRG-GDJ',
'LJR-NNTW-66X-NGQ',
'LMQ-RJH6-GZP-67R',
'L2P-MXNK-9RT-VK4',
'L9L-RRTY-PJR-7XG',
'LCY-XG94-W2K-XN9',
'LBB-7ZCH-2VW-6W6',
'Q6Z-X2R2-D9L-HWB',
'QNB-YR4K-Z2L-G2Y',
'QHV-YL4V-MYY-Z2G',
'WRL-77DY-NJT-CGH',
'WGP-W7BN-MNZ-7NQ',
'W7N-PYDB-QJC-2WH',
'WTG-LHLK-LCV-JVZ',
'WBZ-HPNX-M2C-TBP',
'WW2-6XRG-RNZ-7HL',
'WKB-2JDC-LJL-JT7',
'WWZ-NVMX-7Y7-GWR',
'W2L-2R2K-4HW-GCQ',
'DKK-RJ72-WT4-BHL',
'QMN-JGG6-PWX-N2R',
'Q96-9C7D-Z9Q-VXZ',
'QZ4-9M7K-BXD-WLQ',
'QYB-RCG6-9WM-VXK',
'QVK-YWBY-4MT-4GW',
'QTN-PNNQ-VWK-D9B',
'QHL-XL6P-GNC-MN7',
'QJG-M2V6-KYL-6LK',
'QBT-XWHT-NWZ-WPB',
'CKG-XVL2-D4B-GWQ',
'CQH-CQDP-JGW-6BG',
'CBW-97CT-9ZK-6C6',
'C6Y-Z7XT-CYY-9N2',
'C6P-249T-6WN-6LX',
'CCH-BL9V-7LB-C9V',
'C2V-7DXL-D22-C9P',
'CYC-DC7G-G6G-V49',
'CL6-PNZ2-WZY-QWX',
'CQB-R4VD-JP2-X2H',
'CJ7-BHLN-KTV-DHJ',
'CLP-44L9-4ZN-NTK',
'Q4L-6C7D-ZTT-VXV',
'Q2X-PNV9-XHH-Z66',
'Q9N-NMWW-LZG-RYP',
'QXG-YYVZ-LDY-ML2',
'LZR-9Q7D-JR9-VGW',
'Y2R-YC2J-MB9-GHC',
'J6P-ZDDM-DPY-H2N',
'CYN-HYLB-RTM-7LG',
'HQZ-Q2KX-HJJ-4RZ',
'DQX-DZVB-VHG-R69',
'42B-X9LW-96M-7WN',
'MCQ-KG77-9DT-NJ9',
'4NX-BXXB-6YC-TCQ',
'PYP-Y7GT-6ZW-7LP',
'Q7R-4MW6-2BH-BZC',
'PNG-HNMR-QJC-YJD',
'9MK-4Z4D-2YX-2LV',
'YB4-MD7G-MQD-GRQ',
'TNY-TB7M-W7J-LNK',
'Y4H-LZBJ-X7T-CY6',
'PL9-CG6X-ZBJ-7YX',
'4MJ-PCHN-V7J-LTM',
'QCQ-DMQC-2YQ-ZNQ',
'LGN-C4PD-WJ4-Z2W',
'XHG-LWBP-9NJ-Q2M',
'47J-NQNT-BKT-LCB',
'GZN-7Y9X-MCX-DCB',
'PZZ-JBJV-PQQ-BD9',
'LLY-HXHM-T2K-MXR',
'GW6-XVTV-ZGN-D6L',
'PB6-QZLT-QBL-HQX',
'CLJ-RTT2-46M-6BZ',
'MKB-CCRK-9YQ-VPL',
'VDR-QVJG-Z4X-72R',
'9V7-PM42-BZ9-H7R',
'9RT-JTDB-YBH-QGD',
'BJ9-QJRV-R7H-7CK',
'B7K-9YWJ-MJT-YDL',
'BWQ-BKBQ-V94-LZG',
'BBG-G9KP-ZK7-HZ6',
'J4D-4NGD-D2J-2LP',
'JHZ-B7RN-GV2-42V',
'J7J-RHC7-NYH-LH9',
'JGD-RG7G-4XH-H7J',
'JQG-ZXPX-ZYK-TDK',
'JB7-QHPM-YNP-ZX9',
'JC9-7CD7-XMM-HPK',
'JPR-QK6J-JBQ-N22',
'Z6R-ZLHT-6NW-N2J',
'J4R-4X49-YYB-KBV',
'GJC-BGJB-K2M-9X9',
'JM4-CXVW-X2L-6Y4',
'JKY-DWKH-D27-BPV',
'J6X-2X9L-K7H-JZN',
'JPQ-9RVL-2QR-TPL',
'J7Y-9ZJ7-DW6-XBH',
'J72-GHVJ-NHJ-QDZ',
'ZJM-K2VJ-VJM-WML',
'RKN-ZZZL-MVT-DJG',
'NQ6-JXG4-MJX-WR2',
'7Q4-9ZP6-BLD-N4X',
'M6H-PWM4-K7M-4QX',
'GVG-M4GH-TTZ-2P9',
'7V4-GG2B-P6K-V6K',
'VBD-29HW-KN7-XJ2',
'NMD-NMGB-2YG-MZZ',
'VPM-Z4WV-H7D-XX6',
'MKY-RJXY-D42-J6Y',
'MYX-ZV9J-DHB-JHQ',
'LMW-MJBZ-TTB-4JG',
'LLC-99DP-7VL-X7Y',
'6P2-2KQT-YLT-26C',
'NM6-LQ7H-X4J-QLC',
'XGK-DGLZ-XLX-JZG',
'NTY-2QNK-LKG-LP9',
'6KL-D77G-YRH-BXL',
'VCJ-XG7J-Q4H-YNV',
'6GR-DRTZ-VCH-7Z9',
'NQJ-XQPP-L4B-T94',
'GKG-KRKW-RZD-N2Y',
'LCX-HRZ6-QBZ-MMQ',
'RM2-RB97-YYR-GMV',
'NZN-DHVZ-CYX-NTT',
'6TX-XJTG-C9R-VHX',
'VDP-MRRD-LRM-J9C',
'R4Z-6WHM-VMK-XHH',
'N2K-HW2C-D7T-92Y',
'XK4-WYBD-7JM-T2K',
'NJR-7Z66-NCQ-M4Q',
'LLX-DGRM-C6Y-JL7',
'LMT-RP6V-GLJ-ZQ7',
'LXT-QWJN-NV9-KPC',
'R6R-PNNX-V7P-TJQ',
'KXM-92YN-B7R-DHQ',
'ZCN-WGBC-KTL-JH4',
'LRM-BW4D-PXW-N2D',
'LCL-PLVW-PM7-B2B',
'TLZ-RKVK-CLG-QXK',
'RKN-9BY2-WHY-NLJ',
]
itemsToSellLen = len(itemsToSell)
count = 0
for i in range(0, itemsToSellLen):
    if (count >= 9):
        foo = input("9 Codes entered, pausing")
        count = 0
    pyautogui.leftClick(
        mainLocation[0], mainLocation[1], 0, random.uniform(0.3, 0.7))
    # writeSleepEnter("+sell " + itemsToSell[i])
    writeSleepEnter(itemsToSell[i])
    print("Item " + str(i+1) + " of " +
          str(itemsToSellLen) + ": " + itemsToSell[i])
    pyautogui.moveTo(sellbutton[0], sellbutton[1])
    # sleepRandom(4, 7)
    sleepRandom(0.25, 0.6)
    current = pyautogui.position()
    if (current[0] != sellbutton[0] and current[1] != sellbutton[1]):
        pause = input("Pausing ")
    pyautogui.leftClick(sellbutton[0], sellbutton[1],
                        0, random.uniform(0.3, 0.7))
    sleepRandom(0.25, 0.6)
    count = count + 1
print("done")
quit()
