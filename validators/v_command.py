def convert_command(cmd_txt):
    eroare = ""
    try:
        tid = int(cmd_txt[0])
        day = int(cmd_txt[1])
        s = int(cmd_txt[2])
    except ValueError:
        eroare += "Please insert an valid integer"
        raise Exception(eroare)
    return [tid, day, s, cmd_txt[3]]
