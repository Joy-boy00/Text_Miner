from sentiment_ranking import score_paragraph
import multitasking
@multitasking.task
def score(data,index):
    out = score_paragraph(data)
    print("processong ===> ",index)
    return out
if __name__ == "__main__":
    f = open("data.txt",'r',encoding='utf-8')
    huge_text = f.read()

    chunks = huge_text.split("\n") # splitting the huge text to paragraphs
    for i,chunk in enumerate(chunks):
        score(chunk,i)
    multitasking.wait_for_tasks()
    f.close()
