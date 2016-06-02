from tips import models


def load_tips_from_dlsv():
    tips = []
    f = tips_dlsv.split("\n")
    for index, title in enumerate(f):
        if '~~' not in title:
            continue
        tmp_item = {}
        tmp_item['title'] = title[2:]
        tmp_item['tip_author'] = f[index + 1]
        tmp_item['tip_text'] = f[index + 2]
        next = "multi line text"
        next_index = 3
        while next != "":
            next = f[index + next_index]
            tmp_item['tip_text'] += next
            next_index += 1
        tips.append(tmp_item)
    return tips


def save_tips(dic_tips):
    tips = [models.TipOfDay(**tip) for tip in dic_tips]
    for tip in tips:
        tip.save()


tips_dlsv = """
~~Saying #1: 10,000 Hours
Breck Yunits
There is a saying that it takes 10,000 hours of doing something to master it.
So, to master programming, it might take you 10,000 hours of being actively coding or thinking about coding. That translates to a consistent effort spread out over a number of years.


~~Saying #2: No Speed Limit
Breck Yunits
There is another saying that I just read, which inspired me to write this, that says “there is no speed limit”.
In that post, Derek Sivers claims that a talented and generous guy named Kimo Williams taught him 2 years worth of music theory in five lessons. I have been learning to program for 2 years, and despite the fact that I’ve made great progress, my process has been slow and inefficient.
I did not have a Kimo Williams. But now that I know a bit, I’ll try and emulate him and help you learn faster by sharing my top 12 lessons.


~~Get started.
Breck Yunits
Do not feel bad that you are not an expert programmer yet. In 10,000 hours, you will be. All you need to do is start. Dedicate some time each day or week to checking things off this list. You can take as long as you want or move as fast as you want. If you’ve decided to become a great programmer, youve already accomplished the hardest part: planting the seed. Now you just have to add time and your skills will blossom. If you need any help with any of these steps, feel free to email me and Ill do my best to help.


~~Dont worry.
Breck Yunits
Do not be intimated by how much you dont understand. Computers are still largely magic even to me. We all know that computers are fundamentally about 1s and 0s, but what the hell does that really mean? It took me a long time to figure it out–it has something to do with voltages and transistors. There are endless topics in computer science and endless terms that you won’t understand. But if you stick with it, eventually almost everything will be demystified.


~~Dont worry.
Breck Yunits
don’t waste time or get stressed worrying about what you don’t know. It will come, trust me. Remember, every great programmer at one time had NO IDEA what assembly was, or a compiler, or a pointer, or a class, or a closure, or a transistor. Many of them still dont! That’s part of the fun of this subject–you’ll always be learning.


~~Silicon Valley.
Breck Yunits
Simply by moving to Silicon Valley, you have at least: 10x as many programmers to talk to, 10x as many programming job opportunities, 10x as many programming meetups, and so on. You don’t have to do this, but it will make you move much faster. The first year of my programming career was in Boston. The second year was in San Francisco. I have learned at a much faster pace my second year.


~~Read books.
Breck Yunits
In December of 2007 I spent a few hundred dollars on programming books. I bought like 20 of them because I had no idea where to begin. I felt guilty spending so much money on books back then. Looking back, it was worth it hundreds of times over. You will read and learn more from a good $30 paperback book than dozens of free blogs. I could probably explain why, but its not even worth it. The data is so very clear from my experience that trying to explain why it is that way is like trying to explain why pizza tastes better than broccoli: Im sure there are reasons but just try pizza and you’ll agree with me.


~~Get mentors.
Breck Yunits
I used to create websites for small businesses. Sometimes my clients would want something I didnt know how to do, simple things back then like forms. I used to search Google for the answers, and if I couldnt find them, I’d panic! Dont do that. When you get in over your head, ping mentors. They dont mind, trust me. Something that youll spend 5 hours panicking to learn will take them 2 minutes to explain to you. If you dont know any good coders, feel free to use me as your first mentor.


~~Object Oriented.
Breck Yunits
This is the “language” the world codes in. Just as businessmen communicate primarily in English, coders communicate primarily in Object Oriented terms. Terms like classes and instances and inheritance. They were completely, completely, completely foreign and scary to me. Theyd make me sick to my stomach. Then I read a good book(Object Oriented PHP, Peter Lavin), and slowly practiced the techniques, and now I totally get it. Now I can communicate and work with other programmers.


~~Publish code.
Breck Yunits
If you keep a private journal and write the sentence The car green is, you may keep writing that hundreds of times without realizing its bad grammar, until you happen to come upon the correct way of doing things. If you write that in an email, someone will instantly correctly you and you probably won’t make the mistake again. You can speed up your learning 1-2 orders of magnitude by sharing your work with others. Its embarrassing to make mistakes, but the only way to become great is to trudge through foul smelling swamp of embarrassment.


~~Use github.
Breck Yunits
The term version control used to scare the hell out of me. Heck, it still can be pretty cryptic. But version control is crucial to becoming a great programmer. Every other developer uses it, and you can’t become a great programmer by coding alone, so you’ll have to start using it. Luckily, you’re learning during an ideal time. Github has made learning and using version control much easier. Also, Dropbox is a great tool that your mom could use and yet that has some of the powerful sharing and version control features of something like git.


~~Treat yourself.
Breck Yunits
Build things you think are cool. Build stuff you want to use. Its more fun to work on something you are interested in. Programming is like cooking, you don’t know if what you make is good until you taste it. If something you cook tastes like dog food, how will you know unless you taste it? Build things you are going to consume yourself and you’ll be more interested in making it taste not like dog food.


~~Write English.
Breck Yunits
Code is surprisingly more like English than like math. Great code is easy to read. In great code functions, files, classes and variables are named well. Comments, when needed, are concise and helpful. In great code the language and vocabulary is not elitist: it is easy for the layman to understand.


~~Treat yourself.
Breck Yunits
Build things you think are cool. Build stuff you want to use. Its more fun to work on something you are interested in. Programming is like cooking, you don’t know if what you make is good until you taste it. If something you cook tastes like dog food, how will you know unless you taste it? Build things you are going to consume yourself and you’ll be more interested in making it taste not like dog food.

~~Write English.
Breck Yunits
Code is surprisingly more like English than like math. Great code is easy to read. In great code functions, files, classes and variables are named well. Comments, when needed, are concise and helpful. In great code the language and vocabulary is not elitist: it is easy for the layman to understand.


~~Be prolific.
Breck Yunits
You dont paint the Mona Lisa by spending 5 years working on 1 piece. You create the Mona Lisa by painting 1000 different works, one of them eventually happens to be the Mona Lisa. Write web apps, iPhone apps, Javascript apps, desktop apps, command line tools: as many things as you want. Start a small new project every week or even every day. You eventually have to strike a balance between quantity and quality, but when you are young the goal should be quantity. Quality will come in time.


~~Learn Linux.
Breck Yunits
The command line is not user friendly. It will take time and lots of repetition to learn it. But again, its what the world uses, you’ll need at least a basic grasp of the command line to become a great programmer. When you get good at the command line, its actually pretty damn cool. Youll appreciate how much of what we depend on today was written over the course of a few decades. And youll be amazed at how much you can do from the command line. If you use Windows, get CYGWIN! I just found it a few months ago, and it is much easier and faster than running virtualized Linux instances.

"""
