from experta import *
from tkinter import *
from tkinter import messagebox



def Answer(word):
    app = Tk()
    app.title("Answer")
    app.iconbitmap(r'Images\SoundKitAid.ico')
    app.resizable(0, 0)
    ws = app.winfo_screenwidth()
    wh = app.winfo_screenheight()
    w = 650
    h = 450
    ws = app.winfo_screenwidth()
    hs = app.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    app.geometry('%dx%d+%d+%d' % (w, h, x, y))
    app.configure(bg="#141414")

    text = Text(app, width=80, height=27, border=0, relief=RAISED, bg="#141414", fg="white",
                font=("Jetbrains Mono", 10))
    text.insert(INSERT, 'The Answer is\n' + word)
    text.config(state=DISABLED)
    text.pack(expand=1, fill=BOTH)
    
    def destroy(v):
        global c
        c = v.get()
        if (c == ""):
            app.destroy()
            

    v = StringVar()
    b = Button(app, text="Close", font=("jetbrains mono", 30), relief='flat', highlightthickness=0, bd=0, bg="#350c35",
               fg="white", command=lambda: destroy(v)).place(x=250, y=300)
    app.mainloop()


c = ""

def ok(app, v):
    global c
    c = v.get()
    if (c == ""):
        messagebox.showwarning('Check Warning', 'Please Check Before You Go on')
    else:
        app.destroy()


def test(question, answers):
    global c
    c = ""

    app = Tk()
    app.title("ِAI tools Recommendation")
    app.iconbitmap(r'Images\SoundKitAid.ico')
    app.resizable(0, 0)
    ws = app.winfo_screenwidth()
    wh = app.winfo_screenheight()

    w = 650
    h = 450
    ws = app.winfo_screenwidth()
    hs = app.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    app.geometry('%dx%d+%d+%d' % (w, h, x, y))
    app.configure(bg="#141414")

    text = Label(app, text=question, bg='#141414', fg='white', font=("Jetbrains Mono", 14)).pack(pady=10)

    v = StringVar()
    b = Button(app, text="Next", font=("jetbrains mono", 30), relief='flat', highlightthickness=0, bd=0, bg="#350c35",
               fg="white", command=lambda: ok(app, v)).place(x=250, y=300)

    for i in range(len(answers)):
        Radiobutton(app, text=answers[i], variable=v, indicator=0, value=answers[i]
                    , relief='flat', highlightthickness=0, bd=0
                    , bg="#141414", fg="#bb1433", font=("Jetbrains Mono", 15)).pack(pady=5)
        

    
    app.mainloop()

    return c


class Sound_Kit_Aid(KnowledgeEngine):
    @Rule()
    def Start(self):
        x = test("Do you need a recommendation for Ai  tools ?", ['text tools','image tools', 'video and 3D tools'])
        self.declare(Fact(action=x))

    # image tools
    @Rule(Fact(action='image tools'))
    def image_home(self):
        x = test("Type of use?", ['tool powered by Dell', 'powered by Discord', 'vector Characters' , 'image editing tools'])
        self.declare(Fact(action=x))
        
    @Rule(Fact(action='image editing tools'))
    def image_editing(self):
        x = test("Type of use?", ['Adjust', 'remove Background'])
        self.declare(Fact(imageedit_action=x))   

    # image tools tool powered by Dell
    @Rule(Fact(action='powered by Discord'))
    def Discord(self):
        Answer(
            "\nMidjourney : \n https://www.midjourney.com/auth/signin/")

    @Rule(Fact(action='tool powered by Dell'))
    def Dell(self):
        Answer(
                         "\nDALL-E 2 :\n https://labs.openai.com/")
 
    @Rule(Fact(imageedit_action='Adjust'))
    def ajust(self):
        Answer(
                "\nbefunky photo editor :\n https://www.befunky.com/")
        
    @Rule(Fact(imageedit_action='remove Background'))
    def removebg(self):
        Answer(
                "\nRemove Background:\n https://www.remove.bg/")
    # vector Characters
    @Rule(Fact(action='vector Characters'))
    def vector(self):
        Answer(
             "\nfotor :\n https://www.fotor.com/features/ai-image-generator/")
       
        
        #############################################text tools####################################################### 
        
    @Rule(Fact(action='text tools'))
    def text_home(self):
        x = test("Type of use?", ['plagiarism and grammar', 'generate your own content', 'Ecommerce content' , 'article writer with 9 languages'])
        self.declare(Fact(action=x))
        
    @Rule(Fact(action='plagiarism and grammar'))
    def pgrammer(self):
        x = test("Type of use?", ['plagiarism tools', 'grammar tools'])
        self.declare(Fact(pg_action=x))   

    # image tools tool powered by Dell
    @Rule(Fact(action='generate your own content'))
    def own_content(self):
        Answer(
            "\nChibi AI: \n https://chibi.ai/")

    @Rule(Fact(action='tool powered by Dell'))
    def Dell(self):
        Answer(
                         "\nDALL-E 2 :\n https://labs.openai.com/")
 
    @Rule(Fact(pg_action='plagiarism tools'))
    def plagiarism(self):
        Answer(
                "\nJasper: \n https://www.jasper.ai")
        
    @Rule(Fact(pg_action='grammar tools'))
    def grammar(self):
        Answer(
                "\nGrammarly:\n https://www.grammarly.com")
    # vector Characters
    @Rule(Fact(action='Ecommerce content'))
    def Ecommerce_content(self):
        Answer(
             "\nCopySmith:\n https://app.copysmith.ai/")  
        
    @Rule(Fact(action='article writer with 9 languages'))
    def article(self):
        Answer(
             "\nKafKai:\n https://kafkai.com/en")   
        
        
        
   #################################################################video #######################################################################     
        
   
    @Rule(Fact(action='video and 3D tools'))
    def video_home(self):
        x = test("Type of use?", ['generate your own video with AI', 'Create Talking Interactive Video'])
        self.declare(Fact(action=x))
        
   

    # video tools generate your own video with AI
    @Rule(Fact(action='generate your own video with AI'))
    def own_Ai_video(self):
        Answer(
            "\nTopaz: \n https://www.topazlabs.com/")

    @Rule(Fact(action='Create Talking Interactive Video'))
    def Interactive_Video(self):
        Answer(
                         "\nD-DI:\n https://www.d-id.com/")
 
    # 4444444444444444444444444
    #   @Rule(Fact(Pc_mic_action ='no'))
    #  def content_maker_equipment(self):
    #     x = test("Do You have a microphone?", ['yes', 'no'])
    #    self.declare(Fact(pc_mic_action=x))

    # @Rule(Fact(content_maker_action ='no '))
    # def content_maker_equipment(self):
    #   x = test("Do you have A Personal Computer?", ['yes', 'no'])
    #  self.declare(Fact(content_maker_action=x))

    # 44444444444444444444444444444444444444444

    # image tools powered by Discord
  
# No noise




engine = Sound_Kit_Aid()
engine.reset()
engine.run()
