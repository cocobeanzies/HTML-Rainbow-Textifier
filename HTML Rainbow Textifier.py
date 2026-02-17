colours = [
"#EF635B",
"#ED782D",
"#FCD05B",
"#8EE57E",
"#31EFE1",
"#6DADE7",
"#B896F4",
"#EA4965",
]
wainbow = []
i = 0

while True:
    no_wainbow = input("Please input your text! Go one paragraph at a time. If you are done, just hit enter again.").strip()
    if not no_wainbow:
        break
    answer = input('Would you like each character rainbowed, or each word rainbowed? Please reply "character" or "word": ').strip()
    match answer:
        case "character":
            no_wainbow_list = no_wainbow
        case "word":
            no_wainbow_list = no_wainbow.split()
        case _:
            print("Spell it right please, I'm too lazy to hardcode spelling mistakes. (￣ω￣)")
            continue
    if wainbow:
        wainbow.append("<br />\n")
    for c in no_wainbow_list:
        span = '<span style="color:' + colours[i % len(colours)] + '">' + c + "</span>"
        wainbow.append(span)
        i += 1
print("".join(wainbow))