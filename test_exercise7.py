import exercise7 as E7

def test_OUI_1():
    ''' OUI provided. '''
    mac_address="01:02:03"
    assert E7.getOUI(mac_address) == mac_address

def test_OUI_2():
    ''' Full MAC address. '''
    mac_address="81:72:65:43:23:78"
    assert E7.getOUI(mac_address) == "81:72:65"

def test_OUI_3():
    ''' Check shorter than OUI.  '''
    mac_address="01:2:03"
    UNDEFINED="GG:GG:GG"
    answer=E7.getOUI(mac_address)
    if(answer == UNDEFINED):
        assert answer == UNDEFINED
    elif(answer.upper() == UNDEFINED):
        print(f"Needs to be uppercase {UNDEFINED}.")
        assert answer.upper() == UNDEFINED
    else:
        print("Doesn't return correct result.")
        assert answer == UNDEFINED

def test_OUI_4():
    ''' Full MAC except missing a character. '''
    mac_address="65:43:23:E:7E:3C"
    UNDEFINED="GG:GG:GG"
    answer=E7.getOUI(mac_address)
    
    if(answer == UNDEFINED):
        assert answer == UNDEFINED
    elif(answer.upper() == UNDEFINED):
        print(f"Needs to be uppercase {UNDEFINED}.")
        assert answer.upper() == UNDEFINED
    else:
        print("Doesn't return correct result.")
        assert answer == UNDEFINED

def test_calcMAC_Manufacturer_IMPROPER_FORMAT():
    ''' Full MAC except ADDED a character. '''
    MAC_Prefix=["00:00:17", "00:07:E9","04:27:28", "04:26:65",
                "04:33:89","00:00:0C"]
    MAC_Manufacturer=["Oracle", "Intel Corporation", "Microsoft Corporation", 
                    "Apple, Inc.", "Huawei Technologies Co.,Ltd", "Cisco Systems, Inc", ]
    
    index=0
    mac_address=MAC_Prefix[index]+":1A:7E:3CD"
    UNDEFINED="IMPROPER FORMAT"
    answer=E7.calcMACManufacturer(MAC_Prefix, MAC_Manufacturer, mac_address)
    
    if(answer == UNDEFINED):
        assert answer == UNDEFINED
    elif(answer.upper() == UNDEFINED):
        print(f"Needs to be uppercase - {answer}.")
        assert answer.upper() == UNDEFINED
    else:
        print("Doesn't return correct result.")
        assert answer == UNDEFINED


def test_calcMAC_Manufacturer_0():
    ''' MAC_Prefix at index 0. '''
    MAC_Prefix=["00:00:17", "00:07:E9","04:27:28", "04:26:65",
                "04:33:89","00:00:0C"]
    MAC_Manufacturer=["Oracle", "Intel Corporation", "Microsoft Corporation", 
                    "Apple, Inc.", "Huawei Technologies Co.,Ltd", "Cisco Systems, Inc", ]
    
    index=0
    mac_address=MAC_Prefix[index]+":1A:7E:3C"
    answer=E7.calcMACManufacturer(MAC_Prefix, MAC_Manufacturer, mac_address)
    
    if(answer == MAC_Manufacturer[index]):
        assert answer == MAC_Manufacturer[index]
    elif(answer.upper() == MAC_Manufacturer[index].upper()):
        print(f"Needs to be uppercase - {answer}.")
        assert answer.upper() == MAC_Manufacturer[index].upper()
    else:
        print("Doesn't return correct result.")
        assert answer == MAC_Manufacturer[index]

def test_calcMAC_Manufacturer_1():
    ''' MAC_Prefix at index 1. '''
    MAC_Prefix=["00:00:17", "00:07:E9","04:27:28", "04:26:65",
                "04:33:89","00:00:0C"]
    MAC_Manufacturer=["Oracle", "Intel Corporation", "Microsoft Corporation", 
                    "Apple, Inc.", "Huawei Technologies Co.,Ltd", "Cisco Systems, Inc", ]
    
    index=1
    mac_address=MAC_Prefix[index]+":F0:7E:C3"
    answer=E7.calcMACManufacturer(MAC_Prefix, MAC_Manufacturer, mac_address)
    
    if(answer == MAC_Manufacturer[index]):
        assert answer == MAC_Manufacturer[index]
    elif(answer.upper() == MAC_Manufacturer[index].upper()):
        print(f"Needs to be uppercase - {answer}.")
        assert answer.upper() == MAC_Manufacturer[index].upper()
    else:
        print("Doesn't return correct result.")
        assert answer == MAC_Manufacturer[index]

def test_calcMAC_Manufacturer_2():
    ''' MAC_Prefix at index 2. '''
    MAC_Prefix=["00:00:17", "00:07:E9","04:27:28", "04:26:65",
                "04:33:89","00:00:0C"]
    MAC_Manufacturer=["Oracle", "Intel Corporation", "Microsoft Corporation", 
                    "Apple, Inc.", "Huawei Technologies Co.,Ltd", "Cisco Systems, Inc", ]
    
    index=2
    mac_address=MAC_Prefix[index]+":7E:AB:3C"
    answer=E7.calcMACManufacturer(MAC_Prefix, MAC_Manufacturer, mac_address)
    
    if(answer == MAC_Manufacturer[index]):
        assert answer == MAC_Manufacturer[index]
    elif(answer.upper() == MAC_Manufacturer[index].upper()):
        print(f"Needs to be uppercase - {answer}.")
        assert answer.upper() == MAC_Manufacturer[index].upper()
    else:
        print("Doesn't return correct result.")
        assert answer == MAC_Manufacturer[index]

def test_calcMAC_Manufacturer_3():
    ''' MAC_Prefix at index 3. '''
    MAC_Prefix=["00:00:17", "00:07:E9","04:27:28", "04:26:65",
                "04:33:89","00:00:0C"]
    MAC_Manufacturer=["Oracle", "Intel Corporation", "Microsoft Corporation", 
                    "Apple, Inc.", "Huawei Technologies Co.,Ltd", "Cisco Systems, Inc", ]
    
    index=3
    mac_address=MAC_Prefix[index]+":AA:7B:34"
    answer=E7.calcMACManufacturer(MAC_Prefix, MAC_Manufacturer, mac_address)
    
    if(answer == MAC_Manufacturer[index]):
        assert answer == MAC_Manufacturer[index]
    elif(answer.upper() == MAC_Manufacturer[index].upper()):
        print(f"Needs to be uppercase - {answer}.")
        assert answer.upper() == MAC_Manufacturer[index].upper()
    else:
        print("Doesn't return correct result.")
        assert answer == MAC_Manufacturer[index]

def test_calcMAC_Manufacturer_4():
    ''' MAC_Prefix at index 4. '''
    MAC_Prefix=["00:00:17", "00:07:E9","04:27:28", "04:26:65",
                "04:33:89","00:00:0C"]
    MAC_Manufacturer=["Oracle", "Intel Corporation", "Microsoft Corporation", 
                    "Apple, Inc.", "Huawei Technologies Co.,Ltd", "Cisco Systems, Inc", ]
    
    index=4
    mac_address=MAC_Prefix[index]+":1A:EE:DD"
    answer=E7.calcMACManufacturer(MAC_Prefix, MAC_Manufacturer, mac_address)
    
    if(answer == MAC_Manufacturer[index]):
        assert answer == MAC_Manufacturer[index]
    elif(answer.upper() == MAC_Manufacturer[index].upper()):
        print(f"Needs to be uppercase - {answer}.")
        assert answer.upper() == MAC_Manufacturer[index].upper()
    else:
        print("Doesn't return correct result.")
        assert answer == MAC_Manufacturer[index]

def test_calcMAC_Manufacturer_5():
    ''' MAC_Prefix at index 5. '''
    MAC_Prefix=["00:00:17", "00:07:E9","04:27:28", "04:26:65",
                "04:33:89","00:00:0C"]
    MAC_Manufacturer=["Oracle", "Intel Corporation", "Microsoft Corporation", 
                    "Apple, Inc.", "Huawei Technologies Co.,Ltd", "Cisco Systems, Inc", ]
    
    index=5
    mac_address=MAC_Prefix[index]+":23:E7:FE"
    answer=E7.calcMACManufacturer(MAC_Prefix, MAC_Manufacturer, mac_address)
    
    if(answer == MAC_Manufacturer[index]):
        assert answer == MAC_Manufacturer[index]
    elif(answer.upper() == MAC_Manufacturer[index].upper()):
        print(f"Needs to be uppercase - {answer}.")
        assert answer.upper() == MAC_Manufacturer[index].upper()
    else:
        print("Doesn't return correct result.")
        assert answer == MAC_Manufacturer[index]

def test_calcMAC_Manufacturer_UNKNOWN_1():
    ''' Full MAC not in MAC_Prefix array. '''
    MAC_Prefix=["00:00:17", "00:07:E9","04:27:28", "04:26:65",
                "04:33:89","00:00:0C"]
    MAC_Manufacturer=["Oracle", "Intel Corporation", "Microsoft Corporation", 
                    "Apple, Inc.", "Huawei Technologies Co.,Ltd", "Cisco Systems, Inc", ]
    
    index=0
    UNKNOWN="Unknown"
    mac_address="00:00:00"+":1A:7E:3C"
    answer=E7.calcMACManufacturer(MAC_Prefix, MAC_Manufacturer, mac_address)
    
    if(answer == UNKNOWN):
        assert answer == UNKNOWN
    elif(answer.upper() == UNKNOWN.upper()):
        print(f"Needs to be case sensitive - {answer}.")
        assert answer.upper() == UNKNOWN.upper()
    else:
        print("Doesn't return correct result.")
        assert answer == UNKNOWN

def test_calcMAC_Manufacturer_UNKNOWN_2():
    ''' Full MAC except not in MAC_Prefix. '''
    MAC_Prefix=["00:00:17", "00:07:E9","04:27:28", "04:26:65",
                "04:33:89","00:00:0C"]
    MAC_Manufacturer=["Oracle", "Intel Corporation", "Microsoft Corporation", 
                    "Apple, Inc.", "Huawei Technologies Co.,Ltd", "Cisco Systems, Inc", ]
    
    index=0
    UNKNOWN="Unknown"
    mac_address="FF:FF:FF"+":A1:CC:DE"
    answer=E7.calcMACManufacturer(MAC_Prefix, MAC_Manufacturer, mac_address)
    
    if(answer == UNKNOWN):
        assert answer == UNKNOWN
    elif(answer.upper() == UNKNOWN.upper()):
        print(f"Needs to be case sensitive - {answer}.")
        assert answer.upper() == UNKNOWN.upper()
    else:
        print("Doesn't return correct result.")
        assert answer == UNKNOWN

def test_calcMAC_Manufacturer_New_Array():
    ''' Mac Manufacturer at index 0 with new array. '''
    MAC_Prefix=["01:02:03"]
    MAC_Manufacturer=["Made-Up Company"]
    
    index=0
    mac_address=MAC_Prefix[index]+":04:05:06"
    answer=E7.calcMACManufacturer(MAC_Prefix, MAC_Manufacturer, mac_address)
    
    if(answer == MAC_Manufacturer[index]):
        assert answer == MAC_Manufacturer[index]
    elif(answer.upper() == MAC_Manufacturer[index].upper()):
        print(f"Needs to be uppercase - {answer}.")
        assert answer.upper() == MAC_Manufacturer[index].upper()
    else:
        print("Doesn't return correct result.")
        assert answer == MAC_Manufacturer[index]