
# sumerian_untranslated.txt is the file extracted form cdli data-extracter

import re
stopping_chars=["@", "#", "&", "$"]
lines=[]


class Processing:
    
    def __init__(self,INPUT):
        self.INPUT=INPUT
        self.cleaned_summerian=[]
        

    def OPENfile(self,filename):
        lines=[]
        with open(filename, "r") as f:
            for line in f:
                line=line.strip()
                lines.append(line)
        return lines

    def savefile(self,filename,LIST):
        with open(filename, 'w') as f:
            for line in LIST:
                f.write("%s\n" % line)


    def processing_1(self,text_line):
        #x = re.sub(r"\[\.+\]","unk",text_line)
        #x = re.sub(r"...","unk",x)
        x = re.sub(r'\#', '', text_line)
        x = re.sub(r"\_", "", x)
        x = re.sub(r"\[", "", x)
        x = re.sub(r"\]", "", x)
        x = re.sub(r"\<", "", x)
        x = re.sub(r"\>", "", x)
        x = re.sub(r"\!", "", x)
        x = re.sub(r"@c", "", x)
        x = re.sub(r"@t", "", x)
        x = re.sub(r",", "", x)
        #x=re.sub(r"(x)+","x",x)
        x = re.sub(r"\?", "", x)
        x = x.split()
        x = " ".join(x)
        k = re.search(r"[a-wyzA-Z]+",x)
        if k:
            return x
        else:
            return ""

    def main(self):
        lines=self.OPENfile(self.INPUT)
        Original_sumerian_mono=[]
        for i in lines:
            if len(i)>0 and i[0] not in stopping_chars:
                index=i.find(".")
                l=i[index+1:].strip()
                Original_sumerian_mono.append(l)

        processed_summerian=[] 
        for i in range(len(Original_sumerian_mono)):
            text=self.processing_1(Original_sumerian_mono[i])
            if(re.search("\d\d\d\d\d",text)):
                continue
            if(len(text)>2):
                processed_summerian.append(text)
                
        self.cleaned_summerian=processed_summerian
        

        
        
if __name__=='__main__':
    
    obj=Processing('CDLI_Data/sumerian_untranslated.txt')    
    obj.main()
    result=obj.cleaned_summerian
    obj.savefile('CDLI_Data/Sumerian_monolingual_processed_new.txt',result)
    