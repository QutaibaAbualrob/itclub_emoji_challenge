



def example():
    unicode_str = "U+1FAE0"
    emoji = chr(int(unicode_str[2:], 16))
    print(emoji)


def hex_to_emoji(hx):
    if hx == "":
        return 
    emoji = chr(int(hx[2:], 16))
    return emoji


# Takes a dictionary that contains     emoji name : HEX VALUES and returns values which are the emojis
def dict_hex_to_emoji(dict):
    for key, value in dict.items():
        if key == "" or value =="":
            continue
        emojis = ""
        hexList = value.split(' ')
        if len(hexList) > 1:
            for hex in hexList:
                # To ignoreZero Width Joiner (ZWJ),
                #  used to combine emojis.
                if "U+200D" in hex:
                    continue
                emojis += hex_to_emoji(hex)
            dict[key] = emojis
        else:
            dict[key] = hex_to_emoji(value)
    return dict


#example()

# list = ['U+1F468', 'U+200D', 'U+1F3A8',]	

# for li in list:
#     print(hex_to_emoji(li))
