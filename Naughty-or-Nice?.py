def what_list_am_i_on(actions):
    
    nice_count = 0
    naughty_count = 0
    
    for action in actions:
        if action[0] in ("b", "f", "k"):
            naughty_count += 1
        elif action[0] in ("g", "s", "n"):
            nice_count += 1
            
    if nice_count > naughty_count:
        return 'nice'
    else: return 'naughty'
