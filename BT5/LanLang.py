
def countDDT(ls):
    c_danh = 0
    for w in ls:
        if typeOfWord(w) == "danh":
            c_danh += 1
    return c_danh==1
def typeOfWord(w):
    if w.endswith('lios') or w.endswith('liala'):
        return "tinh"
    if w.endswith('etr') or w.endswith('etra'):
        return "danh"
    if w.endswith('initis') or w.endswith('inites'):
        return "dong"
    return "none"
def trueLocation(ls):
    index_danh = ls.index()
#2 - kiem tra gioi tinh
def gender(w):
    if w.endswith('lios') or w.endswith('etr') or w.endswith('initis'):
        return   "nam"
    else:
        return   "nu"
def trueGender(ls):
    g = gender(ls[0])
    for w in ls:   
        if gender(w) != g:
            return False
    return True

ls = input().split()