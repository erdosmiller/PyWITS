LOGICAL_RECORD_BEGIN = '&&\r\n' #HEX 26,26,OD,OA
LOGICAL_RECORD_END = '!!\r\n' #HEX 21,21,0D,0A
DATA_ITEM_SEPERATOR = '\r\n'
DATA_REQUEST = LOGICAL_RECORD_BEGIN + LOGICAL_RECORD_END
PASON_DATA_REQUEST = LOGICAL_RECORD_BEGIN + '0111-9999.0' + DATA_ITEM_SEPERATOR + LOGICAL_RECORD_END

if __name__ == '__main__':
    print repr(PASON_DATA_REQUEST)


