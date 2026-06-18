Max_subject=5
def collect_all():
    subject=[]
    entry=collect()
    subject.append(entry)
    print(subject)
    while len(subject)<Max_subject:
        if ask_y_n("Enter another subject-"):
            ele = collect()
            print(ele)
            subject.append(ele)
            print(subject)
        else:
            break
    if len(subject)==Max_subject:
        return("maximum subject reached")
    return(subject)
collect_all()
